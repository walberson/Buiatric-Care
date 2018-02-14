# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'main_page2.ui'
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
'''
Autor: Walberson Dias - walberson.mv@gmail.com
adaptado de: Joao Santanna - joaosantanna@yahoo.com.br
versao: 1.0a
data: 31 de Janeiro de 2018
'''

from PyQt5 import QtCore, QtGui, QtWidgets
from avaliar import avaliar_sinais_clinicos
import os


#CRIAR A LISTA DE SINAIS CLÍNICOS
#APRESENTANDO 208 SINAIS CLÍNICOS
sinais_clinicos = [0]*209
lista_P_E = []

#CRIAR A LISTA DE ENFERMIDADES
enfermidades = ['Doença de Aujeszky', 'Babesiose cerebral', 'Botulismo',
'Cetose', 'Deficiência de cobre', 'Encefalopatia espongiforme bovina', 'Febre catarral maligna',
'Hipocalcemia', 'Intoxicação por Aspergillus clavatus', 'Intoxicação por chumbo',
'Intoxicação por Claviceps paspalis', 'Intoxicação por Equisetum sp.', 'Intoxicação por Ipomoea asarifolia',
'Intoxicação por Ipomoea carnea', 'Intoxicação por Marsdenia sp.', 'Intoxicação por organofosforados e carbamatos',
'Intoxicação por Phalaris spp.', 'Intoxicação por Polygala klotzschii', 'Intoxicação por Prosopis juriflora',
'Intoxicação por Ricinus communis', 'Intoxicação por Sida carpinifolia', 'Intoxicação por Solanum fastigiatum',
'Intoxicação por Sternocarpella maydis', 'Intoxicação por uréia', 'Leucose bovina', 'Listeriose',
'Meningoencefalite por BHV-5', 'Poliencefalomalácia', 'Raiva', 'Tétano']

'''
AQUI INICIAM-SE AS LINHAS DE CÓDIGO PARA A JANELA PRINCIPAL
'''

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(827, 629)
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
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imagens/bcicone.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.widget = QtWidgets.QWidget(MainWindow)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_logo = QtWidgets.QLabel(self.widget)
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("imagens/logo3.png"))
        self.label_logo.setScaledContents(False)
        self.label_logo.setObjectName("label_logo")
        self.verticalLayout.addWidget(self.label_logo)
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 110))
        self.textBrowser.setMouseTracking(False)
        self.textBrowser.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.textBrowser.setAcceptDrops(True)
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.scrollArea = QtWidgets.QScrollArea(self.widget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(226, 255, 255, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(226, 255, 255, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(226, 255, 255, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(226, 255, 255, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.scrollArea.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.scrollArea.setFont(font)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(-223, 0, 1215, 2965))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.checkbox_169 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_169.setObjectName("checkbox_169")
        self.gridLayout.addWidget(self.checkbox_169, 86, 3, 1, 1)
        self.checkbox_170 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_170.setObjectName("checkbox_170")
        self.gridLayout.addWidget(self.checkbox_170, 87, 3, 1, 1)
        self.checkbox_166 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_166.setObjectName("checkbox_166")
        self.gridLayout.addWidget(self.checkbox_166, 93, 2, 1, 1)
        self.checkbox_167 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_167.setObjectName("checkbox_167")
        self.gridLayout.addWidget(self.checkbox_167, 85, 3, 1, 1)
        self.checkbox_165 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_165.setObjectName("checkbox_165")
        self.gridLayout.addWidget(self.checkbox_165, 92, 2, 1, 1)
        self.checkbox_164 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_164.setObjectName("checkbox_164")
        self.gridLayout.addWidget(self.checkbox_164, 91, 2, 1, 1)
        self.checkbox_163 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_163.setObjectName("checkbox_163")
        self.gridLayout.addWidget(self.checkbox_163, 90, 2, 1, 1)
        self.checkbox_171 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_171.setObjectName("checkbox_171")
        self.gridLayout.addWidget(self.checkbox_171, 88, 3, 1, 1)
        self.checkbox_152 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_152.setObjectName("checkbox_152")
        self.gridLayout.addWidget(self.checkbox_152, 89, 3, 1, 1)
        self.checkbox_177 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_177.setObjectName("checkbox_177")
        self.gridLayout.addWidget(self.checkbox_177, 97, 1, 1, 1)
        self.checkbox_179 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_179.setObjectName("checkbox_179")
        self.gridLayout.addWidget(self.checkbox_179, 99, 1, 1, 1)
        self.checkbox_173 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_173.setObjectName("checkbox_173")
        self.gridLayout.addWidget(self.checkbox_173, 90, 3, 1, 1)
        self.checkbox_178 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_178.setObjectName("checkbox_178")
        self.gridLayout.addWidget(self.checkbox_178, 98, 1, 1, 1)
        self.checkbox_174 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_174.setObjectName("checkbox_174")
        self.gridLayout.addWidget(self.checkbox_174, 91, 3, 1, 1)
        self.checkbox_112 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_112.setObjectName("checkbox_112")
        self.gridLayout.addWidget(self.checkbox_112, 64, 2, 1, 1)
        self.checkbox_64 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_64.setObjectName("checkbox_64")
        self.gridLayout.addWidget(self.checkbox_64, 40, 1, 1, 1)
        self.checkbox_35 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_35.setFont(font)
        self.checkbox_35.setObjectName("checkbox_35")
        self.gridLayout.addWidget(self.checkbox_35, 25, 2, 1, 1)
        self.label_b = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_b.setText("")
        self.label_b.setPixmap(QtGui.QPixmap("imagens/b.png"))
        self.label_b.setObjectName("label_b")
        self.gridLayout.addWidget(self.label_b, 18, 1, 1, 1)
        self.checkbox_111 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_111.setObjectName("checkbox_111")
        self.gridLayout.addWidget(self.checkbox_111, 63, 2, 1, 1)
        self.checkbox_109 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_109.setObjectName("checkbox_109")
        self.gridLayout.addWidget(self.checkbox_109, 64, 1, 1, 1)
        self.checkbox_121 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_121.setObjectName("checkbox_121")
        self.gridLayout.addWidget(self.checkbox_121, 66, 3, 1, 1)
        self.checkbox_30 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_30.setFont(font)
        self.checkbox_30.setObjectName("checkbox_30")
        self.gridLayout.addWidget(self.checkbox_30, 26, 1, 1, 1)
        self.checkbox_33 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_33.setFont(font)
        self.checkbox_33.setObjectName("checkbox_33")
        self.gridLayout.addWidget(self.checkbox_33, 23, 2, 1, 1)
        self.checkbox_31 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_31.setFont(font)
        self.checkbox_31.setObjectName("checkbox_31")
        self.gridLayout.addWidget(self.checkbox_31, 21, 2, 1, 1)
        self.checkbox_34 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_34.setFont(font)
        self.checkbox_34.setObjectName("checkbox_34")
        self.gridLayout.addWidget(self.checkbox_34, 24, 2, 1, 1)
        self.checkbox_29 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_29.setFont(font)
        self.checkbox_29.setObjectName("checkbox_29")
        self.gridLayout.addWidget(self.checkbox_29, 25, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("imagens/e.png"))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 39, 1, 1, 1)
        self.label_c = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_c.sizePolicy().hasHeightForWidth())
        self.label_c.setSizePolicy(sizePolicy)
        self.label_c.setText("")
        self.label_c.setPixmap(QtGui.QPixmap("imagens/c.png"))
        self.label_c.setObjectName("label_c")
        self.gridLayout.addWidget(self.label_c, 20, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("imagens/o.png"))
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 79, 1, 1, 1)
        self.checkbox_32 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkbox_32.sizePolicy().hasHeightForWidth())
        self.checkbox_32.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_32.setFont(font)
        self.checkbox_32.setObjectName("checkbox_32")
        self.gridLayout.addWidget(self.checkbox_32, 22, 2, 1, 1)
        self.checkbox_65 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_65.setObjectName("checkbox_65")
        self.gridLayout.addWidget(self.checkbox_65, 41, 1, 1, 1)
        self.checkbox_82 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_82.setObjectName("checkbox_82")
        self.gridLayout.addWidget(self.checkbox_82, 49, 1, 1, 1)
        self.label_d = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_d.sizePolicy().hasHeightForWidth())
        self.label_d.setSizePolicy(sizePolicy)
        self.label_d.setText("")
        self.label_d.setPixmap(QtGui.QPixmap("imagens/d.png"))
        self.label_d.setObjectName("label_d")
        self.gridLayout.addWidget(self.label_d, 27, 1, 1, 1)
        self.checkbox_110 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_110.setObjectName("checkbox_110")
        self.gridLayout.addWidget(self.checkbox_110, 62, 2, 1, 1)
        self.label_a = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_a.setText("")
        self.label_a.setPixmap(QtGui.QPixmap("imagens/a.png"))
        self.label_a.setObjectName("label_a")
        self.gridLayout.addWidget(self.label_a, 0, 1, 1, 1)
        self.checkbox_41 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_41.setObjectName("checkbox_41")
        self.gridLayout.addWidget(self.checkbox_41, 28, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("imagens/f.png"))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 46, 1, 1, 1)
        self.checkbox_25 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_25.setFont(font)
        self.checkbox_25.setObjectName("checkbox_25")
        self.gridLayout.addWidget(self.checkbox_25, 21, 1, 1, 1)
        self.checkbox_37 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkbox_37.sizePolicy().hasHeightForWidth())
        self.checkbox_37.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_37.setFont(font)
        self.checkbox_37.setObjectName("checkbox_37")
        self.gridLayout.addWidget(self.checkbox_37, 21, 3, 1, 1)
        self.checkbox_26 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_26.setFont(font)
        self.checkbox_26.setObjectName("checkbox_26")
        self.gridLayout.addWidget(self.checkbox_26, 22, 1, 1, 1)
        self.checkbox_113 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_113.setObjectName("checkbox_113")
        self.gridLayout.addWidget(self.checkbox_113, 62, 3, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap("imagens/r.png"))
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 94, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("imagens/v.png"))
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 111, 1, 1, 1)
        self.checkbox_117 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_117.setObjectName("checkbox_117")
        self.gridLayout.addWidget(self.checkbox_117, 67, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("imagens/u.png"))
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 109, 1, 1, 1)
        self.checkbox_116 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_116.setObjectName("checkbox_116")
        self.gridLayout.addWidget(self.checkbox_116, 66, 1, 1, 1)
        self.checkbox_157 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_157.setObjectName("checkbox_157")
        self.gridLayout.addWidget(self.checkbox_157, 92, 1, 1, 1)
        self.checkbox_151 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_151.setObjectName("checkbox_151")
        self.gridLayout.addWidget(self.checkbox_151, 86, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap("imagens/t.png"))
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 103, 1, 1, 1)
        self.checkbox_158 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_158.setObjectName("checkbox_158")
        self.gridLayout.addWidget(self.checkbox_158, 93, 1, 1, 1)
        self.checkbox_153 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_153.setObjectName("checkbox_153")
        self.gridLayout.addWidget(self.checkbox_153, 88, 1, 1, 1)
        self.checkbox_132 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_132.setObjectName("checkbox_132")
        self.gridLayout.addWidget(self.checkbox_132, 74, 2, 1, 1)
        self.checkbox_156 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_156.setObjectName("checkbox_156")
        self.gridLayout.addWidget(self.checkbox_156, 91, 1, 1, 1)
        self.checkbox_150 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_150.setObjectName("checkbox_150")
        self.gridLayout.addWidget(self.checkbox_150, 85, 1, 1, 1)
        self.checkbox_134 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_134.setObjectName("checkbox_134")
        self.gridLayout.addWidget(self.checkbox_134, 76, 2, 1, 1)
        self.checkbox_131 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_131.setObjectName("checkbox_131")
        self.gridLayout.addWidget(self.checkbox_131, 73, 2, 1, 1)
        self.checkbox_135 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_135.setObjectName("checkbox_135")
        self.gridLayout.addWidget(self.checkbox_135, 75, 2, 1, 1)
        self.checkbox_136 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_136.setObjectName("checkbox_136")
        self.gridLayout.addWidget(self.checkbox_136, 71, 3, 1, 1)
        self.checkbox_129 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_129.setObjectName("checkbox_129")
        self.gridLayout.addWidget(self.checkbox_129, 71, 2, 1, 1)
        self.checkbox_133 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_133.setObjectName("checkbox_133")
        self.gridLayout.addWidget(self.checkbox_133, 70, 3, 1, 1)
        self.checkbox_96 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_96.setObjectName("checkbox_96")
        self.gridLayout.addWidget(self.checkbox_96, 58, 1, 1, 1)
        self.checkbox_119 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_119.setObjectName("checkbox_119")
        self.gridLayout.addWidget(self.checkbox_119, 67, 3, 1, 1)
        self.checkbox_36 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_36.setFont(font)
        self.checkbox_36.setObjectName("checkbox_36")
        self.gridLayout.addWidget(self.checkbox_36, 26, 2, 1, 1)
        self.checkbox_137 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_137.setObjectName("checkbox_137")
        self.gridLayout.addWidget(self.checkbox_137, 72, 3, 1, 1)
        self.checkbox_38 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_38.setFont(font)
        self.checkbox_38.setObjectName("checkbox_38")
        self.gridLayout.addWidget(self.checkbox_38, 22, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("imagens/n.png"))
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 77, 1, 1, 1)
        self.checkbox_130 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_130.setObjectName("checkbox_130")
        self.gridLayout.addWidget(self.checkbox_130, 72, 2, 1, 1)
        self.checkbox_128 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_128.setObjectName("checkbox_128")
        self.gridLayout.addWidget(self.checkbox_128, 70, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("imagens/p.png"))
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 84, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("imagens/l.png"))
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 65, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("imagens/h.png"))
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 55, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("imagens/G.png"))
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 53, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("imagens/m.png"))
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 69, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("imagens/i.png"))
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 61, 1, 1, 1)
        self.checkbox_95 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_95.setObjectName("checkbox_95")
        self.gridLayout.addWidget(self.checkbox_95, 57, 1, 1, 1)
        self.checkbox_97 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_97.setObjectName("checkbox_97")
        self.gridLayout.addWidget(self.checkbox_97, 59, 1, 1, 1)
        self.checkbox_99 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_99.setObjectName("checkbox_99")
        self.gridLayout.addWidget(self.checkbox_99, 56, 2, 1, 1)
        self.checkbox_91 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_91.setObjectName("checkbox_91")
        self.gridLayout.addWidget(self.checkbox_91, 50, 3, 1, 1)
        self.checkbox_88 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_88.setObjectName("checkbox_88")
        self.gridLayout.addWidget(self.checkbox_88, 51, 2, 1, 1)
        self.checkbox_40 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_40.setFont(font)
        self.checkbox_40.setObjectName("checkbox_40")
        self.gridLayout.addWidget(self.checkbox_40, 24, 3, 1, 1)
        self.checkbox_83 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_83.setObjectName("checkbox_83")
        self.gridLayout.addWidget(self.checkbox_83, 50, 1, 1, 1)
        self.checkbox_27 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkbox_27.sizePolicy().hasHeightForWidth())
        self.checkbox_27.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_27.setFont(font)
        self.checkbox_27.setObjectName("checkbox_27")
        self.gridLayout.addWidget(self.checkbox_27, 23, 1, 1, 1)
        self.checkbox_142 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_142.setObjectName("checkbox_142")
        self.gridLayout.addWidget(self.checkbox_142, 80, 1, 1, 1)
        self.checkbox_39 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_39.setFont(font)
        self.checkbox_39.setObjectName("checkbox_39")
        self.gridLayout.addWidget(self.checkbox_39, 23, 3, 1, 1)
        self.checkbox_28 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_28.setFont(font)
        self.checkbox_28.setObjectName("checkbox_28")
        self.gridLayout.addWidget(self.checkbox_28, 24, 1, 1, 1)
        self.checkbox_144 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_144.setObjectName("checkbox_144")
        self.gridLayout.addWidget(self.checkbox_144, 82, 1, 1, 1)
        self.checkbox_98 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_98.setObjectName("checkbox_98")
        self.gridLayout.addWidget(self.checkbox_98, 60, 1, 1, 1)
        self.checkbox_93 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_93.setObjectName("checkbox_93")
        self.gridLayout.addWidget(self.checkbox_93, 54, 1, 1, 1)
        self.checkbox_94 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_94.setObjectName("checkbox_94")
        self.gridLayout.addWidget(self.checkbox_94, 56, 1, 1, 1)
        self.checkbox_187 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_187.setObjectName("checkbox_187")
        self.gridLayout.addWidget(self.checkbox_187, 98, 3, 1, 1)
        self.checkbox_185 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_185.setObjectName("checkbox_185")
        self.gridLayout.addWidget(self.checkbox_185, 96, 3, 1, 1)
        self.checkbox_186 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_186.setObjectName("checkbox_186")
        self.gridLayout.addWidget(self.checkbox_186, 97, 3, 1, 1)
        self.checkbox_190 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_190.setObjectName("checkbox_190")
        self.gridLayout.addWidget(self.checkbox_190, 102, 1, 1, 1)
        self.checkbox_196 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_196.setObjectName("checkbox_196")
        self.gridLayout.addWidget(self.checkbox_196, 106, 1, 1, 1)
        self.checkbox_201 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_201.setObjectName("checkbox_201")
        self.gridLayout.addWidget(self.checkbox_201, 107, 2, 1, 1)
        self.checkbox_205 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_205.setObjectName("checkbox_205")
        self.gridLayout.addWidget(self.checkbox_205, 107, 3, 1, 1)
        self.checkbox_192 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_192.setObjectName("checkbox_192")
        self.gridLayout.addWidget(self.checkbox_192, 102, 2, 1, 1)
        self.checkbox_206 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_206.setObjectName("checkbox_206")
        self.gridLayout.addWidget(self.checkbox_206, 110, 1, 1, 1)
        self.checkbox_195 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_195.setObjectName("checkbox_195")
        self.gridLayout.addWidget(self.checkbox_195, 105, 1, 1, 1)
        self.checkbox_203 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_203.setObjectName("checkbox_203")
        self.gridLayout.addWidget(self.checkbox_203, 105, 3, 1, 1)
        self.checkbox_197 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_197.setObjectName("checkbox_197")
        self.gridLayout.addWidget(self.checkbox_197, 107, 1, 1, 1)
        self.checkbox_194 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_194.setObjectName("checkbox_194")
        self.gridLayout.addWidget(self.checkbox_194, 104, 1, 1, 1)
        self.checkbox_200 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_200.setObjectName("checkbox_200")
        self.gridLayout.addWidget(self.checkbox_200, 106, 2, 1, 1)
        self.checkbox_159 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_159.setObjectName("checkbox_159")
        self.gridLayout.addWidget(self.checkbox_159, 85, 2, 1, 1)
        self.checkbox_198 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_198.setObjectName("checkbox_198")
        self.gridLayout.addWidget(self.checkbox_198, 104, 2, 1, 1)
        self.checkbox_204 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_204.setObjectName("checkbox_204")
        self.gridLayout.addWidget(self.checkbox_204, 106, 3, 1, 1)
        self.checkbox_155 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_155.setObjectName("checkbox_155")
        self.gridLayout.addWidget(self.checkbox_155, 90, 1, 1, 1)
        self.checkbox_154 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_154.setObjectName("checkbox_154")
        self.gridLayout.addWidget(self.checkbox_154, 89, 1, 1, 1)
        self.checkbox_140 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_140.setObjectName("checkbox_140")
        self.gridLayout.addWidget(self.checkbox_140, 78, 1, 1, 1)
        self.checkbox_199 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_199.setObjectName("checkbox_199")
        self.gridLayout.addWidget(self.checkbox_199, 105, 2, 1, 1)
        self.checkbox_162 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_162.setObjectName("checkbox_162")
        self.gridLayout.addWidget(self.checkbox_162, 89, 2, 1, 1)
        self.checkbox_143 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_143.setObjectName("checkbox_143")
        self.gridLayout.addWidget(self.checkbox_143, 81, 1, 1, 1)
        self.checkbox_57 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_57.setObjectName("checkbox_57")
        self.gridLayout.addWidget(self.checkbox_57, 28, 3, 1, 1)
        self.checkbox_55 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_55.setObjectName("checkbox_55")
        self.gridLayout.addWidget(self.checkbox_55, 34, 2, 1, 1)
        self.checkbox_60 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_60.setObjectName("checkbox_60")
        self.gridLayout.addWidget(self.checkbox_60, 31, 3, 1, 1)
        self.checkbox_71 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_71.setObjectName("checkbox_71")
        self.gridLayout.addWidget(self.checkbox_71, 40, 2, 1, 1)
        self.checkbox_50 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_50.setObjectName("checkbox_50")
        self.gridLayout.addWidget(self.checkbox_50, 29, 2, 1, 1)
        self.checkbox_61 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_61.setObjectName("checkbox_61")
        self.gridLayout.addWidget(self.checkbox_61, 32, 3, 1, 1)
        self.checkbox_59 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_59.setObjectName("checkbox_59")
        self.gridLayout.addWidget(self.checkbox_59, 30, 3, 1, 1)
        self.checkbox_54 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_54.setObjectName("checkbox_54")
        self.gridLayout.addWidget(self.checkbox_54, 33, 2, 1, 1)
        self.checkbox_0 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkbox_0.sizePolicy().hasHeightForWidth())
        self.checkbox_0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_0.setFont(font)
        self.checkbox_0.setObjectName("checkbox_0")
        self.gridLayout.addWidget(self.checkbox_0, 1, 1, 1, 1)


        self.checkbox_22 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_22.setFont(font)
        self.checkbox_22.setObjectName("checkbox_22")
        self.gridLayout.addWidget(self.checkbox_22, 6, 1, 1, 1)
        self.checkbox_49 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkbox_49.sizePolicy().hasHeightForWidth())
        self.checkbox_49.setSizePolicy(sizePolicy)
        self.checkbox_49.setObjectName("checkbox_49")
        self.gridLayout.addWidget(self.checkbox_49, 28, 2, 1, 1)
        self.checkbox_181 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_181.setObjectName("checkbox_181")
        self.gridLayout.addWidget(self.checkbox_181, 97, 2, 1, 1)
        self.checkbox_176 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_176.setObjectName("checkbox_176")
        self.gridLayout.addWidget(self.checkbox_176, 96, 1, 1, 1)
        self.checkbox_182 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_182.setObjectName("checkbox_182")
        self.gridLayout.addWidget(self.checkbox_182, 98, 2, 1, 1)
        self.checkbox_202 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_202.setObjectName("checkbox_202")
        self.gridLayout.addWidget(self.checkbox_202, 104, 3, 1, 1)
        self.checkbox_184 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_184.setObjectName("checkbox_184")
        self.gridLayout.addWidget(self.checkbox_184, 95, 3, 1, 1)
        self.checkbox_42 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_42.setObjectName("checkbox_42")
        self.gridLayout.addWidget(self.checkbox_42, 29, 1, 1, 1)
        self.checkbox_5 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkbox_5.sizePolicy().hasHeightForWidth())
        self.checkbox_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_5.setFont(font)
        self.checkbox_5.setObjectName("checkbox_5")
        self.gridLayout.addWidget(self.checkbox_5, 14, 1, 1, 1)
        self.checkbox_6 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkbox_6.sizePolicy().hasHeightForWidth())
        self.checkbox_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_6.setFont(font)
        self.checkbox_6.setObjectName("checkbox_6")
        self.gridLayout.addWidget(self.checkbox_6, 15, 1, 1, 1)
        self.checkbox_4 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_4.setFont(font)
        self.checkbox_4.setObjectName("checkbox_4")
        self.gridLayout.addWidget(self.checkbox_4, 13, 1, 1, 1)



        self.checkbox_24 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_24.setFont(font)
        self.checkbox_24.setObjectName("checkbox_24")
        self.gridLayout.addWidget(self.checkbox_24, 19, 2, 1, 1)
        self.checkbox_17 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_17.setFont(font)
        self.checkbox_17.setObjectName("checkbox_17")
        self.gridLayout.addWidget(self.checkbox_17, 2, 3, 1, 1)
        self.checkbox_47 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_47.setObjectName("checkbox_47")
        self.gridLayout.addWidget(self.checkbox_47, 34, 1, 1, 1)
        self.checkbox_9 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_9.setFont(font)
        self.checkbox_9.setObjectName("checkbox_9")
        self.gridLayout.addWidget(self.checkbox_9, 2, 2, 1, 1)
        self.checkbox_18 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_18.setFont(font)
        self.checkbox_18.setObjectName("checkbox_18")
        self.gridLayout.addWidget(self.checkbox_18, 4, 3, 1, 1)
        self.checkbox_44 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_44.setObjectName("checkbox_44")
        self.gridLayout.addWidget(self.checkbox_44, 31, 1, 1, 1)
        self.checkbox_13 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_13.setFont(font)
        self.checkbox_13.setObjectName("checkbox_13")
        self.gridLayout.addWidget(self.checkbox_13, 14, 2, 1, 1)
        self.checkbox_43 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_43.setObjectName("checkbox_43")
        self.gridLayout.addWidget(self.checkbox_43, 30, 1, 1, 1)
        self.checkbox_19 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_19.setFont(font)
        self.checkbox_19.setObjectName("checkbox_19")
        self.gridLayout.addWidget(self.checkbox_19, 6, 3, 1, 1)
        self.checkbox_16 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_16.setFont(font)
        self.checkbox_16.setObjectName("checkbox_16")
        self.gridLayout.addWidget(self.checkbox_16, 1, 3, 1, 1)
        self.checkbox_10 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_10.setFont(font)
        self.checkbox_10.setObjectName("checkbox_10")
        self.gridLayout.addWidget(self.checkbox_10, 4, 2, 1, 1)
        self.checkbox_20 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_20.setObjectName("checkbox_20")
        self.gridLayout.addWidget(self.checkbox_20, 13, 3, 1, 1)
        self.checkbox_14 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_14.setFont(font)
        self.checkbox_14.setObjectName("checkbox_14")
        self.gridLayout.addWidget(self.checkbox_14, 15, 2, 1, 1)
        self.checkbox_48 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_48.setObjectName("checkbox_48")
        self.gridLayout.addWidget(self.checkbox_48, 35, 1, 1, 1)
        self.checkbox_11 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_11.setFont(font)
        self.checkbox_11.setObjectName("checkbox_11")
        self.gridLayout.addWidget(self.checkbox_11, 6, 2, 1, 1)
        self.checkbox_45 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_45.setObjectName("checkbox_45")
        self.gridLayout.addWidget(self.checkbox_45, 32, 1, 1, 1)
        self.checkbox_51 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_51.setObjectName("checkbox_51")
        self.gridLayout.addWidget(self.checkbox_51, 30, 2, 1, 1)
        self.checkbox_12 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_12.setFont(font)
        self.checkbox_12.setObjectName("checkbox_12")
        self.gridLayout.addWidget(self.checkbox_12, 13, 2, 1, 1)
        self.checkbox_15 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_15.setFont(font)
        self.checkbox_15.setObjectName("checkbox_15")
        self.gridLayout.addWidget(self.checkbox_15, 16, 2, 1, 1)
        self.checkbox_62 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_62.setObjectName("checkbox_62")
        self.gridLayout.addWidget(self.checkbox_62, 33, 3, 1, 1)
        self.checkbox_46 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_46.setObjectName("checkbox_46")
        self.gridLayout.addWidget(self.checkbox_46, 33, 1, 1, 1)
        self.checkbox_53 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_53.setObjectName("checkbox_53")
        self.gridLayout.addWidget(self.checkbox_53, 32, 2, 1, 1)
        self.checkbox_58 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_58.setObjectName("checkbox_58")
        self.gridLayout.addWidget(self.checkbox_58, 29, 3, 1, 1)
        self.checkbox_63 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_63.setObjectName("checkbox_63")
        self.gridLayout.addWidget(self.checkbox_63, 34, 3, 1, 1)
        self.checkbox_56 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_56.setObjectName("checkbox_56")
        self.gridLayout.addWidget(self.checkbox_56, 35, 2, 1, 1)
        self.checkbox_7 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkbox_7.sizePolicy().hasHeightForWidth())
        self.checkbox_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_7.setFont(font)
        self.checkbox_7.setObjectName("checkbox_7")
        self.gridLayout.addWidget(self.checkbox_7, 16, 1, 1, 1)
        self.checkbox_52 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_52.setObjectName("checkbox_52")
        self.gridLayout.addWidget(self.checkbox_52, 31, 2, 1, 1)
        self.checkbox_80 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_80.setObjectName("checkbox_80")
        self.gridLayout.addWidget(self.checkbox_80, 44, 3, 1, 1)
        self.checkbox_73 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_73.setObjectName("checkbox_73")
        self.gridLayout.addWidget(self.checkbox_73, 42, 2, 1, 1)
        self.checkbox_66 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_66.setObjectName("checkbox_66")
        self.gridLayout.addWidget(self.checkbox_66, 43, 3, 1, 1)
        self.checkbox_75 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_75.setObjectName("checkbox_75")
        self.gridLayout.addWidget(self.checkbox_75, 44, 2, 1, 1)
        self.checkbox_79 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_79.setObjectName("checkbox_79")
        self.gridLayout.addWidget(self.checkbox_79, 42, 3, 1, 1)
        self.checkbox_74 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_74.setObjectName("checkbox_74")
        self.gridLayout.addWidget(self.checkbox_74, 43, 2, 1, 1)
        self.checkbox_76 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_76.setObjectName("checkbox_76")
        self.gridLayout.addWidget(self.checkbox_76, 45, 2, 1, 1)
        self.checkbox_72 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_72.setObjectName("checkbox_72")
        self.gridLayout.addWidget(self.checkbox_72, 41, 2, 1, 1)
        self.checkbox_77 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_77.setObjectName("checkbox_77")
        self.gridLayout.addWidget(self.checkbox_77, 40, 3, 1, 1)
        self.checkbox_78 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_78.setObjectName("checkbox_78")
        self.gridLayout.addWidget(self.checkbox_78, 41, 3, 1, 1)
        self.checkbox_81 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_81.setObjectName("checkbox_81")
        self.gridLayout.addWidget(self.checkbox_81, 51, 3, 1, 1)
        self.checkbox_100 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_100.setObjectName("checkbox_100")
        self.gridLayout.addWidget(self.checkbox_100, 57, 2, 1, 1)
        self.checkbox_102 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_102.setObjectName("checkbox_102")
        self.gridLayout.addWidget(self.checkbox_102, 59, 2, 1, 1)
        self.checkbox_92 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_92.setObjectName("checkbox_92")
        self.gridLayout.addWidget(self.checkbox_92, 47, 1, 1, 1)
        self.checkbox_101 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_101.setObjectName("checkbox_101")
        self.gridLayout.addWidget(self.checkbox_101, 58, 2, 1, 1)
        self.checkbox_103 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_103.setObjectName("checkbox_103")
        self.gridLayout.addWidget(self.checkbox_103, 60, 2, 1, 1)
        self.checkbox_106 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_106.setObjectName("checkbox_106")
        self.gridLayout.addWidget(self.checkbox_106, 58, 3, 1, 1)
        self.checkbox_115 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_115.setObjectName("checkbox_115")
        self.gridLayout.addWidget(self.checkbox_115, 62, 1, 1, 1)
        self.checkbox_107 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_107.setObjectName("checkbox_107")
        self.gridLayout.addWidget(self.checkbox_107, 64, 3, 1, 1)
        self.checkbox_104 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_104.setObjectName("checkbox_104")
        self.gridLayout.addWidget(self.checkbox_104, 56, 3, 1, 1)
        self.checkbox_105 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_105.setObjectName("checkbox_105")
        self.gridLayout.addWidget(self.checkbox_105, 57, 3, 1, 1)
        self.checkbox_118 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_118.setObjectName("checkbox_118")
        self.gridLayout.addWidget(self.checkbox_118, 67, 2, 1, 1)
        self.checkbox_120 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_120.setObjectName("checkbox_120")
        self.gridLayout.addWidget(self.checkbox_120, 66, 2, 1, 1)
        self.checkbox_114 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_114.setObjectName("checkbox_114")
        self.gridLayout.addWidget(self.checkbox_114, 63, 1, 1, 1)
        self.checkbox_108 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_108.setObjectName("checkbox_108")
        self.gridLayout.addWidget(self.checkbox_108, 63, 3, 1, 1)
        self.checkbox_69 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_69.setObjectName("checkbox_69")
        self.gridLayout.addWidget(self.checkbox_69, 44, 1, 1, 1)
        self.checkbox_1 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkbox_1.sizePolicy().hasHeightForWidth())
        self.checkbox_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_1.setFont(font)
        self.checkbox_1.setObjectName("checkbox_1")
        self.gridLayout.addWidget(self.checkbox_1, 2, 1, 1, 1)


        self.checkbox_67 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_67.setObjectName("checkbox_67")
        self.gridLayout.addWidget(self.checkbox_67, 42, 1, 1, 1)
        self.checkbox_8 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkbox_8.sizePolicy().hasHeightForWidth())
        self.checkbox_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_8.setFont(font)
        self.checkbox_8.setObjectName("checkbox_8")
        self.gridLayout.addWidget(self.checkbox_8, 1, 2, 1, 1)
        self.checkbox_21 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_21.setFont(font)
        self.checkbox_21.setObjectName("checkbox_21")
        self.gridLayout.addWidget(self.checkbox_21, 14, 3, 1, 1)
        self.checkbox_70 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_70.setObjectName("checkbox_70")
        self.gridLayout.addWidget(self.checkbox_70, 45, 1, 1, 1)
        self.checkbox_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_2.setFont(font)
        self.checkbox_2.setObjectName("checkbox_2")
        self.gridLayout.addWidget(self.checkbox_2, 4, 1, 1, 1)
        self.checkbox_68 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_68.setObjectName("checkbox_68")
        self.gridLayout.addWidget(self.checkbox_68, 43, 1, 1, 1)
        self.checkbox_23 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.checkbox_23.setFont(font)
        self.checkbox_23.setObjectName("checkbox_23")
        self.gridLayout.addWidget(self.checkbox_23, 19, 1, 1, 1)
        self.checkbox_175 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_175.setObjectName("checkbox_175")
        self.gridLayout.addWidget(self.checkbox_175, 96, 2, 1, 1)
        self.checkbox_188 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_188.setObjectName("checkbox_188")
        self.gridLayout.addWidget(self.checkbox_188, 99, 2, 1, 1)
        self.checkbox_183 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_183.setObjectName("checkbox_183")
        self.gridLayout.addWidget(self.checkbox_183, 95, 1, 1, 1)
        self.checkbox_193 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_193.setObjectName("checkbox_193")
        self.gridLayout.addWidget(self.checkbox_193, 101, 2, 1, 1)
        self.checkbox_189 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_189.setObjectName("checkbox_189")
        self.gridLayout.addWidget(self.checkbox_189, 101, 3, 1, 1)
        self.checkbox_191 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_191.setObjectName("checkbox_191")
        self.gridLayout.addWidget(self.checkbox_191, 101, 1, 1, 1)
        self.checkbox_123 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_123.setObjectName("checkbox_123")
        self.gridLayout.addWidget(self.checkbox_123, 71, 1, 1, 1)
        self.checkbox_122 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_122.setObjectName("checkbox_122")
        self.gridLayout.addWidget(self.checkbox_122, 70, 1, 1, 1)
        self.checkbox_139 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_139.setObjectName("checkbox_139")
        self.gridLayout.addWidget(self.checkbox_139, 76, 1, 1, 1)
        self.checkbox_124 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_124.setObjectName("checkbox_124")
        self.gridLayout.addWidget(self.checkbox_124, 72, 1, 1, 1)
        self.checkbox_126 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_126.setObjectName("checkbox_126")
        self.gridLayout.addWidget(self.checkbox_126, 73, 1, 1, 1)
        self.checkbox_125 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_125.setObjectName("checkbox_125")
        self.gridLayout.addWidget(self.checkbox_125, 73, 3, 1, 1)
        self.checkbox_138 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_138.setObjectName("checkbox_138")
        self.gridLayout.addWidget(self.checkbox_138, 74, 1, 1, 1)
        self.checkbox_127 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_127.setObjectName("checkbox_127")
        self.gridLayout.addWidget(self.checkbox_127, 75, 1, 1, 1)
        self.checkbox_146 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_146.setObjectName("checkbox_146")
        self.gridLayout.addWidget(self.checkbox_146, 81, 2, 1, 1)
        self.checkbox_147 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_147.setObjectName("checkbox_147")
        self.gridLayout.addWidget(self.checkbox_147, 80, 2, 1, 1)
        self.checkbox_145 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_145.setObjectName("checkbox_145")
        self.gridLayout.addWidget(self.checkbox_145, 81, 3, 1, 1)
        self.checkbox_149 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_149.setObjectName("checkbox_149")
        self.gridLayout.addWidget(self.checkbox_149, 80, 3, 1, 1)
        self.checkbox_160 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_160.setObjectName("checkbox_160")
        self.gridLayout.addWidget(self.checkbox_160, 86, 2, 1, 1)
        self.checkbox_148 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_148.setObjectName("checkbox_148")
        self.gridLayout.addWidget(self.checkbox_148, 82, 2, 1, 1)
        self.checkbox_172 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_172.setObjectName("checkbox_172")
        self.gridLayout.addWidget(self.checkbox_172, 87, 1, 1, 1)
        self.checkbox_161 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_161.setObjectName("checkbox_161")
        self.gridLayout.addWidget(self.checkbox_161, 87, 2, 1, 1)
        self.checkbox_168 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_168.setObjectName("checkbox_168")
        self.gridLayout.addWidget(self.checkbox_168, 88, 2, 1, 1)
        self.checkbox_180 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_180.setObjectName("checkbox_180")
        self.gridLayout.addWidget(self.checkbox_180, 95, 2, 1, 1)
        self.checkbox_85 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_85.setObjectName("checkbox_85")
        self.gridLayout.addWidget(self.checkbox_85, 51, 1, 1, 1)
        self.checkbox_84 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_84.setObjectName("checkbox_84")
        self.gridLayout.addWidget(self.checkbox_84, 47, 3, 1, 1)
        self.checkbox_86 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_86.setObjectName("checkbox_86")
        self.gridLayout.addWidget(self.checkbox_86, 47, 2, 1, 1)
        self.checkbox_89 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_89.setObjectName("checkbox_89")
        self.gridLayout.addWidget(self.checkbox_89, 49, 2, 1, 1)
        self.checkbox_90 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_90.setObjectName("checkbox_90")
        self.gridLayout.addWidget(self.checkbox_90, 50, 2, 1, 1)
        self.checkbox_87 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_87.setObjectName("checkbox_87")
        self.gridLayout.addWidget(self.checkbox_87, 49, 3, 1, 1)
        self.checkbox_207 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_207.setObjectName("checkbox_207")
        self.gridLayout.addWidget(self.checkbox_207, 112, 3, 1, 1)
        self.checkbox_208 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_208.setObjectName("checkbox_208")
        self.gridLayout.addWidget(self.checkbox_208, 112, 1, 1, 1)
        self.checkbox_141 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkbox_141.setObjectName("checkbox_141")
        self.gridLayout.addWidget(self.checkbox_141, 78, 3, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.widget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 827, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuAjuda = QtWidgets.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.menuAjuda.setFont(font)
        self.menuAjuda.setObjectName("menuAjuda")
        MainWindow.setMenuBar(self.menuBar)
        self.actionAvisos_legais = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.actionAvisos_legais.setFont(font)
        self.actionAvisos_legais.setObjectName("actionAvisos_legais")
        self.actionSuporte = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.actionSuporte.setFont(font)
        self.actionSuporte.setObjectName("actionSuporte")
        self.actionInforma_es_do_programa = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.actionInforma_es_do_programa.setFont(font)
        self.actionInforma_es_do_programa.setObjectName("actionInforma_es_do_programa")
        self.menuAjuda.addAction(self.actionInforma_es_do_programa)
        self.menuAjuda.addAction(self.actionAvisos_legais)
        self.menuAjuda.addAction(self.actionSuporte)
        self.menuBar.addAction(self.menuAjuda.menuAction())


        '''
        ESTÃO LISTADOS ABAIXO OS COMANDOS DOS CHECKBOXES PARA CHAMAR AS FUNÇOES
        QUE IRÃO MODIFICAR O VALOR DOS SINAIS CLÍNICOS ( 1=SIM 0=NÃO)
        '''

        self.checkbox_0.stateChanged.connect(self.clickbox_0)
        self.checkbox_1.stateChanged.connect(self.clickbox_1)
        self.checkbox_2.stateChanged.connect(self.clickbox_2)

        self.checkbox_4.stateChanged.connect(self.clickbox_4)
        self.checkbox_5.stateChanged.connect(self.clickbox_5)
        self.checkbox_6.stateChanged.connect(self.clickbox_6)
        self.checkbox_7.stateChanged.connect(self.clickbox_7)
        self.checkbox_8.stateChanged.connect(self.clickbox_8)
        self.checkbox_9.stateChanged.connect(self.clickbox_9)
        self.checkbox_10.stateChanged.connect(self.clickbox_10)
        self.checkbox_11.stateChanged.connect(self.clickbox_11)
        self.checkbox_12.stateChanged.connect(self.clickbox_12)
        self.checkbox_13.stateChanged.connect(self.clickbox_13)
        self.checkbox_14.stateChanged.connect(self.clickbox_14)
        self.checkbox_15.stateChanged.connect(self.clickbox_15)
        self.checkbox_16.stateChanged.connect(self.clickbox_16)
        self.checkbox_17.stateChanged.connect(self.clickbox_17)
        self.checkbox_18.stateChanged.connect(self.clickbox_18)
        self.checkbox_19.stateChanged.connect(self.clickbox_19)
        self.checkbox_20.stateChanged.connect(self.clickbox_20)
        self.checkbox_21.stateChanged.connect(self.clickbox_21)
        self.checkbox_22.stateChanged.connect(self.clickbox_22)
        self.checkbox_23.stateChanged.connect(self.clickbox_23)
        self.checkbox_24.stateChanged.connect(self.clickbox_24)
        self.checkbox_25.stateChanged.connect(self.clickbox_25)
        self.checkbox_26.stateChanged.connect(self.clickbox_26)
        self.checkbox_27.stateChanged.connect(self.clickbox_27)
        self.checkbox_28.stateChanged.connect(self.clickbox_28)
        self.checkbox_29.stateChanged.connect(self.clickbox_29)
        self.checkbox_30.stateChanged.connect(self.clickbox_30)
        self.checkbox_31.stateChanged.connect(self.clickbox_31)
        self.checkbox_32.stateChanged.connect(self.clickbox_32)
        self.checkbox_33.stateChanged.connect(self.clickbox_33)
        self.checkbox_34.stateChanged.connect(self.clickbox_34)
        self.checkbox_35.stateChanged.connect(self.clickbox_35)
        self.checkbox_36.stateChanged.connect(self.clickbox_36)
        self.checkbox_37.stateChanged.connect(self.clickbox_37)
        self.checkbox_38.stateChanged.connect(self.clickbox_38)
        self.checkbox_39.stateChanged.connect(self.clickbox_39)
        self.checkbox_40.stateChanged.connect(self.clickbox_40)
        self.checkbox_41.stateChanged.connect(self.clickbox_41)
        self.checkbox_42.stateChanged.connect(self.clickbox_42)
        self.checkbox_43.stateChanged.connect(self.clickbox_43)
        self.checkbox_44.stateChanged.connect(self.clickbox_44)
        self.checkbox_45.stateChanged.connect(self.clickbox_45)
        self.checkbox_46.stateChanged.connect(self.clickbox_46)
        self.checkbox_47.stateChanged.connect(self.clickbox_47)
        self.checkbox_48.stateChanged.connect(self.clickbox_48)
        self.checkbox_49.stateChanged.connect(self.clickbox_49)
        self.checkbox_50.stateChanged.connect(self.clickbox_50)
        self.checkbox_51.stateChanged.connect(self.clickbox_51)
        self.checkbox_52.stateChanged.connect(self.clickbox_52)
        self.checkbox_53.stateChanged.connect(self.clickbox_53)
        self.checkbox_54.stateChanged.connect(self.clickbox_54)
        self.checkbox_55.stateChanged.connect(self.clickbox_55)
        self.checkbox_56.stateChanged.connect(self.clickbox_56)
        self.checkbox_57.stateChanged.connect(self.clickbox_57)
        self.checkbox_58.stateChanged.connect(self.clickbox_58)
        self.checkbox_59.stateChanged.connect(self.clickbox_59)
        self.checkbox_60.stateChanged.connect(self.clickbox_60)
        self.checkbox_61.stateChanged.connect(self.clickbox_61)
        self.checkbox_62.stateChanged.connect(self.clickbox_62)
        self.checkbox_63.stateChanged.connect(self.clickbox_63)
        self.checkbox_64.stateChanged.connect(self.clickbox_64)
        self.checkbox_65.stateChanged.connect(self.clickbox_65)
        self.checkbox_66.stateChanged.connect(self.clickbox_66)
        self.checkbox_67.stateChanged.connect(self.clickbox_67)
        self.checkbox_68.stateChanged.connect(self.clickbox_68)
        self.checkbox_69.stateChanged.connect(self.clickbox_69)
        self.checkbox_70.stateChanged.connect(self.clickbox_70)
        self.checkbox_71.stateChanged.connect(self.clickbox_71)
        self.checkbox_72.stateChanged.connect(self.clickbox_72)
        self.checkbox_73.stateChanged.connect(self.clickbox_73)
        self.checkbox_74.stateChanged.connect(self.clickbox_74)
        self.checkbox_75.stateChanged.connect(self.clickbox_75)
        self.checkbox_76.stateChanged.connect(self.clickbox_76)
        self.checkbox_77.stateChanged.connect(self.clickbox_77)
        self.checkbox_78.stateChanged.connect(self.clickbox_78)
        self.checkbox_79.stateChanged.connect(self.clickbox_79)
        self.checkbox_80.stateChanged.connect(self.clickbox_80)
        self.checkbox_81.stateChanged.connect(self.clickbox_81)
        self.checkbox_82.stateChanged.connect(self.clickbox_82)
        self.checkbox_83.stateChanged.connect(self.clickbox_83)
        self.checkbox_84.stateChanged.connect(self.clickbox_84)
        self.checkbox_85.stateChanged.connect(self.clickbox_85)
        self.checkbox_86.stateChanged.connect(self.clickbox_86)
        self.checkbox_87.stateChanged.connect(self.clickbox_87)
        self.checkbox_88.stateChanged.connect(self.clickbox_88)
        self.checkbox_89.stateChanged.connect(self.clickbox_89)
        self.checkbox_90.stateChanged.connect(self.clickbox_90)
        self.checkbox_91.stateChanged.connect(self.clickbox_91)
        self.checkbox_92.stateChanged.connect(self.clickbox_92)
        self.checkbox_93.stateChanged.connect(self.clickbox_93)
        self.checkbox_94.stateChanged.connect(self.clickbox_94)
        self.checkbox_95.stateChanged.connect(self.clickbox_95)
        self.checkbox_96.stateChanged.connect(self.clickbox_96)
        self.checkbox_97.stateChanged.connect(self.clickbox_97)
        self.checkbox_98.stateChanged.connect(self.clickbox_98)
        self.checkbox_99.stateChanged.connect(self.clickbox_99)
        self.checkbox_100.stateChanged.connect(self.clickbox_100)
        self.checkbox_101.stateChanged.connect(self.clickbox_101)
        self.checkbox_102.stateChanged.connect(self.clickbox_102)
        self.checkbox_103.stateChanged.connect(self.clickbox_103)
        self.checkbox_104.stateChanged.connect(self.clickbox_104)
        self.checkbox_105.stateChanged.connect(self.clickbox_105)
        self.checkbox_106.stateChanged.connect(self.clickbox_106)
        self.checkbox_107.stateChanged.connect(self.clickbox_107)
        self.checkbox_108.stateChanged.connect(self.clickbox_108)
        self.checkbox_109.stateChanged.connect(self.clickbox_109)
        self.checkbox_110.stateChanged.connect(self.clickbox_110)
        self.checkbox_111.stateChanged.connect(self.clickbox_111)
        self.checkbox_112.stateChanged.connect(self.clickbox_112)
        self.checkbox_113.stateChanged.connect(self.clickbox_113)
        self.checkbox_114.stateChanged.connect(self.clickbox_114)
        self.checkbox_115.stateChanged.connect(self.clickbox_115)
        self.checkbox_116.stateChanged.connect(self.clickbox_116)
        self.checkbox_117.stateChanged.connect(self.clickbox_117)
        self.checkbox_118.stateChanged.connect(self.clickbox_118)
        self.checkbox_119.stateChanged.connect(self.clickbox_119)
        self.checkbox_120.stateChanged.connect(self.clickbox_120)
        self.checkbox_121.stateChanged.connect(self.clickbox_121)
        self.checkbox_122.stateChanged.connect(self.clickbox_122)
        self.checkbox_123.stateChanged.connect(self.clickbox_123)
        self.checkbox_124.stateChanged.connect(self.clickbox_124)
        self.checkbox_125.stateChanged.connect(self.clickbox_125)
        self.checkbox_126.stateChanged.connect(self.clickbox_126)
        self.checkbox_127.stateChanged.connect(self.clickbox_127)
        self.checkbox_128.stateChanged.connect(self.clickbox_128)
        self.checkbox_129.stateChanged.connect(self.clickbox_129)
        self.checkbox_130.stateChanged.connect(self.clickbox_130)
        self.checkbox_131.stateChanged.connect(self.clickbox_131)
        self.checkbox_132.stateChanged.connect(self.clickbox_132)
        self.checkbox_133.stateChanged.connect(self.clickbox_133)
        self.checkbox_134.stateChanged.connect(self.clickbox_134)
        self.checkbox_135.stateChanged.connect(self.clickbox_135)
        self.checkbox_136.stateChanged.connect(self.clickbox_136)
        self.checkbox_137.stateChanged.connect(self.clickbox_137)
        self.checkbox_138.stateChanged.connect(self.clickbox_138)
        self.checkbox_139.stateChanged.connect(self.clickbox_139)
        self.checkbox_140.stateChanged.connect(self.clickbox_140)
        self.checkbox_141.stateChanged.connect(self.clickbox_141)
        self.checkbox_142.stateChanged.connect(self.clickbox_142)
        self.checkbox_143.stateChanged.connect(self.clickbox_143)
        self.checkbox_144.stateChanged.connect(self.clickbox_144)
        self.checkbox_145.stateChanged.connect(self.clickbox_145)
        self.checkbox_146.stateChanged.connect(self.clickbox_146)
        self.checkbox_147.stateChanged.connect(self.clickbox_147)
        self.checkbox_148.stateChanged.connect(self.clickbox_148)
        self.checkbox_149.stateChanged.connect(self.clickbox_149)
        self.checkbox_150.stateChanged.connect(self.clickbox_150)
        self.checkbox_151.stateChanged.connect(self.clickbox_151)
        self.checkbox_152.stateChanged.connect(self.clickbox_152)
        self.checkbox_153.stateChanged.connect(self.clickbox_153)
        self.checkbox_154.stateChanged.connect(self.clickbox_154)
        self.checkbox_155.stateChanged.connect(self.clickbox_155)
        self.checkbox_156.stateChanged.connect(self.clickbox_156)
        self.checkbox_157.stateChanged.connect(self.clickbox_157)
        self.checkbox_158.stateChanged.connect(self.clickbox_158)
        self.checkbox_159.stateChanged.connect(self.clickbox_159)
        self.checkbox_160.stateChanged.connect(self.clickbox_160)
        self.checkbox_161.stateChanged.connect(self.clickbox_161)
        self.checkbox_162.stateChanged.connect(self.clickbox_162)
        self.checkbox_163.stateChanged.connect(self.clickbox_163)
        self.checkbox_164.stateChanged.connect(self.clickbox_164)
        self.checkbox_165.stateChanged.connect(self.clickbox_165)
        self.checkbox_166.stateChanged.connect(self.clickbox_166)
        self.checkbox_167.stateChanged.connect(self.clickbox_167)
        self.checkbox_168.stateChanged.connect(self.clickbox_168)
        self.checkbox_169.stateChanged.connect(self.clickbox_169)
        self.checkbox_170.stateChanged.connect(self.clickbox_170)
        self.checkbox_171.stateChanged.connect(self.clickbox_171)
        self.checkbox_172.stateChanged.connect(self.clickbox_172)
        self.checkbox_173.stateChanged.connect(self.clickbox_173)
        self.checkbox_174.stateChanged.connect(self.clickbox_174)
        self.checkbox_175.stateChanged.connect(self.clickbox_175)
        self.checkbox_176.stateChanged.connect(self.clickbox_176)
        self.checkbox_177.stateChanged.connect(self.clickbox_177)
        self.checkbox_178.stateChanged.connect(self.clickbox_178)
        self.checkbox_179.stateChanged.connect(self.clickbox_179)
        self.checkbox_180.stateChanged.connect(self.clickbox_180)
        self.checkbox_181.stateChanged.connect(self.clickbox_181)
        self.checkbox_182.stateChanged.connect(self.clickbox_182)
        self.checkbox_183.stateChanged.connect(self.clickbox_183)
        self.checkbox_184.stateChanged.connect(self.clickbox_184)
        self.checkbox_185.stateChanged.connect(self.clickbox_185)
        self.checkbox_186.stateChanged.connect(self.clickbox_186)
        self.checkbox_187.stateChanged.connect(self.clickbox_187)
        self.checkbox_188.stateChanged.connect(self.clickbox_188)
        self.checkbox_189.stateChanged.connect(self.clickbox_189)
        self.checkbox_190.stateChanged.connect(self.clickbox_190)
        self.checkbox_191.stateChanged.connect(self.clickbox_191)
        self.checkbox_192.stateChanged.connect(self.clickbox_192)
        self.checkbox_193.stateChanged.connect(self.clickbox_193)
        self.checkbox_194.stateChanged.connect(self.clickbox_194)
        self.checkbox_195.stateChanged.connect(self.clickbox_195)
        self.checkbox_196.stateChanged.connect(self.clickbox_196)
        self.checkbox_197.stateChanged.connect(self.clickbox_197)
        self.checkbox_198.stateChanged.connect(self.clickbox_198)
        self.checkbox_199.stateChanged.connect(self.clickbox_199)
        self.checkbox_200.stateChanged.connect(self.clickbox_200)
        self.checkbox_201.stateChanged.connect(self.clickbox_201)
        self.checkbox_202.stateChanged.connect(self.clickbox_202)
        self.checkbox_203.stateChanged.connect(self.clickbox_203)
        self.checkbox_204.stateChanged.connect(self.clickbox_204)
        self.checkbox_205.stateChanged.connect(self.clickbox_205)
        self.checkbox_206.stateChanged.connect(self.clickbox_206)
        self.checkbox_207.stateChanged.connect(self.clickbox_207)
        self.checkbox_208.stateChanged.connect(self.clickbox_208)

        '''
        ESTÃO LISTADOS ABAIXO OS COMANDOS DOS BOTÕES PARA CHAMAR AS FUNÇOES
        QUE IRÃO ABRIR A JANELA DAS ENFERMIDADES BUSCADAS OU A BIBLIOTECA
        '''

        self.pushButton.clicked.connect(self.button_buscar)
        self.pushButton_2.clicked.connect(self.button_biblioteca)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    '''
    ESTÃO LISTADAS ABAIXO AS FUNÇOES CHAMADAS PELOS CHECKBOXES E BOTÕES
    '''

    def clickbox_0(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[0] = 1
            else:
                sinais_clinicos[0] = 0

    def clickbox_1(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[1] = 1
            else:
                sinais_clinicos[1] = 0

    def clickbox_2(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[2] = 1
            else:
                sinais_clinicos[2] = 0

    def clickbox_3(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[3] = 1
            else:
                sinais_clinicos[3] = 0

    def clickbox_4(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[4] = 1
            else:
                sinais_clinicos[4] = 0

    def clickbox_5(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[5] = 1
            else:
                sinais_clinicos[5] = 0

    def clickbox_6(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[6] = 1
            else:
                sinais_clinicos[6] = 0

    def clickbox_7(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[7] = 1
            else:
                sinais_clinicos[7] = 0

    def clickbox_8(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[8] = 1
            else:
                sinais_clinicos[8] = 0

    def clickbox_9(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[9] = 1
            else:
                sinais_clinicos[9] = 0

    def clickbox_10(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[10] = 1
            else:
                sinais_clinicos[10] = 0

    def clickbox_11(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[11] = 1
            else:
                sinais_clinicos[11] = 0

    def clickbox_12(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[12] = 1
            else:
                sinais_clinicos[12] = 0

    def clickbox_13(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[13] = 1
            else:
                sinais_clinicos[13] = 0

    def clickbox_14(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[14] = 1
            else:
                sinais_clinicos[14] = 0

    def clickbox_15(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[15] = 1
            else:
                sinais_clinicos[15] = 0

    def clickbox_16(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[16] = 1
            else:
                sinais_clinicos[16] = 0

    def clickbox_17(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[17] = 1
            else:
                sinais_clinicos[17] = 0

    def clickbox_18(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[18] = 1
            else:
                sinais_clinicos[18] = 0

    def clickbox_19(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[19] = 1
            else:
                sinais_clinicos[19] = 0

    def clickbox_20(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[20] = 1
            else:
                sinais_clinicos[20] = 0

    def clickbox_21(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[21] = 1
            else:
                sinais_clinicos[21] = 0

    def clickbox_22(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[22] = 1
            else:
                sinais_clinicos[22] = 0

    def clickbox_23(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[23] = 1
            else:
                sinais_clinicos[23] = 0

    def clickbox_24(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[24] = 1
            else:
                sinais_clinicos[24] = 0

    def clickbox_25(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[25] = 1
            else:
                sinais_clinicos[25] = 0

    def clickbox_26(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[26] = 1
            else:
                sinais_clinicos[26] = 0

    def clickbox_27(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[27] = 1
            else:
                sinais_clinicos[27] = 0

    def clickbox_28(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[28] = 1
            else:
                sinais_clinicos[28] = 0

    def clickbox_29(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[29] = 1
            else:
                sinais_clinicos[29] = 0

    def clickbox_30(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[30] = 1
            else:
                sinais_clinicos[30] = 0

    def clickbox_31(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[31] = 1
            else:
                sinais_clinicos[31] = 0

    def clickbox_32(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[32] = 1
            else:
                sinais_clinicos[32] = 0

    def clickbox_33(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[33] = 1
            else:
                sinais_clinicos[33] = 0

    def clickbox_34(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[34] = 1
            else:
                sinais_clinicos[34] = 0

    def clickbox_35(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[35] = 1
            else:
                sinais_clinicos[35] = 0

    def clickbox_36(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[36] = 1
            else:
                sinais_clinicos[36] = 0

    def clickbox_37(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[37] = 1
            else:
                sinais_clinicos[37] = 0

    def clickbox_38(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[38] = 1
            else:
                sinais_clinicos[38] = 0

    def clickbox_39(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[39] = 1
            else:
                sinais_clinicos[39] = 0

    def clickbox_40(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[40] = 1
            else:
                sinais_clinicos[40] = 0

    def clickbox_41(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[41] = 1
            else:
                sinais_clinicos[41] = 0

    def clickbox_42(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[42] = 1
            else:
                sinais_clinicos[42] = 0

    def clickbox_43(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[43] = 1
            else:
                sinais_clinicos[43] = 0

    def clickbox_44(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[44] = 1
            else:
                sinais_clinicos[44] = 0

    def clickbox_45(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[45] = 1
            else:
                sinais_clinicos[45] = 0

    def clickbox_46(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[46] = 1
            else:
                sinais_clinicos[46] = 0

    def clickbox_47(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[47] = 1
            else:
                sinais_clinicos[47] = 0

    def clickbox_48(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[48] = 1
            else:
                sinais_clinicos[48] = 0

    def clickbox_49(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[49] = 1
            else:
                sinais_clinicos[49] = 0

    def clickbox_50(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[50] = 1
            else:
                sinais_clinicos[50] = 0

    def clickbox_51(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[51] = 1
            else:
                sinais_clinicos[51] = 0

    def clickbox_52(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[52] = 1
            else:
                sinais_clinicos[52] = 0

    def clickbox_53(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[53] = 1
            else:
                sinais_clinicos[53] = 0

    def clickbox_54(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[54] = 1
            else:
                sinais_clinicos[1] = 0

    def clickbox_55(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[55] = 1
            else:
                sinais_clinicos[55] = 0

    def clickbox_56(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[56] = 1
            else:
                sinais_clinicos[56] = 0

    def clickbox_57(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[57] = 1
            else:
                sinais_clinicos[57] = 0

    def clickbox_58(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[58] = 1
            else:
                sinais_clinicos[58] = 0

    def clickbox_59(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[59] = 1
            else:
                sinais_clinicos[59] = 0

    def clickbox_60(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[60] = 1
            else:
                sinais_clinicos[60] = 0

    def clickbox_61(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[61] = 1
            else:
                sinais_clinicos[61] = 0

    def clickbox_62(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[62] = 1
            else:
                sinais_clinicos[62] = 0

    def clickbox_63(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[63] = 1
            else:
                sinais_clinicos[63] = 0

    def clickbox_64(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[64] = 1
            else:
                sinais_clinicos[64] = 0

    def clickbox_65(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[65] = 1
            else:
                sinais_clinicos[65] = 0

    def clickbox_66(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[66] = 1
            else:
                sinais_clinicos[66] = 0

    def clickbox_67(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[67] = 1
            else:
                sinais_clinicos[67] = 0

    def clickbox_68(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[68] = 1
            else:
                sinais_clinicos[68] = 0

    def clickbox_69(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[69] = 1
            else:
                sinais_clinicos[69] = 0

    def clickbox_70(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[70] = 1
            else:
                sinais_clinicos[70] = 0

    def clickbox_71(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[71] = 1
            else:
                sinais_clinicos[71] = 0

    def clickbox_72(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[72] = 1
            else:
                sinais_clinicos[72] = 0

    def clickbox_73(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[73] = 1
            else:
                sinais_clinicos[73] = 0

    def clickbox_74(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[74] = 1
            else:
                sinais_clinicos[74] = 0

    def clickbox_75(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[75] = 1
            else:
                sinais_clinicos[75] = 0

    def clickbox_76(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[76] = 1
            else:
                sinais_clinicos[76] = 0

    def clickbox_77(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[77] = 1
            else:
                sinais_clinicos[77] = 0

    def clickbox_78(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[78] = 1
            else:
                sinais_clinicos[78] = 0

    def clickbox_79(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[79] = 1
            else:
                sinais_clinicos[79] = 0

    def clickbox_80(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[80] = 1
            else:
                sinais_clinicos[80] = 0

    def clickbox_81(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[81] = 1
            else:
                sinais_clinicos[81] = 0

    def clickbox_82(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[82] = 1
            else:
                sinais_clinicos[82] = 0

    def clickbox_83(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[83] = 1
            else:
                sinais_clinicos[83] = 0

    def clickbox_84(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[84] = 1
            else:
                sinais_clinicos[84] = 0

    def clickbox_85(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[85] = 1
            else:
                sinais_clinicos[85] = 0

    def clickbox_86(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[86] = 1
            else:
                sinais_clinicos[86] = 0

    def clickbox_87(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[87] = 1
            else:
                sinais_clinicos[87] = 0

    def clickbox_88(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[88] = 1
            else:
                sinais_clinicos[88] = 0

    def clickbox_89(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[89] = 1
            else:
                sinais_clinicos[89] = 0

    def clickbox_90(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[90] = 1
            else:
                sinais_clinicos[90] = 0

    def clickbox_91(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[91] = 1
            else:
                sinais_clinicos[91] = 0

    def clickbox_92(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[92] = 1
            else:
                sinais_clinicos[92] = 0

    def clickbox_93(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[93] = 1
            else:
                sinais_clinicos[93] = 0

    def clickbox_94(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[94] = 1
            else:
                sinais_clinicos[94] = 0

    def clickbox_95(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[95] = 1
            else:
                sinais_clinicos[95] = 0

    def clickbox_96(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[96] = 1
            else:
                sinais_clinicos[96] = 0

    def clickbox_97(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[97] = 1
            else:
                sinais_clinicos[97] = 0

    def clickbox_98(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[98] = 1
            else:
                sinais_clinicos[98] = 0

    def clickbox_99(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[99] = 1
            else:
                sinais_clinicos[99] = 0

    def clickbox_100(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[100] = 1
            else:
                sinais_clinicos[100] = 0

    def clickbox_101(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[101] = 1
            else:
                sinais_clinicos[101] = 0

    def clickbox_102(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[102] = 1
            else:
                sinais_clinicos[102] = 0

    def clickbox_103(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[103] = 1
            else:
                sinais_clinicos[103] = 0

    def clickbox_104(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[104] = 1
            else:
                sinais_clinicos[104] = 0

    def clickbox_105(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[105] = 1
            else:
                sinais_clinicos[105] = 0

    def clickbox_106(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[106] = 1
            else:
                sinais_clinicos[106] = 0

    def clickbox_107(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[107] = 1
            else:
                sinais_clinicos[107] = 0

    def clickbox_108(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[108] = 1
            else:
                sinais_clinicos[108] = 0

    def clickbox_109(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[109] = 1
            else:
                sinais_clinicos[109] = 0

    def clickbox_110(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[110] = 1
            else:
                sinais_clinicos[110] = 0

    def clickbox_111(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[111] = 1
            else:
                sinais_clinicos[111] = 0

    def clickbox_112(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[112] = 1
            else:
                sinais_clinicos[112] = 0

    def clickbox_113(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[113] = 1
            else:
                sinais_clinicos[113] = 0

    def clickbox_114(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[114] = 1
            else:
                sinais_clinicos[114] = 0

    def clickbox_115(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[115] = 1
            else:
                sinais_clinicos[115] = 0

    def clickbox_116(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[116] = 1
            else:
                sinais_clinicos[116] = 0

    def clickbox_117(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[117] = 1
            else:
                sinais_clinicos[117] = 0

    def clickbox_118(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[118] = 1
            else:
                sinais_clinicos[118] = 0

    def clickbox_119(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[119] = 1
            else:
                sinais_clinicos[119] = 0

    def clickbox_120(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[120] = 1
            else:
                sinais_clinicos[120] = 0

    def clickbox_121(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[121] = 1
            else:
                sinais_clinicos[121] = 0

    def clickbox_122(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[122] = 1
            else:
                sinais_clinicos[122] = 0

    def clickbox_123(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[123] = 1
            else:
                sinais_clinicos[123] = 0

    def clickbox_124(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[124] = 1
            else:
                sinais_clinicos[124] = 0

    def clickbox_125(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[125] = 1
            else:
                sinais_clinicos[125] = 0

    def clickbox_126(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[126] = 1
            else:
                sinais_clinicos[126] = 0

    def clickbox_127(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[127] = 1
            else:
                sinais_clinicos[127] = 0

    def clickbox_128(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[128] = 1
            else:
                sinais_clinicos[128] = 0

    def clickbox_129(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[129] = 1
            else:
                sinais_clinicos[129] = 0

    def clickbox_130(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[130] = 1
            else:
                sinais_clinicos[130] = 0

    def clickbox_131(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[131] = 1
            else:
                sinais_clinicos[131] = 0

    def clickbox_132(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[132] = 1
            else:
                sinais_clinicos[132] = 0

    def clickbox_133(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[133] = 1
            else:
                sinais_clinicos[133] = 0

    def clickbox_134(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[134] = 1
            else:
                sinais_clinicos[134] = 0

    def clickbox_135(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[135] = 1
            else:
                sinais_clinicos[135] = 0

    def clickbox_136(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[136] = 1
            else:
                sinais_clinicos[136] = 0

    def clickbox_137(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[137] = 1
            else:
                sinais_clinicos[137] = 0

    def clickbox_138(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[138] = 1
            else:
                sinais_clinicos[138] = 0

    def clickbox_139(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[139] = 1
            else:
                sinais_clinicos[139] = 0

    def clickbox_140(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[140] = 1
            else:
                sinais_clinicos[140] = 0

    def clickbox_141(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[141] = 1
            else:
                sinais_clinicos[141] = 0

    def clickbox_142(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[142] = 1
            else:
                sinais_clinicos[142] = 0

    def clickbox_143(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[143] = 1
            else:
                sinais_clinicos[143] = 0

    def clickbox_144(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[144] = 1
            else:
                sinais_clinicos[144] = 0

    def clickbox_145(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[145] = 1
            else:
                sinais_clinicos[145] = 0

    def clickbox_146(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[146] = 1
            else:
                sinais_clinicos[146] = 0

    def clickbox_147(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[147] = 1
            else:
                sinais_clinicos[147] = 0

    def clickbox_148(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[148] = 1
            else:
                sinais_clinicos[148] = 0

    def clickbox_149(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[149] = 1
            else:
                sinais_clinicos[149] = 0

    def clickbox_150(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[150] = 1
            else:
                sinais_clinicos[150] = 0

    def clickbox_151(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[151] = 1
            else:
                sinais_clinicos[151] = 0

    def clickbox_152(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[152] = 1
            else:
                sinais_clinicos[152] = 0

    def clickbox_153(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[153] = 1
            else:
                sinais_clinicos[153] = 0

    def clickbox_154(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[154] = 1
            else:
                sinais_clinicos[154] = 0

    def clickbox_155(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[155] = 1
            else:
                sinais_clinicos[155] = 0

    def clickbox_156(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[156] = 1
            else:
                sinais_clinicos[156] = 0

    def clickbox_157(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[157] = 1
            else:
                sinais_clinicos[157] = 0

    def clickbox_158(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[158] = 1
            else:
                sinais_clinicos[158] = 0

    def clickbox_159(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[159] = 1
            else:
                sinais_clinicos[159] = 0

    def clickbox_160(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[160] = 1
            else:
                sinais_clinicos[160] = 0

    def clickbox_161(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[161] = 1
            else:
                sinais_clinicos[161] = 0

    def clickbox_162(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[162] = 1
            else:
                sinais_clinicos[162] = 0

    def clickbox_163(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[163] = 1
            else:
                sinais_clinicos[163] = 0

    def clickbox_164(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[164] = 1
            else:
                sinais_clinicos[164] = 0

    def clickbox_165(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[165] = 1
            else:
                sinais_clinicos[165] = 0

    def clickbox_166(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[166] = 1
            else:
                sinais_clinicos[166] = 0

    def clickbox_167(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[167] = 1
            else:
                sinais_clinicos[167] = 0

    def clickbox_168(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[168] = 1
            else:
                sinais_clinicos[168] = 0

    def clickbox_169(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[169] = 1
            else:
                sinais_clinicos[169] = 0

    def clickbox_170(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[170] = 1
            else:
                sinais_clinicos[170] = 0

    def clickbox_171(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[171] = 1
            else:
                sinais_clinicos[171] = 0

    def clickbox_172(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[172] = 1
            else:
                sinais_clinicos[172] = 0

    def clickbox_173(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[173] = 1
            else:
                sinais_clinicos[173] = 0

    def clickbox_174(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[174] = 1
            else:
                sinais_clinicos[174] = 0

    def clickbox_175(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[175] = 1
            else:
                sinais_clinicos[175] = 0

    def clickbox_176(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[176] = 1
            else:
                sinais_clinicos[176] = 0

    def clickbox_177(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[177] = 1
            else:
                sinais_clinicos[177] = 0

    def clickbox_178(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[178] = 1
            else:
                sinais_clinicos[178] = 0

    def clickbox_179(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[179] = 1
            else:
                sinais_clinicos[179] = 0

    def clickbox_180(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[180] = 1
            else:
                sinais_clinicos[180] = 0

    def clickbox_181(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[181] = 1
            else:
                sinais_clinicos[181] = 0

    def clickbox_182(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[182] = 1
            else:
                sinais_clinicos[182] = 0

    def clickbox_183(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[183] = 1
            else:
                sinais_clinicos[183] = 0

    def clickbox_184(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[184] = 1
            else:
                sinais_clinicos[184] = 0

    def clickbox_185(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[185] = 1
            else:
                sinais_clinicos[185] = 0

    def clickbox_186(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[186] = 1
            else:
                sinais_clinicos[186] = 0

    def clickbox_187(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[187] = 1
            else:
                sinais_clinicos[187] = 0

    def clickbox_188(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[188] = 1
            else:
                sinais_clinicos[188] = 0

    def clickbox_189(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[189] = 1
            else:
                sinais_clinicos[189] = 0

    def clickbox_190(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[190] = 1
            else:
                sinais_clinicos[190] = 0

    def clickbox_191(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[191] = 1
            else:
                sinais_clinicos[191] = 0

    def clickbox_192(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[192] = 1
            else:
                sinais_clinicos[192] = 0

    def clickbox_193(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[193] = 1
            else:
                sinais_clinicos[193] = 0

    def clickbox_194(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[194] = 1
            else:
                sinais_clinicos[194] = 0

    def clickbox_195(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[1] = 1
            else:
                sinais_clinicos[1] = 0

    def clickbox_196(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[196] = 1
            else:
                sinais_clinicos[196] = 0

    def clickbox_197(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[197] = 1
            else:
                sinais_clinicos[197] = 0

    def clickbox_198(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[198] = 1
            else:
                sinais_clinicos[198] = 0

    def clickbox_199(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[199] = 1
            else:
                sinais_clinicos[199] = 0

    def clickbox_200(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[200] = 1
            else:
                sinais_clinicos[200] = 0

    def clickbox_201(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[201] = 1
            else:
                sinais_clinicos[201] = 0

    def clickbox_202(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[202] = 1
            else:
                sinais_clinicos[202] = 0

    def clickbox_203(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[203] = 1
            else:
                sinais_clinicos[203] = 0

    def clickbox_204(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[204] = 1
            else:
                sinais_clinicos[204] = 0

    def clickbox_205(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[205] = 1
            else:
                sinais_clinicos[205] = 0

    def clickbox_206(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[206] = 1
            else:
                sinais_clinicos[206] = 0

    def clickbox_207(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[207] = 1
            else:
                sinais_clinicos[207] = 0

    def clickbox_208(self,state):
            if state == QtCore.Qt.Checked:
                sinais_clinicos[208] = 1
            else:
                sinais_clinicos[208] = 0



    def button_buscar(self,state):
        global lista_P_E
        probabilidade = avaliar_sinais_clinicos(sinais_clinicos)

        for n,i in enumerate(probabilidade):
            reg =[i,enfermidades[n]]
            lista_P_E.append(reg)
        lista_P_E.sort(reverse=True)

        for i in range(len(lista_P_E)):
            lista_P_E[i][0]=(round(lista_P_E[i][0],2))


        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ResultWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        lista_P_E = []

        #SCRIPT TESTA CAIXAS DE SELEÇÃO
        if sinais_clinicos[86] == 1:
            print ("botão marcado")
        else:
            print ("Botão desmarcado")

        if sinais_clinicos[123] == 1:
            print ("botão marcado")
        else:
            print ("Botão desmarcado")

        if sinais_clinicos[16] == 1:
            print ("botão marcado")
        else:
            print ("Botão desmarcado")

    def button_suporte(self):
        os.startfile("suporte.py")

    def button_info(self):
        os.startfile("info.py")

    def button_legais(self):
        os.startfile("legais.py")

    def button_biblioteca(self):
        os.startfile("biblioteca.py")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Buiatric Care"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Century Gothic\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Seja bem-vindo ao Buiatric Care, uma biblioteca digital para auxiliá-lo no conhecimento e busca de informações acerca do diagnóstico de enfermidades do sistema nervoso central de bovinos. Para utilizar essa ferramenta você deve marcar nas caixas de seleção referentes aos sinais clínicos desejados e pressionar o botão &quot;Buscar enfermidade&quot;. O Programa irá direcioná-lo paras as enfermidades mais prováveis, apontando-lhes o porcentual de probabilidade. Na segunda interface será possível acessar a etiopatogenia, aspectos epidemiológicos, sinais clínicos, possibilidades terapêuticas, quando houver, profilaxia e prevenção.</p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Biblioteca de enfermidades"))
        self.pushButton.setText(_translate("MainWindow", "Buscar enfermidade"))
        self.checkbox_169.setText(_translate("MainWindow", "Pressão da cabeça contra obstáculos"))
        self.checkbox_170.setText(_translate("MainWindow", "Prolapso da terceira pálpebra (membrana nictante)"))
        self.checkbox_166.setText(_translate("MainWindow", "Polipnéia"))
        self.checkbox_167.setText(_translate("MainWindow", "Posição de autoauscultação"))
        self.checkbox_165.setText(_translate("MainWindow", "Poliflexão dos membros"))
        self.checkbox_164.setText(_translate("MainWindow", "Perda do reflexo palpebral"))
        self.checkbox_163.setText(_translate("MainWindow", "Perda do equilíbrio"))
        self.checkbox_171.setText(_translate("MainWindow", "Prostração"))
        self.checkbox_152.setText(_translate("MainWindow", "Paralisia com decúbito lateral ou esternal permanente"))
        self.checkbox_177.setText(_translate("MainWindow", "Relaxamento do esfíncter anal"))
        self.checkbox_179.setText(_translate("MainWindow", "Respiração oabdominal"))
        self.checkbox_173.setText(_translate("MainWindow", "Prurido intenso no ponto de inoculação"))
        self.checkbox_178.setText(_translate("MainWindow", "Relutância na locomoção"))
        self.checkbox_174.setText(_translate("MainWindow", "Ptose palpebral"))
        self.checkbox_112.setText(_translate("MainWindow", "Inquietação"))
        self.checkbox_64.setText(_translate("MainWindow", "Edema pulmonar"))
        self.checkbox_35.setText(_translate("MainWindow", "Contração das pálpebras"))
        self.checkbox_111.setText(_translate("MainWindow", "Infertilidade"))
        self.checkbox_109.setText(_translate("MainWindow", "Incoordenação motora"))
        self.checkbox_121.setText(_translate("MainWindow", "Linfadenomegalia"))
        self.checkbox_30.setText(_translate("MainWindow", "Ceratoconjuntivite"))
        self.checkbox_33.setText(_translate("MainWindow", "Constipação"))
        self.checkbox_31.setText(_translate("MainWindow", "Cianose"))
        self.checkbox_34.setText(_translate("MainWindow", "Contração das orelhas"))
        self.checkbox_29.setText(_translate("MainWindow", "Ceratite"))
        self.checkbox_32.setText(_translate("MainWindow", "Coma"))
        self.checkbox_65.setText(_translate("MainWindow", "Edema submandibular"))
        self.checkbox_82.setText(_translate("MainWindow", "Fasciculações"))
        self.checkbox_110.setText(_translate("MainWindow", "Inepsia para girar"))
        self.checkbox_41.setText(_translate("MainWindow", "Debilidade"))
        self.checkbox_25.setText(_translate("MainWindow", "Cambaleios"))
        self.checkbox_37.setText(_translate("MainWindow", "Contrações tônico-clônicas"))
        self.checkbox_26.setText(_translate("MainWindow", "Caquexia"))
        self.checkbox_113.setText(_translate("MainWindow", "Irritabilidade"))
        self.checkbox_117.setText(_translate("MainWindow", "Lambedura das narinas"))
        self.checkbox_116.setText(_translate("MainWindow", "Lambedura dos flancos e narinas"))
        self.checkbox_157.setText(_translate("MainWindow", "Paralisia espástica dos membros"))
        self.checkbox_151.setText(_translate("MainWindow", "Parada cardiorrespiratória"))
        self.checkbox_158.setText(_translate("MainWindow", "Paralisia facial"))
        self.checkbox_153.setText(_translate("MainWindow", "Paralisia da cauda"))
        self.checkbox_132.setText(_translate("MainWindow", "Morte súbita"))
        self.checkbox_156.setText(_translate("MainWindow", "Paralisia e protrusão da língua"))
        self.checkbox_150.setText(_translate("MainWindow", "Panoftalmite"))
        self.checkbox_134.setText(_translate("MainWindow", "Movimentos abruptos e violentos"))
        self.checkbox_131.setText(_translate("MainWindow", "Mortalidade perinatal"))
        self.checkbox_135.setText(_translate("MainWindow", "Movimentos de pedalagem"))
        self.checkbox_136.setText(_translate("MainWindow", "Movimentos frequentes e ritmados da orelha"))
        self.checkbox_129.setText(_translate("MainWindow", "Mímicas de mastigação"))
        self.checkbox_133.setText(_translate("MainWindow", "Movimentos desordenados com a cabeça em sentido horizontal"))
        self.checkbox_96.setText(_translate("MainWindow", "Hiperestesia"))
        self.checkbox_119.setText(_translate("MainWindow", "Lesões erosiva-ulcerativa na mucosa do trato respiratório, focinho, narinas e mucosa oral"))
        self.checkbox_36.setText(_translate("MainWindow", "Contrações musculares"))
        self.checkbox_137.setText(_translate("MainWindow", "Movimentos lentos ou incertos"))
        self.checkbox_38.setText(_translate("MainWindow", "Convulsões"))
        self.checkbox_130.setText(_translate("MainWindow", "Miose"))
        self.checkbox_128.setText(_translate("MainWindow", "Midríase"))
        self.checkbox_95.setText(_translate("MainWindow", "Hiperatividade"))
        self.checkbox_97.setText(_translate("MainWindow", "Hiperexcitabildidade"))
        self.checkbox_99.setText(_translate("MainWindow", "Hipermotilidade gastrintestinal"))
        self.checkbox_91.setText(_translate("MainWindow", "Fraqueza muscular"))
        self.checkbox_88.setText(_translate("MainWindow", "Flacidez do lábio superior"))
        self.checkbox_40.setText(_translate("MainWindow", "Corrimento nasal e ocular"))
        self.checkbox_83.setText(_translate("MainWindow", "Febre"))
        self.checkbox_27.setText(_translate("MainWindow", "Cegueira"))
        self.checkbox_142.setText(_translate("MainWindow", "Odor de acetona à respiração"))
        self.checkbox_39.setText(_translate("MainWindow", "Convulsões com movimentos tônico-clônicos"))
        self.checkbox_28.setText(_translate("MainWindow", "Cegueira cortical parcial ou total"))
        self.checkbox_144.setText(_translate("MainWindow", "Odor de amônia no ar expirado"))
        self.checkbox_98.setText(_translate("MainWindow", "Hipermetria"))
        self.checkbox_93.setText(_translate("MainWindow", "Geofagia"))
        self.checkbox_94.setText(_translate("MainWindow", "Hemoglobinúria"))
        self.checkbox_187.setText(_translate("MainWindow", "Rigidez dos membros pélvicos"))
        self.checkbox_185.setText(_translate("MainWindow", "Retenção de alimento na boca"))
        self.checkbox_186.setText(_translate("MainWindow", "Retenção ou incontinência urinária"))
        self.checkbox_190.setText(_translate("MainWindow", "Sereção nasal"))
        self.checkbox_196.setText(_translate("MainWindow", "Taquisfigmia"))
        self.checkbox_201.setText(_translate("MainWindow", "Timpanismo ruminal"))
        self.checkbox_205.setText(_translate("MainWindow", "Trismos"))
        self.checkbox_192.setText(_translate("MainWindow", "Sonolência"))
        self.checkbox_206.setText(_translate("MainWindow", "Úlcera de córnea"))
        self.checkbox_195.setText(_translate("MainWindow", "Taquipnéia"))
        self.checkbox_203.setText(_translate("MainWindow", "Tremores celebelares"))
        self.checkbox_197.setText(_translate("MainWindow", "Tendência a quedas"))
        self.checkbox_194.setText(_translate("MainWindow", "Taquicardia"))
        self.checkbox_200.setText(_translate("MainWindow", "Tetania dos músculos masseteres"))
        self.checkbox_159.setText(_translate("MainWindow", "Paralisia flácida dos membros"))
        self.checkbox_198.setText(_translate("MainWindow", "Tenesmo"))
        self.checkbox_204.setText(_translate("MainWindow", "Tremores da pele"))
        self.checkbox_155.setText(_translate("MainWindow", "Paralisia dos membros pélvicos"))
        self.checkbox_154.setText(_translate("MainWindow", "Paralisia da mandíbula"))
        self.checkbox_140.setText(_translate("MainWindow", "Náuseas"))
        self.checkbox_199.setText(_translate("MainWindow", "Tetania"))
        self.checkbox_162.setText(_translate("MainWindow", "Perda da consciência"))
        self.checkbox_143.setText(_translate("MainWindow", "Odor de acetona na urina"))
        self.checkbox_57.setText(_translate("MainWindow", "Diminuição do escore de condição corporal"))
        self.checkbox_55.setText(_translate("MainWindow", "Diminuição da produção leiteira"))
        self.checkbox_60.setText(_translate("MainWindow", "Dismetria"))
        self.checkbox_71.setText(_translate("MainWindow", "Eructação excessiva"))
        self.checkbox_50.setText(_translate("MainWindow", "Dificuldade de apreensão de alimentos"))
        self.checkbox_61.setText(_translate("MainWindow", "Dispnéia"))
        self.checkbox_59.setText(_translate("MainWindow", "Disfagia"))
        self.checkbox_54.setText(_translate("MainWindow", "Dificuldade respiratória"))
        self.checkbox_0.setText(_translate("MainWindow", "Abortamento"))
        self.checkbox_22.setText(_translate("MainWindow", "Ausência do reflexo de ameaça"))
        self.checkbox_49.setText(_translate("MainWindow", "Diarréia"))
        self.checkbox_181.setText(_translate("MainWindow", "Respiração bifásica à inspiração"))
        self.checkbox_176.setText(_translate("MainWindow", "Reflexo palpebral ausente ou diminuído"))
        self.checkbox_182.setText(_translate("MainWindow", "Respiração estertorosa"))
        self.checkbox_202.setText(_translate("MainWindow", "Torneio"))
        self.checkbox_184.setText(_translate("MainWindow", "Respiração superfiial"))
        self.checkbox_42.setText(_translate("MainWindow", "Decúbito esternal ou lateral"))
        self.checkbox_5.setText(_translate("MainWindow", "Alteração da postura"))
        self.checkbox_6.setText(_translate("MainWindow", "Amaurose"))
        self.checkbox_4.setText(_translate("MainWindow", "Alotriofagia ou pica"))
        self.checkbox_24.setText(_translate("MainWindow", "Bruxismo"))
        self.checkbox_17.setText(_translate("MainWindow", "Apetite caprichoso"))
        self.checkbox_47.setText(_translate("MainWindow", "Desvio lateral da cauda"))
        self.checkbox_9.setText(_translate("MainWindow", "Andar em marcha"))
        self.checkbox_18.setText(_translate("MainWindow", "Ataques epiletiformes"))
        self.checkbox_44.setText(_translate("MainWindow", "Desidratação"))
        self.checkbox_13.setText(_translate("MainWindow", "Animal em alerta"))
        self.checkbox_43.setText(_translate("MainWindow", "Depressão"))
        self.checkbox_19.setText(_translate("MainWindow", "Ataxia"))
        self.checkbox_16.setText(_translate("MainWindow", "Apatia"))
        self.checkbox_10.setText(_translate("MainWindow", "Andar rígido"))
        self.checkbox_20.setText(_translate("MainWindow", "Atonia ruminal"))
        self.checkbox_14.setText(_translate("MainWindow", "Anorexia"))
        self.checkbox_48.setText(_translate("MainWindow", "Desvio lateral do corpo"))
        self.checkbox_11.setText(_translate("MainWindow", "Anemia"))
        self.checkbox_45.setText(_translate("MainWindow", "Despigmentação ao redor dos olhos"))
        self.checkbox_51.setText(_translate("MainWindow", "Dificuldade de deglutição"))
        self.checkbox_12.setText(_translate("MainWindow", "Anestro"))
        self.checkbox_15.setText(_translate("MainWindow", "Ansiedade"))
        self.checkbox_62.setText(_translate("MainWindow", "Dispnéia mista"))
        self.checkbox_46.setText(_translate("MainWindow", "Desvio lateral da cabeça"))
        self.checkbox_53.setText(_translate("MainWindow", "Dificuldade na mastigação"))
        self.checkbox_58.setText(_translate("MainWindow", "Diminuição dos reflexos cutâneos"))
        self.checkbox_63.setText(_translate("MainWindow", "Dor abdominal"))
        self.checkbox_56.setText(_translate("MainWindow", "Diminuição da sensibilidade cutânea"))
        self.checkbox_7.setText(_translate("MainWindow", "Andar a esmo"))
        self.checkbox_52.setText(_translate("MainWindow", "Dificuldade na locomoção"))
        self.checkbox_80.setText(_translate("MainWindow", "Extremidades frias"))
        self.checkbox_73.setText(_translate("MainWindow", "Estado geral debilitado"))
        self.checkbox_66.setText(_translate("MainWindow", "Elevadas concentrações de ácidos graxos livres no sangue"))
        self.checkbox_75.setText(_translate("MainWindow", "Estrabismo dorsomedial"))
        self.checkbox_79.setText(_translate("MainWindow", "Extensão do pescoço e membros torácicos"))
        self.checkbox_74.setText(_translate("MainWindow", "Esteatose hepática"))
        self.checkbox_76.setText(_translate("MainWindow", "Estros irregulares"))
        self.checkbox_72.setText(_translate("MainWindow", "Espasmos musculares"))
        self.checkbox_77.setText(_translate("MainWindow", "Exagerada movimentação das orelhas"))
        self.checkbox_78.setText(_translate("MainWindow", "Expiração sob forma de gemidos"))
        self.checkbox_81.setText(_translate("MainWindow", "Fasciculação dos músculos da face pescoço e orelhas"))
        self.checkbox_100.setText(_translate("MainWindow", "Hipofonese"))
        self.checkbox_102.setText(_translate("MainWindow", "Hipomielinogênese"))
        self.checkbox_92.setText(_translate("MainWindow", "Frenesi"))
        self.checkbox_101.setText(_translate("MainWindow", "Hipoglicemia"))
        self.checkbox_103.setText(_translate("MainWindow", "Hipoproteinemia"))
        self.checkbox_106.setText(_translate("MainWindow", "Hipotonia ruminal"))
        self.checkbox_115.setText(_translate("MainWindow", "Isolamento"))
        self.checkbox_107.setText(_translate("MainWindow", "Incapacidade de apreensão e ingestão de água e alimentos"))
        self.checkbox_104.setText(_translate("MainWindow", "Hiporexia"))
        self.checkbox_105.setText(_translate("MainWindow", "Hipotermia"))
        self.checkbox_118.setText(_translate("MainWindow", "Lambedura vigorosa da pele"))
        self.checkbox_120.setText(_translate("MainWindow", "Letargia"))
        self.checkbox_114.setText(_translate("MainWindow", "Irritação cutânea"))
        self.checkbox_108.setText(_translate("MainWindow", "Inclinação lateral da cabeça durante mastigação"))
        self.checkbox_69.setText(_translate("MainWindow", "Emissão de gemidos roucos"))
        self.checkbox_1.setText(_translate("MainWindow", "Acromotriquia"))
        self.checkbox_67.setText(_translate("MainWindow", "Emaciação"))
        self.checkbox_8.setText(_translate("MainWindow", "Andar em círculos"))
        self.checkbox_21.setText(_translate("MainWindow", "Atrofia do mósculo da face e masseter"))
        self.checkbox_70.setText(_translate("MainWindow", "Epífora"))
        self.checkbox_2.setText(_translate("MainWindow", "Agressividade"))
        self.checkbox_68.setText(_translate("MainWindow", "Embotamento"))
        self.checkbox_23.setText(_translate("MainWindow", "Bradicardia"))
        self.checkbox_175.setText(_translate("MainWindow", "Redução significativa no débito cardíaco"))
        self.checkbox_188.setText(_translate("MainWindow", "Rigidez muscular"))
        self.checkbox_183.setText(_translate("MainWindow", "Respiração ruidosa"))
        self.checkbox_193.setText(_translate("MainWindow", "Sudorese excessiva"))
        self.checkbox_189.setText(_translate("MainWindow", "Saída de espuma pela cavidade nasal e oral"))
        self.checkbox_191.setText(_translate("MainWindow", "Sialorréia"))
        self.checkbox_123.setText(_translate("MainWindow", "Marcha trôpega"))
        self.checkbox_122.setText(_translate("MainWindow", "Marcha para trás"))
        self.checkbox_139.setText(_translate("MainWindow", "Mugidos"))
        self.checkbox_124.setText(_translate("MainWindow", "Medo"))
        self.checkbox_126.setText(_translate("MainWindow", "Meneios de cabeça"))
        self.checkbox_125.setText(_translate("MainWindow", "Meneios de cabeça e parte anterior do corpo"))
        self.checkbox_138.setText(_translate("MainWindow", "Mufla seca"))
        self.checkbox_127.setText(_translate("MainWindow", "Micção e defecação frequentes"))
        self.checkbox_146.setText(_translate("MainWindow", "Opacidade bilateral da córnea"))
        self.checkbox_147.setText(_translate("MainWindow", "Opistótono"))
        self.checkbox_145.setText(_translate("MainWindow", "Olhar atento"))
        self.checkbox_149.setText(_translate("MainWindow", "Orelhas em posição de alerta"))
        self.checkbox_160.setText(_translate("MainWindow", "Pêlos arrepiados"))
        self.checkbox_148.setText(_translate("MainWindow", "Orelhas caídas"))
        self.checkbox_172.setText(_translate("MainWindow", "Prurido"))
        self.checkbox_161.setText(_translate("MainWindow", "Pêlos ásperos"))
        self.checkbox_168.setText(_translate("MainWindow", "Posição de cavalete"))
        self.checkbox_180.setText(_translate("MainWindow", "Respiração acelerada, irregular e laboriosa"))
        self.checkbox_85.setText(_translate("MainWindow", "Fezes ressecadas e escassas"))
        self.checkbox_84.setText(_translate("MainWindow", "Fechamento assimétrico da mandíbula"))
        self.checkbox_86.setText(_translate("MainWindow", "Fezes ressecadas e firmes"))
        self.checkbox_89.setText(_translate("MainWindow", "Flexão do boleto ou emboletamento"))
        self.checkbox_90.setText(_translate("MainWindow", "Franzir do nariz"))
        self.checkbox_87.setText(_translate("MainWindow", "Fibrilação ventricular e colapso seguido de morte"))
        self.checkbox_207.setText(_translate("MainWindow", "vacas parem bezerros com malformações congênitas nos membros"))
        self.checkbox_208.setText(_translate("MainWindow", "Vômito"))
        self.checkbox_141.setText(_translate("MainWindow", "Nistagmo"))
        self.menuAjuda.setTitle(_translate("MainWindow", "Ajuda"))
        self.actionAvisos_legais.setText(_translate("MainWindow", "Avisos legais"))
        self.actionSuporte.setText(_translate("MainWindow", "Suporte"))
        self.actionInforma_es_do_programa.setText(_translate("MainWindow", "Informações do programa"))

        self.actionAvisos_legais.triggered.connect(self.button_legais)
        self.actionSuporte.triggered.connect(self.button_suporte)
        self.actionInforma_es_do_programa.triggered.connect(self.button_info)

'''
AQUI INICIAM-SE AS LINHAS DE CÓDIGO PARA A JANELA DE RESULTADO DA BUSCA DE ENFERMIDADES
'''

class Ui_ResultWindow(object):
    def setupUi(self, ResultWindow):
        ResultWindow.setObjectName("ResultWindow")
        ResultWindow.setWindowModality(QtCore.Qt.NonModal)
        ResultWindow.resize(563, 554)
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
        ResultWindow.setPalette(palette)
        ResultWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        ResultWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        ResultWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imagens/bcicone.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ResultWindow.setWindowIcon(icon)
        ResultWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(ResultWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("imagens/logo3.png"))
        self.logo.setObjectName("logo")
        self.verticalLayout.addWidget(self.logo)
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.verticalLayout.addWidget(self.titulo)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(198, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(198, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(198, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(198, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.scrollArea.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.scrollArea.setFont(font)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -399, 526, 702))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.enfermidade_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enfermidade_1.setObjectName("enfermidade_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.enfermidade_1)
        self.probabilidade_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.probabilidade_1.setObjectName("probabilidade_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.probabilidade_1)
        self.enfermidade_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enfermidade_2.setObjectName("enfermidade_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.enfermidade_2)
        self.probabilidade_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.probabilidade_2.setObjectName("probabilidade_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.probabilidade_2)
        self.enfermidade_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enfermidade_3.setObjectName("enfermidade_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.enfermidade_3)
        self.probabilidade_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.probabilidade_3.setObjectName("probabilidade_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.probabilidade_3)
        self.enfermidade_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enfermidade_4.setObjectName("enfermidade_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.enfermidade_4)
        self.probabilidade_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.probabilidade_4.setObjectName("probabilidade_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.probabilidade_4)
        self.enfermidade_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enfermidade_5.setObjectName("enfermidade_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.enfermidade_5)
        self.probabilidade_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.probabilidade_5.setObjectName("probabilidade_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.probabilidade_5)
        self.enfermidade_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enfermidade_6.setObjectName("enfermidade_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.enfermidade_6)
        self.probabilidade_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.probabilidade_6.setObjectName("probabilidade_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.probabilidade_6)
        self.enfermidade_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enfermidade_7.setObjectName("enfermidade_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.enfermidade_7)
        self.probabilidade_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.probabilidade_7.setObjectName("probabilidade_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.probabilidade_7)
        self.enfermidade_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enfermidade_8.setObjectName("enfermidade_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.enfermidade_8)
        self.probabilidade_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.probabilidade_8.setObjectName("probabilidade_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.probabilidade_8)
        self.enfermidade_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enfermidade_9.setObjectName("enfermidade_9")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.enfermidade_9)
        self.probabilidade_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.probabilidade_9.setObjectName("probabilidade_9")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.probabilidade_9)
        self.enfermidade_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enfermidade_10.setObjectName("enfermidade_10")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.enfermidade_10)
        self.probabilidade_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.probabilidade_10.setObjectName("probabilidade_10")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.probabilidade_10)
        self.enfermidade_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enfermidade_11.setObjectName("enfermidade_11")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.enfermidade_11)
        self.probabilidade_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.probabilidade_11.setObjectName("probabilidade_11")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.probabilidade_11)
        self.enfermidade_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enfermidade_12.setObjectName("enfermidade_12")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.enfermidade_12)
        self.probabilidade_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.probabilidade_12.setObjectName("probabilidade_12")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.probabilidade_12)
        self.enfermidade_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enfermidade_14.setObjectName("enfermidade_14")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.enfermidade_14)
        self.probabilidade_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.probabilidade_14.setObjectName("probabilidade_14")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.probabilidade_14)
        self.enfermidade_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enfermidade_16.setObjectName("enfermidade_16")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.enfermidade_16)
        self.probabilidade_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.probabilidade_16.setObjectName("probabilidade_16")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.probabilidade_16)
        self.enfermidade_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enfermidade_17.setObjectName("enfermidade_17")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.enfermidade_17)
        self.probabilidade_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.probabilidade_17.setObjectName("probabilidade_17")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.probabilidade_17)
        self.enfermidade_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enfermidade_20.setObjectName("enfermidade_20")
        self.formLayout.setWidget(19, QtWidgets.QFormLayout.LabelRole, self.enfermidade_20)
        self.probabilidade_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.probabilidade_20.setObjectName("probabilidade_20")
        self.formLayout.setWidget(19, QtWidgets.QFormLayout.FieldRole, self.probabilidade_20)
        self.enfermidade_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enfermidade_22.setObjectName("enfermidade_22")
        self.formLayout.setWidget(21, QtWidgets.QFormLayout.LabelRole, self.enfermidade_22)
        self.probabilidade_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.probabilidade_22.setObjectName("probabilidade_22")
        self.formLayout.setWidget(21, QtWidgets.QFormLayout.FieldRole, self.probabilidade_22)
        self.enfermidade_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enfermidade_23.setObjectName("enfermidade_23")
        self.formLayout.setWidget(22, QtWidgets.QFormLayout.LabelRole, self.enfermidade_23)
        self.probabilidade_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.probabilidade_23.setObjectName("probabilidade_23")
        self.formLayout.setWidget(22, QtWidgets.QFormLayout.FieldRole, self.probabilidade_23)
        self.enfermidade_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enfermidade_24.setObjectName("enfermidade_24")
        self.formLayout.setWidget(23, QtWidgets.QFormLayout.LabelRole, self.enfermidade_24)
        self.probabilidade_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.probabilidade_24.setObjectName("probabilidade_24")
        self.formLayout.setWidget(23, QtWidgets.QFormLayout.FieldRole, self.probabilidade_24)
        self.enfermidade_25 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enfermidade_25.setObjectName("enfermidade_25")
        self.formLayout.setWidget(24, QtWidgets.QFormLayout.LabelRole, self.enfermidade_25)
        self.probabilidade_25 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.probabilidade_25.setObjectName("probabilidade_25")
        self.formLayout.setWidget(24, QtWidgets.QFormLayout.FieldRole, self.probabilidade_25)
        self.enfermidade_26 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enfermidade_26.setObjectName("enfermidade_26")
        self.formLayout.setWidget(25, QtWidgets.QFormLayout.LabelRole, self.enfermidade_26)
        self.probabilidade_26 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.probabilidade_26.setObjectName("probabilidade_26")
        self.formLayout.setWidget(25, QtWidgets.QFormLayout.FieldRole, self.probabilidade_26)
        self.enfermidade_27 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enfermidade_27.setObjectName("enfermidade_27")
        self.formLayout.setWidget(26, QtWidgets.QFormLayout.LabelRole, self.enfermidade_27)
        self.probabilidade_27 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.probabilidade_27.setObjectName("probabilidade_27")
        self.formLayout.setWidget(26, QtWidgets.QFormLayout.FieldRole, self.probabilidade_27)
        self.enfermidade_28 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enfermidade_28.setObjectName("enfermidade_28")
        self.formLayout.setWidget(27, QtWidgets.QFormLayout.LabelRole, self.enfermidade_28)
        self.probabilidade_28 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.probabilidade_28.setObjectName("probabilidade_28")
        self.formLayout.setWidget(27, QtWidgets.QFormLayout.FieldRole, self.probabilidade_28)
        self.enfermidade_29 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enfermidade_29.setObjectName("enfermidade_29")
        self.formLayout.setWidget(28, QtWidgets.QFormLayout.LabelRole, self.enfermidade_29)
        self.probabilidade_29 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.probabilidade_29.setObjectName("probabilidade_29")
        self.formLayout.setWidget(28, QtWidgets.QFormLayout.FieldRole, self.probabilidade_29)
        self.enfermidade_30 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enfermidade_30.setObjectName("enfermidade_30")
        self.formLayout.setWidget(29, QtWidgets.QFormLayout.LabelRole, self.enfermidade_30)
        self.probabilidade_30 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.probabilidade_30.setObjectName("probabilidade_30")
        self.formLayout.setWidget(29, QtWidgets.QFormLayout.FieldRole, self.probabilidade_30)
        self.enfermidade_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enfermidade_21.setObjectName("enfermidade_21")
        self.formLayout.setWidget(20, QtWidgets.QFormLayout.LabelRole, self.enfermidade_21)
        self.probabilidade_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.probabilidade_21.setObjectName("probabilidade_21")
        self.formLayout.setWidget(20, QtWidgets.QFormLayout.FieldRole, self.probabilidade_21)
        self.enfermidade_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enfermidade_19.setObjectName("enfermidade_19")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.LabelRole, self.enfermidade_19)
        self.probabilidade_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.probabilidade_19.setObjectName("probabilidade_19")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.FieldRole, self.probabilidade_19)
        self.enfermidade_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enfermidade_18.setObjectName("enfermidade_18")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.enfermidade_18)
        self.probabilidade_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.probabilidade_18.setObjectName("probabilidade_18")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.probabilidade_18)
        self.enfermidade_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enfermidade_15.setObjectName("enfermidade_15")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.enfermidade_15)
        self.probabilidade_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.probabilidade_15.setObjectName("probabilidade_15")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.probabilidade_15)
        self.enfermidade_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.enfermidade_13.setObjectName("enfermidade_13")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.enfermidade_13)
        self.probabilidade_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.probabilidade_13.setObjectName("probabilidade_13")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.probabilidade_13)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.biblioteca_enfermidades = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.biblioteca_enfermidades.setFont(font)
        self.biblioteca_enfermidades.setObjectName("biblioteca_enfermidades")
        self.verticalLayout.addWidget(self.biblioteca_enfermidades)
        ResultWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ResultWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 563, 21))
        self.menubar.setObjectName("menubar")
        ResultWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ResultWindow)
        self.statusbar.setObjectName("statusbar")
        ResultWindow.setStatusBar(self.statusbar)

        self.biblioteca_enfermidades.clicked.connect(self.button_biblioteca)

        self.retranslateUi(ResultWindow)
        QtCore.QMetaObject.connectSlotsByName(ResultWindow)


    def button_biblioteca(self):
        os.startfile("biblioteca.py")

    def retranslateUi(self, ResultWindow):
        _translate = QtCore.QCoreApplication.translate
        ResultWindow.setWindowTitle(_translate("ResultWindow", "Resultado BuiatricCare"))
        self.titulo.setText(_translate("ResultWindow", "Possibilidades e probabilidades diagnósticas"))
        self.enfermidade_1.setText(_translate("ResultWindow", "%s" %(lista_P_E[0][1])))
        self.probabilidade_1.setText(_translate("ResultWindow", ("%s" % (lista_P_E[0][0]))+(" %")))
        self.enfermidade_2.setText(_translate("ResultWindow", "%s" % (lista_P_E[1][1])))
        self.probabilidade_2.setText(_translate("ResultWindow", ("%s" % (lista_P_E[1][0]))+(" %")))
        self.enfermidade_3.setText(_translate("ResultWindow", "%s" % (lista_P_E[2][1])))
        self.probabilidade_3.setText(_translate("ResultWindow", ("%s" % (lista_P_E[2][0]))+(" %")))
        self.enfermidade_4.setText(_translate("ResultWindow", "%s" % (lista_P_E[3][1])))
        self.probabilidade_4.setText(_translate("ResultWindow", ("%s" % (lista_P_E[3][0]))+(" %")))
        self.enfermidade_5.setText(_translate("ResultWindow", "%s" % (lista_P_E[4][1])))
        self.probabilidade_5.setText(_translate("ResultWindow", ("%s" % (lista_P_E[4][0]))+(" %")))
        self.enfermidade_6.setText(_translate("ResultWindow", "%s" % (lista_P_E[5][1])))
        self.probabilidade_6.setText(_translate("ResultWindow", ("%s" % (lista_P_E[5][0]))+(" %")))
        self.enfermidade_7.setText(_translate("ResultWindow", "%s" % (lista_P_E[6][1])))
        self.probabilidade_7.setText(_translate("ResultWindow", ("%s" % (lista_P_E[6][0]))+(" %")))
        self.enfermidade_8.setText(_translate("ResultWindow", "%s" % (lista_P_E[7][1])))
        self.probabilidade_8.setText(_translate("ResultWindow", ("%s" % (lista_P_E[7][0]))+(" %")))
        self.enfermidade_9.setText(_translate("ResultWindow", "%s" % (lista_P_E[8][1])))
        self.probabilidade_9.setText(_translate("ResultWindow", ("%s" % (lista_P_E[8][0]))+(" %")))
        self.enfermidade_10.setText(_translate("ResultWindow", "%s" % (lista_P_E[9][1])))
        self.probabilidade_10.setText(_translate("ResultWindow", ("%s" % (lista_P_E[9][0]))+(" %")))
        self.enfermidade_11.setText(_translate("ResultWindow", "%s" % (lista_P_E[10][1])))
        self.probabilidade_11.setText(_translate("ResultWindow", ("%s" % (lista_P_E[10][0]))+(" %")))
        self.enfermidade_12.setText(_translate("ResultWindow", "%s" % (lista_P_E[11][1])))
        self.probabilidade_12.setText(_translate("ResultWindow", ("%s" % (lista_P_E[11][0]))+(" %")))
        self.enfermidade_14.setText(_translate("ResultWindow", "%s" % (lista_P_E[13][1])))
        self.probabilidade_14.setText(_translate("ResultWindow", ("%s" % (lista_P_E[13][0]))+(" %")))
        self.enfermidade_16.setText(_translate("ResultWindow", "%s" % (lista_P_E[15][1])))
        self.probabilidade_16.setText(_translate("ResultWindow", ("%s" % (lista_P_E[15][0]))+(" %")))
        self.enfermidade_17.setText(_translate("ResultWindow", "%s" % (lista_P_E[16][1])))
        self.probabilidade_17.setText(_translate("ResultWindow", ("%s" % (lista_P_E[16][0]))+(" %")))
        self.enfermidade_20.setText(_translate("ResultWindow", "%s" % (lista_P_E[19][1])))
        self.probabilidade_20.setText(_translate("ResultWindow", ("%s" % (lista_P_E[19][0]))+(" %")))
        self.enfermidade_22.setText(_translate("ResultWindow", "%s" % (lista_P_E[21][1])))
        self.probabilidade_22.setText(_translate("ResultWindow", ("%s" % (lista_P_E[21][0]))+(" %")))
        self.enfermidade_23.setText(_translate("ResultWindow", "%s" % (lista_P_E[22][1])))
        self.probabilidade_23.setText(_translate("ResultWindow", ("%s" % (lista_P_E[22][0]))+(" %")))
        self.enfermidade_24.setText(_translate("ResultWindow", "%s" % (lista_P_E[23][1])))
        self.probabilidade_24.setText(_translate("ResultWindow", ("%s" % (lista_P_E[23][0]))+(" %")))
        self.enfermidade_25.setText(_translate("ResultWindow", "%s" % (lista_P_E[24][1])))
        self.probabilidade_25.setText(_translate("ResultWindow", ("%s" % (lista_P_E[24][0]))+(" %")))
        self.enfermidade_26.setText(_translate("ResultWindow", "%s" % (lista_P_E[25][1])))
        self.probabilidade_26.setText(_translate("ResultWindow", ("%s" % (lista_P_E[25][0]))+(" %")))
        self.enfermidade_27.setText(_translate("ResultWindow", "%s" % (lista_P_E[26][1])))
        self.probabilidade_27.setText(_translate("ResultWindow", ("%s" % (lista_P_E[26][0]))+(" %")))
        self.enfermidade_28.setText(_translate("ResultWindow", "%s" % (lista_P_E[27][1])))
        self.probabilidade_28.setText(_translate("ResultWindow", ("%s" % (lista_P_E[27][0]))+(" %")))
        self.enfermidade_29.setText(_translate("ResultWindow", "%s" % (lista_P_E[28][1])))
        self.probabilidade_29.setText(_translate("ResultWindow", ("%s" % (lista_P_E[28][0]))+(" %")))
        self.enfermidade_30.setText(_translate("ResultWindow", "%s" % (lista_P_E[29][1])))
        self.probabilidade_30.setText(_translate("ResultWindow", ("%s" % (lista_P_E[29][0]))+(" %")))
        self.enfermidade_21.setText(_translate("ResultWindow", "%s" % (lista_P_E[20][1])))
        self.probabilidade_21.setText(_translate("ResultWindow", ("%s" % (lista_P_E[20][0]))+(" %")))
        self.enfermidade_19.setText(_translate("ResultWindow", "%s" % (lista_P_E[18][1])))
        self.probabilidade_19.setText(_translate("ResultWindow", ("%s" % (lista_P_E[18][0]))+(" %")))
        self.enfermidade_18.setText(_translate("ResultWindow", "%s" % (lista_P_E[17][1])))
        self.probabilidade_18.setText(_translate("ResultWindow", ("%s" % (lista_P_E[17][0]))+(" %")))
        self.enfermidade_15.setText(_translate("ResultWindow", "%s" % (lista_P_E[14][1])))
        self.probabilidade_15.setText(_translate("ResultWindow", ("%s" % (lista_P_E[14][0]))+(" %")))
        self.enfermidade_13.setText(_translate("ResultWindow", "%s" % (lista_P_E[12][1])))
        self.probabilidade_13.setText(_translate("ResultWindow", ("%s" % (lista_P_E[12][0]))+(" %")))
        self.biblioteca_enfermidades.setText(_translate("ResultWindow", "Biblioteca de enfermidades"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
