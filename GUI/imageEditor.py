# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imageEditor.ui'
#
# Created: Fri Sep 11 16:24:50 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1000, 1000)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(1000, 1000))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.toolBar = QtGui.QGroupBox(self.centralwidget)
        self.toolBar.setGeometry(QtCore.QRect(0, 0, 50, 1000))
        self.toolBar.setMaximumSize(QtCore.QSize(50, 1000))
        self.toolBar.setTitle(_fromUtf8(""))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        self.Brush = QtGui.QPushButton(self.toolBar)
        self.Brush.setGeometry(QtCore.QRect(0, 60, 50, 50))
        self.Brush.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("paintbrush.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Brush.setIcon(icon)
        self.Brush.setIconSize(QtCore.QSize(35, 35))
        self.Brush.setCheckable(False)
        self.Brush.setAutoDefault(False)
        self.Brush.setDefault(False)
        self.Brush.setFlat(False)
        self.Brush.setObjectName(_fromUtf8("Brush"))
        self.Rectangle = QtGui.QPushButton(self.toolBar)
        self.Rectangle.setGeometry(QtCore.QRect(0, 180, 50, 50))
        self.Rectangle.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("rectangle.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Rectangle.setIcon(icon1)
        self.Rectangle.setIconSize(QtCore.QSize(35, 35))
        self.Rectangle.setObjectName(_fromUtf8("Rectangle"))
        self.BlackRec = QtGui.QPushButton(self.toolBar)
        self.BlackRec.setGeometry(QtCore.QRect(0, 320, 45, 35))
        self.BlackRec.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("blackRec.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BlackRec.setIcon(icon2)
        self.BlackRec.setIconSize(QtCore.QSize(45, 45))
        self.BlackRec.setObjectName(_fromUtf8("BlackRec"))
        self.LineLinker = QtGui.QPushButton(self.toolBar)
        self.LineLinker.setGeometry(QtCore.QRect(0, 120, 50, 50))
        self.LineLinker.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("diagLine.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LineLinker.setIcon(icon3)
        self.LineLinker.setIconSize(QtCore.QSize(35, 35))
        self.LineLinker.setObjectName(_fromUtf8("LineLinker"))
        self.Bucket = QtGui.QPushButton(self.toolBar)
        self.Bucket.setGeometry(QtCore.QRect(0, 240, 50, 50))
        self.Bucket.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("bucket.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Bucket.setIcon(icon4)
        self.Bucket.setIconSize(QtCore.QSize(35, 35))
        self.Bucket.setObjectName(_fromUtf8("Bucket"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArquivo = QtGui.QMenu(self.menubar)
        self.menuArquivo.setObjectName(_fromUtf8("menuArquivo"))
        self.menuSobre = QtGui.QMenu(self.menubar)
        self.menuSobre.setObjectName(_fromUtf8("menuSobre"))
        MainWindow.setMenuBar(self.menubar)
        self.actionAbrir = QtGui.QAction(MainWindow)
        self.actionAbrir.setObjectName(_fromUtf8("actionAbrir"))
        self.actionSalvar = QtGui.QAction(MainWindow)
        self.actionSalvar.setObjectName(_fromUtf8("actionSalvar"))
        self.actionDeletar = QtGui.QAction(MainWindow)
        self.actionDeletar.setObjectName(_fromUtf8("actionDeletar"))
        self.actionSair = QtGui.QAction(MainWindow)
        self.actionSair.setObjectName(_fromUtf8("actionSair"))
        self.actionFinalizar_Demarca_o = QtGui.QAction(MainWindow)
        self.actionFinalizar_Demarca_o.setObjectName(_fromUtf8("actionFinalizar_Demarca_o"))
        self.menuArquivo.addAction(self.actionAbrir)
        self.menuArquivo.addAction(self.actionFinalizar_Demarca_o)
        self.menuArquivo.addAction(self.actionSalvar)
        self.menuArquivo.addAction(self.actionDeletar)
        self.menuArquivo.addAction(self.actionSair)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuSobre.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionSair, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo", None))
        self.menuSobre.setTitle(_translate("MainWindow", "Sobre", None))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir...", None))
        self.actionSalvar.setText(_translate("MainWindow", "Salvar...", None))
        self.actionDeletar.setText(_translate("MainWindow", "Deletar", None))
        self.actionSair.setText(_translate("MainWindow", "Sair", None))
        self.actionFinalizar_Demarca_o.setText(_translate("MainWindow", "Finalizar Demarcação", None))

