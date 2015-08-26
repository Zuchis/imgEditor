import sys
from PyQt4 import *
from imageEditor import *

class imageProcesser(QtGui.QWidget):
    def __init__(self, parent=None):
        super(imageProcesser, self).__init__(parent)

        self.setAttribute(QtCore.Qt.WA_StaticContents)
        self.setGeometry(50,0,950,1000)
        self.modified = False
        self.scribbling = False
        self.myPenWidth = 5
        self.myPenColor = QtCore.Qt.red
        self.image = QtGui.QImage()
        self.lastPoint = QtCore.QPoint()
        self.brushToggle = False

    def openImage(self, fileName):
        loadedImage = QtGui.QImage()
        if not loadedImage.load(fileName):
            return False

        #newSize = loadedImage.size().expandedTo(self.size())
        #self.resizeImage(loadedImage, newSize)
        self.image = loadedImage
        self.modified = False
        self.update()
        return True

    def saveImage(self,fileName,fileFormat):
        visibleImage = self.image
        self.resizeImage(visibleImage, self.size())

        if visibleImage.save(fileName,fileFormat):
            self.modified = False
            return True
        else:
            return False

    def clearImage(self):
        self.image.fill(QtGui.qRgb(255, 255, 255))
        self.modified = True
        self.update()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.lastPoint = event.pos()
            self.scribbling = True

    def mouseMoveEvent(self, event):
        if (event.buttons() & QtCore.Qt.LeftButton) and self.scribbling:
            self.drawLineTo(event.pos())

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.scribbling:
            self.drawLineTo(event.pos())
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
            #rad = self.myPenWidth / 2 + 2
            #self.update(QtCore.QRect(self.lastPoint, endPoint).normalized().adjusted(-rad, -rad, +rad, +rad))
            self.update()
            #print(self.image.width(),self.image.height())
            #print(self.lastPoint)
            self.lastPoint = QtCore.QPoint(endPoint)
            #print

    #def resizeImage(self, image, newSize):
        #if image.size() == newSize:
            #return

        #newImage = QtGui.QImage(newSize, QtGui.QImage.Format_RGB32)
        #newImage.fill(QtGui.qRgb(255, 255, 255))
        #painter = QtGui.QPainter(newImage)
        #painter.drawImage(QtCore.QPoint(0, 0), image)
        #self.image = newImage

    def isModified(self):
        return self.modified

    def penColor(self):
        return self.myPenColor

    def penWidth(self):
        return self.myPenWidth

    def toggleBrush(self):
        if self.brushToggle == False:
            self.brushToggle = True
        else:
            self.brushToggle = False
                     
class gui(QtGui.QMainWindow, Ui_MainWindow,QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        QtCore.QObject.connect(self.actionAbrir, QtCore.SIGNAL(("activated()")), self.openFile)
        self.scribbler = imageProcesser(self.centralwidget)
        QtCore.QObject.connect(self.actionDeletar, QtCore.SIGNAL(("activated()")), self.scribbler.clearImage)
        self.Brush.clicked.connect(self.scribbler.toggleBrush)
        #self.setCentralWidget(self.scribbler)

    def openFile(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self, "Abrir Imagem")
        if fileName:
            self.scribbler.openImage(fileName)
            #pixmap = QtGui.QPixmap(fileName)
            #self.lbl.setPixmap(pixmap)
            #self.hbox.addWidget(self.lbl)
            #self.imageLoader.setLayout(self.hbox)

    def save(self):
        action = self.sender()
        fileFormat = action.data()
        self.saveFile(fileFormat)
