import sys
from PyQt4 import *
from imageEditor import *
from PIL import Image, ImageDraw, ImageQt
from copy import *

# TODO
# Adicionar dialogos para: modificação de arquivos; avisar que a imagem não foi binarizada
# Adicionar ferramenta de zoom

class imageProcesser(QtGui.QWidget,QtGui.QWheelEvent):
    def __init__(self,parent = None):
        super(imageProcesser, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_StaticContents)
        self.setGeometry(50,0,2000,2000)


#==========================ATRIBUTES================================
        self.modified = False
        self.scribbling = False
        self.myPenWidth = 3
        self.myPenColor = QtCore.Qt.red
        self.image = QtGui.QImage()
        self.toBeSaved = QtGui.QImage()
        self.binImage = QtGui.QImage()
        self.lastPoint = QtCore.QPoint()
        self.recp1 = QtCore.QPoint(-1,-1)
        self.recp2 = QtCore.QPoint(-1,-1)
        self.pointNull = QtCore.QPoint(-1,-1)
        self.brushToggle = False
        self.recToggle = False
        self.lineToggle = False
        self.bucketToggle = False
        self.canDrawRec = True
        self.canSave = False
        self.fileName_ = None
        self.drawnPixels = set() 
        self.img = None 
        self.rThresh = 110
        self.gThresh = 50 
        self.bThresh = 50 
        self.linePoints = []
        self.imgList = []
        self.originalSize = None
        self.lastSize = None
        self.zoomFactor = 1.15
#=====================================================================


    def swapBuffers(self,img):
        pilToQt = ImageQt.ImageQt(img)
        self.image = pilToQt

    def openImage(self, fileName):
        #loadedImage = QtGui.QImage()
        #if not loadedImage.load(fileName):
            #return False

        name = 'p2.jpg'
        ##newSize = loadedImage.size().expandedTo(self.size())
        ##self.resizeImage(loadedImage, newSize)
        #self.image = loadedImage
        #self.fileName_ = fileName
        #self.img = Image.open(self.fileName_)
        self.fileName_ = name 
        #self.image.load(name)
        self.img = Image.open(name)
        self.swapBuffers(self.img)
        w,h = self.img.size
        #self.rectangleBuffer.fill(QtGui.qRgba(0,0,0,0))

        
        self.modified = False
        self.update()
        self.lastSize = self.originalSize = self.img.size
        return True

    def saveImage(self,fileName,fileFormat):
        visibleImage = self.image
        #self.resizeImage(visibleImage, self.size())
        if visibleImage.save(fileName,fileFormat):
            self.modified = False
            return True
        else:
            return False

    def clearImage(self):
        self.image.fill(QtGui.qRgb(255, 255, 255))
        self.modified = True
        self.canDrawRec = True
        self.recp1 = self.pointNull
        self.recp2 = self.pointNull
        self.img = None
        del self.linePoints[:]
        self.update()

    def wheelEvent(self,event):
        if self.fileName_:
            delta = event.delta()
            if delta > 0:
                self.zoom()
            else:
                self.zoomOut()

    def mousePressEvent(self, event):
        if self.brushToggle == True:
            if event.button() == QtCore.Qt.LeftButton:
                self.imgList.append((self.image.copy(),self.img.copy(),2)) #add the instance for the undo function
                self.lastPoint = event.pos()
                x = self.lastPoint.x()
                y = self.lastPoint.y()
                self.drawnPixels.add((x,y))
                self.scribbling = True
        elif self.recToggle == True:
            if event.button() == QtCore.Qt.LeftButton:
                if self.recp1 == self.pointNull:
                   self.recp1 = event.pos()
                #elif self.recp2 == self.pointNull:
                   #self.recp2 = event.pos()
                   #self.drawRec()
        elif self.lineToggle == True:
            if event.button() == QtCore.Qt.LeftButton:
                point = event.pos()
                x = point.x()
                y = point.y()
                self.linePoints.append((x,y))
                self.drawBetween()
        elif self.bucketToggle == True:
            if event.button() == QtCore.Qt.LeftButton:
                point = event.pos()
                x = point.x()
                y = point.y()
                self.floodFill((x,y))


    def mouseMoveEvent(self, event):
        if (event.buttons() & QtCore.Qt.LeftButton) and self.scribbling:
            point = event.pos()
            #x = point.x()
            #y = point.y()
            #self.drawnPixels.add((x,y))
            if self.brushToggle == True:
                self.drawLineTo(point)
        elif (event.buttons() & QtCore.Qt.LeftButton) and self.recToggle == True:
            point = event.pos()
            self.recp2 = point
            #self.rectangleBuffer.fill(QtGui.qRgba(0,0,0,0))
            self.drawRec()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.scribbling:
            point = event.pos()
            #x = point.x()
            #y = point.y()
            #self.drawnPixels.add((x,y))
            self.drawLineTo(point)
            self.scribbling = False

    def paintEvent(self, event):
        if self.fileName_:
            painter = QtGui.QPainter(self)
            painter.drawImage(self.image.rect(),self.image)

    def drawBetween(self):
        if len(self.linePoints) > 1:
            self.imgList.append((self.image.copy(),self.img.copy(),2)) #add the instance for the undo function
            painter = QtGui.QPainter(self.image)
            painter.setPen(QtGui.QPen(QtCore.Qt.red, self.myPenWidth,
                    QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
            start = self.linePoints[len(self.linePoints)-2]
            x1,y1 = start
            start = QtCore.QPoint(start[0],start[1])
            end = self.linePoints[len(self.linePoints)-1]
            x2,y2 = end
            end = QtCore.QPoint(end[0],end[1])
            painter.drawLine(start,end)
            draw = ImageDraw.Draw(self.img)
            draw.line(((x1,y1),(x2,y2)),(255,0,0))
            self.modified = True
            self.update()

    def floodFill(self,pixel):
        self.imgList.append((self.image.copy(),self.img.copy(),0)) #add the instance for the undo function
        pStack = [pixel]
        processedPixels = set()
        while len(pStack) > 0:
            x,y = pStack.pop()
            if (x,y) not in processedPixels:
                r,g,b = self.img.getpixel((x,y))
                processedPixels.add((x,y))
                if r > self.rThresh and g < self.gThresh and b < self.bThresh: # check if the pixel is red
                    self.img.putpixel((x,y),(255,255,255))
                else:
                    self.img.putpixel((x,y),(255,255,255))
                    pStack.append((x + 1, y))
                    pStack.append((x - 1, y))
                    pStack.append((x, y + 1))
                    pStack.append((x, y - 1))
        self.modified = True
        self.img.save('temp.png','PNG')
        self.image.load('temp.png')
        self.update()

            

    #def resizeEvent(self, event):
        #if self.width() > self.image.width() or self.height() > self.image.height():
            #newWidth = max(self.width() + 128, self.image.width())
            #newHeight = max(self.height() + 128, self.image.height())
            #self.resizeImage(self.image, QtCore.QSize(newWidth, newHeight))
            #self.update()

        #self.resizeImage(self.image, event.size())
        #super(imageProcesser, self).resizeEvent(event)

    def drawLineTo(self, endPoint):
        if self.fileName_:
            if self.brushToggle == True:
                painter = QtGui.QPainter(self.image)
                painter.setPen(QtGui.QPen(self.myPenColor, self.myPenWidth,
                        QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
                painter.drawLine(self.lastPoint, endPoint)
                self.modified = True
                self.update()
                x1 = self.lastPoint.x()
                y1 = self.lastPoint.y()
                x2 = endPoint.x()
                y2 = endPoint.y()
                self.drawnPixels.add((x2,y2))
                self.lastPoint = QtCore.QPoint(endPoint)
                draw = ImageDraw.Draw(self.img)
                draw.line(((x1,y1),(x2,y2)),(255,0,0))

    #def drawRec(self):
        #if self.recToggle == True and self.canDrawRec == True:
            #self.imgList.append((self.image.copy(),self.img.copy(),1)) #add the instance for the undo function
            #x = self.recp1.x()
            #y = self.recp1.y()
            #w = self.recp2.x() - self.recp1.x()
            #h = self.recp2.y() - self.recp1.y()
            #x2 = self.recp2.x()
            #y2 = self.recp2.y()
            #painter = QtGui.QPainter(self.image)
            #painter.setPen(QtGui.QPen(QtCore.Qt.red, self.myPenWidth,
                    #QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
            #painter.drawRect(x,y,w,h)
            #draw = ImageDraw.Draw(self.img)
            #draw.rectangle(((x,y),(x2,y2)),None,(255,0,0))
            #self.modified = True
            #self.canDrawRec = False
            #self.update()

    def drawRec(self):
        #if self.recToggle == True and self.canDrawRec == True:
            x = self.recp1.x()
            y = self.recp1.y()
            #w = self.recp2.x() - self.recp1.x()
            #h = self.recp2.y() - self.recp1.y()
            x2 = self.recp2.x()
            y2 = self.recp2.y()
            rectangleBuffer = Image.new('RGBA',self.img.size,(0,0,0,0))
            draw = ImageDraw.Draw(rectangleBuffer)
            draw.rectangle(((x,y),(x2,y2)),None,(255,0,0))
            temp = self.img.copy()
            temp.paste(rectangleBuffer, (0,0), rectangleBuffer)
            self.swapBuffers(temp)
            #painter = QtGui.QPainter(self.rectangleBuffer)
            #painter.setPen(QtGui.QPen(QtCore.Qt.red, self.myPenWidth,
                    #QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
            #painter.drawRect(x,y,w,h)
            #self.rectangleBuffer.save('ffs.png')
            #draw = ImageDraw.Draw(self.img)
            #draw.rectangle(((x,y),(x2,y2)),None,(255,0,0))
            #self.modified = True
            #self.canDrawRec = False
            self.update()

    def binarize(self):
        self.imgList.append((self.image.copy(),self.img.copy(),0)) #add the instance for the undo function
        self.toBeSaved = self.image.copy()
        self.toBeSaved = self.toBeSaved.scaled(w,h,QtCore.Qt.KeepAspectRatio)
        self.canSave = True
        draw = ImageDraw.Draw(self.img)
        (w,h) = self.img.size
        offset = 2
        xOrigin = self.recp1.x()
        xDestin = self.recp2.x()
        yOrigin = self.recp1.y()
        yDestin = self.recp2.y()
        xRange = range(xOrigin,xDestin)
        yRange = range(yOrigin,yDestin)
        for i in range (0,w):
            for j in range (0,h):
                if i not in xRange or j not in yRange:
                    self.img.putpixel((i,j),(0,0,0))

        for i in range (xOrigin+offset,xDestin+offset):
            for j in range (yOrigin+offset,yDestin+offset):
                r,g,b = self.img.getpixel((i,j)) 
                if r > self.rThresh and g > self.gThresh and b > self.bThresh: #check if it is white
                    self.img.putpixel((i,j),(255,255,255))
                elif r < self.rThresh: # if it isn't, check if it is a red one
                    self.img.putpixel((i,j),(0,0,0))

        self.img.save('temp.png','PNG')
        self.image.load('temp.png')
        self.update()

    def isModified(self):
        return self.modified

    def penColor(self):
        return self.myPenColor

    def penWidth(self):
        return self.myPenWidth

    def changeBlack(self):
        self.myPenColor = QtCore.Qt.black
        self.myPenWidth = 3

    def undo(self):
        if len(self.imgList) > 0:
            self.image,self.img,ret = self.imgList.pop()
            if len(self.linePoints) > 0 and ret == 2:
                del self.linePoints[-1:]
            elif ret == 1:
                self.recp1 = self.recp2 = self.pointNull
                self.canDrawRec = True
            self.update()

    def zoom(self):
        w = int(round(self.image.width() * self.zoomFactor))
        h = int(round(self.image.height() * self.zoomFactor))
        #self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(self.image))
        self.img = self.img.resize((w,h), Image.BICUBIC)
        self.img.save('temp.png','PNG')
        self.image.load('temp.png')
        if self.recp1 != self.pointNull and self.recp2 != self.pointNull:
            self.setRecp(w,h)
            self.lastSize = (w,h)
        self.update()

    def zoomOut(self):
        w = float(self.image.width()) / self.zoomFactor
        w = int(round(w))
        h = float(self.image.height()) / self.zoomFactor
        h = int(round(h))
        if w >= self.originalSize[0] and h >= self.originalSize[1]:
            #self.setGeometry(50,0,w,h)
            #self.image = self.image.scaled(w,h,QtCore.Qt.KeepAspectRatio)
            self.img = self.img.resize((w,h), Image.BICUBIC)
            self.img.save('temp.png','PNG')
            self.image.load('temp.png')
            if self.recp1 != self.pointNull and self.recp2 != self.pointNull:
                self.setRecp(w,h)
                self.lastSize = (w,h)
            self.update()

    def setOriginalSize(self):
        w,h = self.originalSize
        if (self.img.size != (w,h)):
            self.img = self.img.resize((w,h), Image.BICUBIC)
            self.img.save('temp.png','PNG')
            #self.setGeometry(50,0,w,h)
            self.image.load('temp.png')
            if self.recp1 != self.pointNull and self.recp2 != self.pointNull:
                self.setRecp(w,h)
                self.lastSize = (w,h)
            self.update()

    def setRecp(self,w,h):
        self.recp1.setX(int(round((self.recp1.x()*w)/self.lastSize[0])))
        self.recp1.setY(int(round((self.recp1.y()*h)/self.lastSize[1])))
        self.recp2.setX(int(round((self.recp2.x()*w)/self.lastSize[0])))
        self.recp2.setY(int(round((self.recp2.y()*h)/self.lastSize[1])))

        

class gui(QtGui.QMainWindow, Ui_MainWindow,QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)

        self.setupUi(self)
        self.scribbler = imageProcesser(self.centralwidget)
# =======================SCROLL=======================================

        #self.scrollArea = QtGui.QScrollArea()
        #self.scrollArea.setBackgroundRole(QtGui.QPalette.Dark)
        #self.scrollArea.setGeometry(self.scribbler.rect())
        #self.scrollArea.setWidget(self.scribbler)
        #self.scrollArea.setWidgetResizable(True)
        #self.scrollArea.setFixedHeight(400)
        #self.scrollArea.setFixedWidth(400)
        #self.scrollArea.setStyleSheet("QScrollArea {background-color:transparent;}")
        #self.scribbler.setStyleSheet("background-color:transparent;")

        #self.imageLabel = QtGui.QLabel(self.scrollArea)
        #self.imageLabel.setGeometry(self.scribbler.rect())
        #self.imageLabel.setSizePolicy(QtGui.QSizePolicy.Ignored,
                #QtGui.QSizePolicy.Ignored)
        #self.imageLabel.setScaledContents(True)

#===================================================================

        QtCore.QObject.connect(self.actionAbrir, QtCore.SIGNAL(("activated()")), self.openFile)
        QtCore.QObject.connect(self.actionDeletar, QtCore.SIGNAL(("activated()")), self.scribbler.clearImage)
        QtCore.QObject.connect(self.actionSalvar, QtCore.SIGNAL(("activated()")), self.save)
        QtCore.QObject.connect(self.actionFinalizar_Demarca_o, QtCore.SIGNAL(("activated()")), self.scribbler.binarize)
        QtCore.QObject.connect(self.actionDesfazer, QtCore.SIGNAL(("activated()")), self.scribbler.undo)
        QtCore.QObject.connect(self.actionAmpliar, QtCore.SIGNAL(("activated()")), self.scribbler.zoom)
        QtCore.QObject.connect(self.actionReduzir_uma_vez, QtCore.SIGNAL(("activated()")), self.scribbler.zoomOut)
        QtCore.QObject.connect(self.actionTamanho_Original, QtCore.SIGNAL(("activated()")), self.scribbler.setOriginalSize)

        self.Brush.clicked.connect(self.toggleBrush)
        self.Rectangle.clicked.connect(self.toggleRec)
        self.LineLinker.clicked.connect(self.toggleLines)
        self.Bucket.clicked.connect(self.toggleBucket)
        self.BlackRec.clicked.connect(self.scribbler.changeBlack)
        self.f = None

    def openFile(self):
        #fileName = QtGui.QFileDialog.getOpenFileName(self, "Abrir Imagem")
        fileName = 'batata'
        #if fileName:
        self.scribbler.openImage(fileName)
            #self.scribbler.setGeometry(50,0,self.scribbler.image.width(),self.scribbler.image.height())

    def save(self):
        if self.scribbler.canSave == True:
            fileNameSave = QtGui.QFileDialog.getSaveFileName(self, "Salvar Imagem","/home/untitled.png",("Images (*.png)"))
            self.scribbler.toBeSaved.save(fileNameSave)
            self.scribbler.img.save('temp.png','PNG')
            self.scribbler.fileName_ = fileNameSave
            self.outputManipulation()

    def outputManipulation(self):
        splits = self.scribbler.fileName_.split('/')
        output = '/'.join(splits[:-1])
        output = output + '/output.txt'
        self.f = open(output,"w")
        x1 = self.scribbler.recp1.x()
        y1 = self.scribbler.recp1.y()
        x2 = self.scribbler.recp2.x()
        y2 = self.scribbler.recp2.y()
        self.f.write(self.scribbler.fileName_ + '\n')
        self.f.write(str(self.scribbler.image.width()) + ' ' +  str(self.scribbler.image.height()) + '\n')
        self.f.write('(' + str(x1) +','+str(y1) + ')' + '  ' + '(' + str(x2) +','+str(y2) + ')' + '\n')
        self.scribbler.image.save('temp.png')
        img = Image.open('temp.png')
        img = img.resize(self.originalSize, Image.BICUBIC)
        for j in range (y1,y2):
            for i in range (x1,x2):
                r,g,b = img.getpixel((i,j))
                if (r,g,b) == (255,255,255):
                    self.f.write('1')
                else:
                    self.f.write('0')
            self.f.write('\n')

    def toggleBrush(self):
        if self.scribbler.brushToggle == False:
            self.Brush.setDefault(True)
            self.scribbler.brushToggle = True
            self.scribbler.recToggle = False
            self.scribbler.lineToggle = False
            del self.scribbler.linePoints[:]
            self.scribbler.bucketToggle = False
        else:
            self.Brush.setDefault(False)
            self.scribbler.brushToggle = False

    def toggleRec(self):
        if self.scribbler.recToggle == False:
            self.Rectangle.setDefault(True)
            self.scribbler.recToggle = True
            self.scribbler.brushToggle = False
            self.scribbler.lineToggle = False
            del self.scribbler.linePoints[:]
            self.scribbler.bucketToggle = False
        else:
            self.Rectangle.setDefault(False)
            self.scribbler.recToggle = False

    def toggleLines(self):
        if self.scribbler.lineToggle == False:
            self.LineLinker.setDefault(True)
            self.scribbler.recToggle = False
            self.scribbler.brushToggle = False
            self.scribbler.lineToggle = True
            self.scribbler.bucketToggle = False
        else:
            self.LineLinker.setDefault(False)
            self.scribbler.lineToggle = False
            del self.scribbler.linePoints[:]

    def toggleBucket(self):
        if self.scribbler.bucketToggle == False:
            self.Bucket.setDefault(True)
            self.scribbler.recToggle = False
            self.scribbler.brushToggle = False
            self.scribbler.lineToggle = False
            del self.scribbler.linePoints[:]
            self.scribbler.bucketToggle = True
        else:
            self.Bucket.setDefault(False)
            self.scribbler.bucketToggle = False
