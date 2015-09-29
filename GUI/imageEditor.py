# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imageEditor.ui'
#
# Created: Tue Sep 29 18:34:51 2015
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
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(10)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 278, 278))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setMargin(5)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArquivo = QtGui.QMenu(self.menubar)
        self.menuArquivo.setObjectName(_fromUtf8("menuArquivo"))
        self.menuSobre = QtGui.QMenu(self.menubar)
        self.menuSobre.setObjectName(_fromUtf8("menuSobre"))
        self.menuEditar = QtGui.QMenu(self.menubar)
        self.menuEditar.setObjectName(_fromUtf8("menuEditar"))
        self.menuReduzir = QtGui.QMenu(self.menuEditar)
        self.menuReduzir.setObjectName(_fromUtf8("menuReduzir"))
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
        self.actionDesfazer = QtGui.QAction(MainWindow)
        self.actionDesfazer.setObjectName(_fromUtf8("actionDesfazer"))
        self.actionAmpliar = QtGui.QAction(MainWindow)
        self.actionAmpliar.setObjectName(_fromUtf8("actionAmpliar"))
        self.actionReduzir_uma_vez = QtGui.QAction(MainWindow)
        self.actionReduzir_uma_vez.setObjectName(_fromUtf8("actionReduzir_uma_vez"))
        self.actionTamanho_Original = QtGui.QAction(MainWindow)
        self.actionTamanho_Original.setObjectName(_fromUtf8("actionTamanho_Original"))
        self.menuArquivo.addAction(self.actionAbrir)
        self.menuArquivo.addAction(self.actionSalvar)
        self.menuArquivo.addSeparator()
        self.menuArquivo.addAction(self.actionSair)
        self.menuReduzir.addAction(self.actionReduzir_uma_vez)
        self.menuReduzir.addAction(self.actionTamanho_Original)
        self.menuEditar.addAction(self.actionDeletar)
        self.menuEditar.addAction(self.actionFinalizar_Demarca_o)
        self.menuEditar.addAction(self.actionDesfazer)
        self.menuEditar.addAction(self.actionAmpliar)
        self.menuEditar.addAction(self.menuReduzir.menuAction())
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())
        self.menubar.addAction(self.menuSobre.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionSair, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo", None))
        self.menuSobre.setTitle(_translate("MainWindow", "Sobre", None))
        self.menuEditar.setTitle(_translate("MainWindow", "Editar", None))
        self.menuReduzir.setTitle(_translate("MainWindow", "Reduzir...", None))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir...", None))
        self.actionAbrir.setToolTip(_translate("MainWindow", "Abrir Imagem", None))
        self.actionAbrir.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionSalvar.setText(_translate("MainWindow", "Salvar...", None))
        self.actionSalvar.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionDeletar.setText(_translate("MainWindow", "Deletar", None))
        self.actionDeletar.setToolTip(_translate("MainWindow", "Deletar Imagem", None))
        self.actionDeletar.setShortcut(_translate("MainWindow", "Ctrl+L", None))
        self.actionSair.setText(_translate("MainWindow", "Sair", None))
        self.actionSair.setShortcut(_translate("MainWindow", "Ctrl+D", None))
        self.actionFinalizar_Demarca_o.setText(_translate("MainWindow", "Finalizar Demarcação", None))
        self.actionFinalizar_Demarca_o.setShortcut(_translate("MainWindow", "Ctrl+B", None))
        self.actionDesfazer.setText(_translate("MainWindow", "Desfazer", None))
        self.actionDesfazer.setShortcut(_translate("MainWindow", "Ctrl+Z", None))
        self.actionAmpliar.setText(_translate("MainWindow", "Ampliar", None))
        self.actionAmpliar.setShortcut(_translate("MainWindow", "Ctrl+=", None))
        self.actionReduzir_uma_vez.setText(_translate("MainWindow", "Reduzir uma vez", None))
        self.actionReduzir_uma_vez.setShortcut(_translate("MainWindow", "Ctrl+-", None))
        self.actionTamanho_Original.setText(_translate("MainWindow", "Tamanho Original", None))
        self.actionTamanho_Original.setShortcut(_translate("MainWindow", "Ctrl+R", None))

