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
            self.image.load(fileName)
            print (self.image.width(), self.image.height())
            self.imageLoader.update()
            #pixmap = QtGui.QPixmap(fileName)
            #self.lbl.setPixmap(pixmap)
            #self.hbox.addWidget(self.lbl)
            #self.imageLoader.setLayout(self.hbox)

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.loadTheImage(qp)
        qp.end()

    def loadTheImage(self,qp):
        qp.drawImage(0,0,self.image)
        
