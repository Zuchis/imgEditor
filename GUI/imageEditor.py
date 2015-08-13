# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imageEditor.ui'
#
# Created: Thu Aug 13 17:19:21 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(707, 539)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolBar = QtWidgets.QGroupBox(self.centralwidget)
        self.toolBar.setGeometry(QtCore.QRect(0, 0, 51, 581))
        self.toolBar.setTitle("")
        self.toolBar.setObjectName("toolBar")
        self.Brush = QtWidgets.QPushButton(self.toolBar)
        self.Brush.setGeometry(QtCore.QRect(0, 60, 41, 41))
        self.Brush.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("paintbrush.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Brush.setIcon(icon)
        self.Brush.setIconSize(QtCore.QSize(41, 41))
        self.Brush.setObjectName("Brush")
        self.Rectangle = QtWidgets.QPushButton(self.toolBar)
        self.Rectangle.setGeometry(QtCore.QRect(0, 180, 41, 41))
        self.Rectangle.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("rectangle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Rectangle.setIcon(icon1)
        self.Rectangle.setIconSize(QtCore.QSize(41, 41))
        self.Rectangle.setObjectName("Rectangle")
        self.imageLoader = QtWidgets.QGroupBox(self.centralwidget)
        self.imageLoader.setGeometry(QtCore.QRect(50, 0, 761, 601))
        self.imageLoader.setTitle("")
        self.imageLoader.setObjectName("imageLoader")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 707, 25))
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setObjectName("menuArquivo")
        self.menuSobre = QtWidgets.QMenu(self.menubar)
        self.menuSobre.setObjectName("menuSobre")
        MainWindow.setMenuBar(self.menubar)
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionSalvar = QtWidgets.QAction(MainWindow)
        self.actionSalvar.setObjectName("actionSalvar")
        self.actionDeletar = QtWidgets.QAction(MainWindow)
        self.actionDeletar.setObjectName("actionDeletar")
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.menuArquivo.addAction(self.actionAbrir)
        self.menuArquivo.addAction(self.actionSalvar)
        self.menuArquivo.addAction(self.actionDeletar)
        self.menuArquivo.addAction(self.actionSair)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuSobre.menuAction())

        self.retranslateUi(MainWindow)
        self.actionSair.activated.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))
        self.menuSobre.setTitle(_translate("MainWindow", "Sobre"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir..."))
        self.actionSalvar.setText(_translate("MainWindow", "Salvar..."))
        self.actionDeletar.setText(_translate("MainWindow", "Deletar"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))

