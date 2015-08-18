import sys
from PyQt4 import *
from imageEditor import *

class gui(QtGui.QMainWindow, Ui_MainWindow,QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        QtCore.QObject.connect(self.actionAbrir, QtCore.SIGNAL(("activated()")), self.openFile)
        self.hbox = QtGui.QHBoxLayout(self.imageLoader)
        self.lbl = QtGui.QLabel(self.imageLoader)
        self.image = QtGui.QImage()
        
    def openFile(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self, "Abrir Imagem")
        if fileName:
            point = QtCore.QPoint(0,0)            
            size = QtCore.QSize(self.image.width(), self.image.height())
            self.image.load(fileName)
            painter = QtGui.QPainter(self.image)
            print (self.image.width(), self.image.height())
            #painter.drawImage(point,self.image)
            pixmap = QtGui.QPixmap(fileName)
            self.lbl.setPixmap(pixmap)
            self.hbox.addWidget(self.lbl)
            self.imageLoader.setLayout(self.hbox)
