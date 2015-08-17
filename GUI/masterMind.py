import sys
from PyQt4 import *
from imageEditor import *

class gui(QtGui.QMainWindow, Ui_MainWindow,QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        QtCore.QObject.connect(self.actionAbrir, QtCore.SIGNAL(("activated()")), self.openFile)
        
    def openFile(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self, "Abrir Imagem")
