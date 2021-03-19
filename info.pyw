# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

'''

Este arquivo é parte do programa Buiatric Care Neurology

Buiatric Care Neurology é um software livre; você pode redistribuí-lo e/ou
modificá-lo dentro dos termos da Licença Pública Geral GNU como
publicada pela Fundação do Software Livre (FSF); na versão 3 da
Licença, ou (a seu critério) qualquer versão posterior.

Este programa é distribuído na esperança de que possa ser  útil,
mas SEM NENHUMA GARANTIA; sem uma garantia implícita de ADEQUAÇÃO
a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
Licença Pública Geral GNU para maiores detalhes.

Você deve ter recebido uma cópia da Licença Pública Geral GNU junto
com este programa, Se não, veja <http://www.gnu.org/licenses/>.

'''


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_info(object):
    def setupUi(self, suport):
        suport.setObjectName("suport")
        suport.resize(494, 559)
        suport.setMinimumSize(QtCore.QSize(494, 559))
        suport.setMaximumSize(QtCore.QSize(494, 559))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        suport.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        suport.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imagens/bcicone.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        suport.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(suport)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 30, 361, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("imagens/logo3.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 420, 171, 91))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("imagens/gaialogo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(30, 150, 431, 251))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 429, 249))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        suport.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(suport)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 494, 21))
        self.menubar.setObjectName("menubar")
        suport.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(suport)
        self.statusbar.setObjectName("statusbar")
        suport.setStatusBar(self.statusbar)

        self.retranslateUi(suport)
        QtCore.QMetaObject.connectSlotsByName(suport)

    def retranslateUi(self, suport):
        _translate = QtCore.QCoreApplication.translate
        suport.setWindowTitle(_translate("suport", "Software Informations - Buiatric Care"))
        self.textBrowser.setHtml(_translate("suport", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Century Gothic\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Version</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.4</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Developers</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Walberson Dias da Silva</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">João Ferreira de Santanna Filho</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Rinaldo Batista Viana</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Contributors</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Century Gothic,sans-serif\'; color:#555555;\">Anderson Silva Coelho<br />Andra Nunes Ferreira<br />André Augusto do Nascimento Mendonça<br />Andreia Tenório Autran de Almeida<br />Brenda Ventura Lopes Carvalho<br />Bruna Gonçalves Vidal de Lima<br />Carlos Conrado da Silva Junior<br />Joévelyn Jacqueline Santos da Silva<br />Leonardo Araújo da Costa<br />Luiz Paulo Silva da Cunha<br />Raquel de Alencar e Silva<br />Raysa Brenda Marques Maia<br />Verena Maciel da Costa<br />Walderson José Fernandes da Silva Jr</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Century Gothic,sans-serif\'; color:#555555;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Century Gothic,sans-serif\'; font-weight:600; color:#555555;\">Used Programming Language</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Century Gothic,sans-serif\'; color:#555555;\">Python</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Century Gothic,sans-serif\'; color:#555555;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Century Gothic,sans-serif\'; font-weight:600; color:#555555;\">Used Modules</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Century Gothic,sans-serif\'; color:#555555;\">Pyqt5</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Century Gothic,sans-serif\'; color:#555555;\">Os.path</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Century Gothic,sans-serif\'; color:#555555;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Century Gothic,sans-serif\'; color:#555555;\"><br /></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_info()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
