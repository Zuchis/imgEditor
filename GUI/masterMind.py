import sys
from PyQt4 import *
from imageEditor import *
from PIL import Image, ImageDraw

# TODO
# Adicionar dialogos para modificação de arquivos, avisar que a imagem não foi binarizada

class imageProcesser(QtGui.QWidget):
    def __init__(self, parent=None):
        super(imageProcesser, self).__init__(parent)

        self.setAttribute(QtCore.Qt.WA_StaticContents)
        self.setGeometry(50,0,950,1000)
        self.modified = False
        self.scribbling = False
        self.myPenWidth = 1
        self.myPenColor = QtCore.Qt.red
        self.image = QtGui.QImage()
        self.binImage = QtGui.QImage()
        self.lastPoint = QtCore.QPoint()
        self.recp1 = QtCore.QPoint(-1,-1)
        self.recp2 = QtCore.QPoint(-1,-1)
        self.pointNull = QtCore.QPoint(-1,-1)
        self.brushToggle = False
        self.recToggle = False
        self.canDrawRec = True
        self.canSave = False
        self.fileName_ = None
        self.drawnPixels = set() 

    def openImage(self, fileName):
        loadedImage = QtGui.QImage()
        if not loadedImage.load(fileName):
            return False

        #newSize = loadedImage.size().expandedTo(self.size())
        #self.resizeImage(loadedImage, newSize)
        self.image = loadedImage
        self.fileName_ = fileName
        self.modified = False
        self.update()
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
        self.update()

    def mousePressEvent(self, event):
        if self.brushToggle == True:
            if event.button() == QtCore.Qt.LeftButton:
                self.lastPoint = event.pos()
                x = self.lastPoint.x()
                y = self.lastPoint.y()
                self.drawnPixels.add((x,y))
                self.scribbling = True
        elif self.recToggle == True:
            if event.button() == QtCore.Qt.LeftButton:
                if self.recp1 == self.pointNull:
                   self.recp1 = event.pos()
                   #print (self.recp1)
                elif self.recp2 == self.pointNull:
                   self.recp2 = event.pos()
                   #print (self.recp2)
                   self.drawRec()

    def mouseMoveEvent(self, event):
        if (event.buttons() & QtCore.Qt.LeftButton) and self.scribbling:
            point = event.pos()
            #x = point.x()
            #y = point.y()
            #self.drawnPixels.add((x,y))
            self.drawLineTo(point)

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.scribbling:
            point = event.pos()
            #x = point.x()
            #y = point.y()
            #self.drawnPixels.add((x,y))
            self.drawLineTo(point)
            self.scribbling = False

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(event.rect(), self.image)


    #def resizeEvent(self, event):
        #if self.width() > self.image.width() or self.height() > self.image.height():
            #newWidth = max(self.width() + 128, self.image.width())
            #newHeight = max(self.height() + 128, self.image.height())
            #self.resizeImage(self.image, QtCore.QSize(newWidth, newHeight))
            #self.update()

        #self.resizeImage(self.image, event.size())
        #super(imageProcesser, self).resizeEvent(event)

    def drawLineTo(self, endPoint):
        if self.brushToggle == True:
            painter = QtGui.QPainter(self.image)
            painter.setPen(QtGui.QPen(self.myPenColor, self.myPenWidth,
                    QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
            painter.drawLine(self.lastPoint, endPoint)
            self.modified = True
            self.update()
            x = endPoint.x()
            y = endPoint.y()
            self.drawnPixels.add((x,y))
            self.lastPoint = QtCore.QPoint(endPoint)

    def drawRec(self):
        if self.recToggle == True and self.canDrawRec == True:
            x = self.recp1.x()
            y = self.recp1.y()
            w = self.recp2.x() - self.recp1.x()
            h = self.recp2.y() - self.recp1.y()
            painter = QtGui.QPainter(self.image)
            painter.setPen(QtGui.QPen(self.myPenColor, self.myPenWidth,
                    QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
            painter.drawRect(x,y,w,h)
            self.modified = True
            self.canDrawRec = False
            self.update()

    def binarize(self):
        fileNameSave = QtGui.QFileDialog.getSaveFileName(self, "Salvar Imagem","/home/untitled.png",("Images (*.png)"))
        self.image.save(fileNameSave)
        self.fileName_ = fileNameSave
        self.canSave = True
        img = Image.open(fileNameSave)
        draw = ImageDraw.Draw(img)
        (w,h) = img.size
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
                    img.putpixel((i,j),(0,0,0))

        for i in range (xOrigin+offset,xDestin+offset):
            for j in range (yOrigin+offset,yDestin+offset):
                r,g,b = img.getpixel((i,j)) 
                if r > 200:
                    img.putpixel((i,j),(255,255,255))
                else:
                    img.putpixel((i,j),(0,0,0))

        for j in range (yOrigin+offset,yDestin+offset):
            startPoint = (-1,-1)
            endPoint = (-1,-1)
            for i in range (xOrigin+offset,xDestin+offset):
                if (i,j) in self.drawnPixels:
                    if startPoint == (-1,-1):
                        startPoint = (i,j)
                    elif endPoint == (-1,-1):
                        endPoint = (i,j)
                        draw.line((startPoint,endPoint),(255,255,255))
                        startPoint = (-1,-1)
                        endPoint = (-1,-1)

        #for set_ in self.drawnPixels:
            #for j in range (yOrigin+offset,yDestin+offset):
                #for i in range (xOrigin+offset,xDestin+offset):
                    #startPoint = (-1,-1)
                    #endPoint = (-1,-1)
                    #if (i,j) in set_:
                        #if startPoint == (-1,-1):
                            #startPoint = (i,j)
                        #elif endPoint == (-1,-1):
                            #endPoint = (i,j)
                #if startPoint in set_ and endPoint in set_:
                    #draw.line((startPoint,endPoint),(255,255,255))

        #for set_ in self.drawnPixels:
            #for setMember

        img.save('temp.png','PNG')
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

    def toggleBrush(self):
        if self.brushToggle == False:
            self.brushToggle = True
            self.recToggle = False
        else:
            self.brushToggle = False

    def toggleRec(self):
        if self.recToggle == False:
            self.recToggle = True
            self.brushToggle = False
        else:
            self.recToggle = False

class gui(QtGui.QMainWindow, Ui_MainWindow,QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        QtCore.QObject.connect(self.actionAbrir, QtCore.SIGNAL(("activated()")), self.openFile)
        self.scribbler = imageProcesser(self.centralwidget)
        QtCore.QObject.connect(self.actionDeletar, QtCore.SIGNAL(("activated()")), self.scribbler.clearImage)
        QtCore.QObject.connect(self.actionSalvar, QtCore.SIGNAL(("activated()")), self.save)
        QtCore.QObject.connect(self.actionFinalizar_Demarca_o, QtCore.SIGNAL(("activated()")), self.scribbler.binarize)
        self.Brush.clicked.connect(self.scribbler.toggleBrush)
        self.Rectangle.clicked.connect(self.scribbler.toggleRec)
        self.BlackRec.clicked.connect(self.scribbler.changeBlack)
        self.f = None
        #self.setCentralWidget(self.scribbler)

    def openFile(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self, "Abrir Imagem")
        if fileName:
            self.scribbler.openImage(fileName)
            self.scribbler.setGeometry(50,0,self.scribbler.image.width(),self.scribbler.image.height())

    def save(self):
        if self.scribbler.canSave == True:
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
        for j in range (y1,y2):
            for i in range (x1,x2):
                r,g,b = img.getpixel((i,j))
                if (r,g,b) == (255,255,255):
                    self.f.write('1')
                else:
                    self.f.write('0')
            self.f.write('\n')
