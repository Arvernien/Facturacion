# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/facturacion.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        MainWindow.resize(1098, 763)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/calculator-solid.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8("QWidget#centralwidget {\n"
"    background: white;\n"
"}\n"
"QPushButton {\n"
"    border: 1px solid rgb(143, 212, 0);\n"
"    border-radius: 3px;\n"
"    background: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0.5, stop:0 rgba(143, 212, 0, 100), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QMenu {\n"
"    background-color: #ABABAB; /* sets background of the menu */\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    border: 1px solid grey;\n"
"    color: black;\n"
"    selection-background-color: rgba(143, 212, 0, 100);\n"
"    selection-color: black;\n"
"}\n"
"QTableWidget QHeaderView::section {\n"
"    background: white;\n"
"    border: 1px outset rgb(143,212,0);\n"
"\n"
"}\n"
"QTableWidget QHeaderView::section:checked\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0.5, stop:0 rgba(143, 212, 0, 100), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTableWidget QHeaderView::down-arrow {\n"
"    height: 5px;\n"
"    width: 5px;\n"
"    image: url(:/img/desplegado.png);\n"
"}\n"
"\n"
"QTableWidget QHeaderView::up-arrow {\n"
"    image: url(:/img/nodesplegado.png);\n"
"}\n"
"QTableWidget QTableCornerButton::section {\n"
"    background: white;\n"
"    border: 1px outset rgb(143,212,0);\n"
"}"))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(0, 30))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.but_open = QtGui.QPushButton(self.widget)
        self.but_open.setMinimumSize(QtCore.QSize(30, 30))
        self.but_open.setMaximumSize(QtCore.QSize(30, 30))
        self.but_open.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/carpeta.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_open.setIcon(icon1)
        self.but_open.setObjectName(_fromUtf8("but_open"))
        self.horizontalLayout.addWidget(self.but_open)
        self.pushButton_3 = QtGui.QPushButton(self.widget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_3.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/23-512.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.line = QtGui.QFrame(self.widget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.but_Calcular = QtGui.QPushButton(self.widget)
        self.but_Calcular.setMinimumSize(QtCore.QSize(30, 30))
        self.but_Calcular.setMaximumSize(QtCore.QSize(30, 30))
        self.but_Calcular.setText(_fromUtf8(""))
        self.but_Calcular.setIcon(icon)
        self.but_Calcular.setObjectName(_fromUtf8("but_Calcular"))
        self.horizontalLayout.addWidget(self.but_Calcular)
        self.but_TI = QtGui.QPushButton(self.widget)
        self.but_TI.setMinimumSize(QtCore.QSize(30, 30))
        self.but_TI.setMaximumSize(QtCore.QSize(30, 30))
        self.but_TI.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/bar-chart-up-3.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_TI.setIcon(icon3)
        self.but_TI.setObjectName(_fromUtf8("but_TI"))
        self.horizontalLayout.addWidget(self.but_TI)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(_fromUtf8("QTabWidget::pane {\n"
"    border-top: 1px solid rgb(143,212,0);\n"
"}\n"
"QTabBar::tab {\n"
"    border: 1px solid rgb(143,212,0);\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    background: rgb(200,200,200);\n"
"    padding-left: 5px;\n"
"    width:50;\n"
"}\n"
"QTabBar::tab:hover{\n"
"    border: 1px solid rgb(143,212,0);\n"
"    background: white;\n"
"    height: 27px;\n"
"}\n"
"QTabBar::tab:selected{\n"
"    border: 1px solid rgb(143,212,0);\n"
"    background: white;\n"
"    height: 27px;\n"
"}\n"
"QTabBar::tab:!selected{\n"
"    border: 1px solid rgb(143,212,0);\n"
"    margin-top: 2px;\n"
"    height: 25px;\n"
"}\n"
"QTabBar::scroller{\n"
"    height: 25px;\n"
"    width:15px;\n"
"}\n"
"QTabBar QToolButton {\n"
"    border: 1px solid rgb(143,212,0);\n"
"    background-color: white;\n"
"    height: 25px;    \n"
"}\n"
"QTabBar QToolButton::right-arrow {\n"
"    image: url(:/img/recogido.png);\n"
"}\n"
"QTabBar QToolButton::left-arrow {\n"
"    image: url(:/img/norecogido.png);\n"
"}\n"
"QWidget#tabSalida {\n"
"    border: 1px solid rgb(143,212,0);\n"
"}\n"
"QWidget#tabEntrada {\n"
"    border: 1px solid rgb(143,212,0);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border-top: 1px solid grey;\n"
"    border-right: 0px solid grey;\n"
"    border-bottom: 0px;\n"
"    border-left: 0px solid grey;\n"
"    background: #D3D3D3;\n"
"    height: 18px;\n"
"    margin: 0px 22px 0px 22px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    border-top: 0px;\n"
"    border-right: 1px solid grey;\n"
"    border-bottom: 0px;\n"
"    border-left: 1px solid grey;\n"
"    background: white;\n"
"    min-width: 20px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border-top: 1px solid grey;\n"
"    border-bottom: 0px;\n"
"    border-left: 1px solid grey;\n"
"    border-right: 1px solid grey;\n"
"    background: white;\n"
"    width: 20px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border-top: 1px solid grey;\n"
"    border-bottom: 0px;\n"
"    border-right: 1px solid grey;\n"
"    background:white;\n"
"    width: 21px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar:left-arrow:horizontal {\n"
"    width: 8px;\n"
"    height: 8px;\n"
"    background: white;\n"
"    color: grey;\n"
"    image: url(:/img/norecogido.png);\n"
"}\n"
" QScrollBar::right-arrow:horizontal {\n"
"    width: 8px;\n"
"    height: 8px;\n"
"    background: white;\n"
"    color: grey;\n"
"    image: url(:/img/recogido.png);\n"
"}\n"
"QScrollBar:vertical {\n"
"    border-top: 0px solid grey;\n"
"    border-right: 0px solid grey;\n"
"    border-bottom: 0px;\n"
"    border-left: 1px solid grey;\n"
"    background:  #D3D3D3;\n"
"    width: 18px;\n"
"    margin: 22px 0px 22px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    border-top: 1px solid grey;\n"
"    border-right: 0px solid grey;\n"
"    border-bottom: 1px solid grey;\n"
"    border-left: 0px solid grey;\n"
"    background: white;\n"
"    min-height: 20px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border-top: 1px solid grey;\n"
"    border-bottom: 1px solid grey;\n"
"    border-left: 1px solid grey;\n"
"    border-right: 0px solid grey;\n"
"    background: white;\n"
"    height: 20px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border-top: 0px solid grey;\n"
"    border-bottom: 1px solid grey;\n"
"    border-left: 1px solid grey;\n"
"    background:white;\n"
"    height: 21px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar:up-arrow:vertical {\n"
"    width: 8px;\n"
"    height: 8px;\n"
"    background: white;\n"
"    color: grey;\n"
"    image: url(:/img/nodesplegado.png);\n"
"}\n"
" QScrollBar::down-arrow:vertical {\n"
"    width: 8px;\n"
"    height: 8px;\n"
"    background: white;\n"
"    color: grey;\n"
"    image: url(:/img/desplegado.png);\n"
"}"))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabEntrada = QtGui.QWidget()
        self.tabEntrada.setObjectName(_fromUtf8("tabEntrada"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tabEntrada)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabla = QtGui.QTableWidget(self.tabEntrada)
        self.tabla.setStyleSheet(_fromUtf8(""))
        self.tabla.setObjectName(_fromUtf8("tabla"))
        self.tabla.setColumnCount(0)
        self.tabla.setRowCount(0)
        self.verticalLayout.addWidget(self.tabla)
        self.tabWidget.addTab(self.tabEntrada, _fromUtf8(""))
        self.tabSalida = QtGui.QWidget()
        self.tabSalida.setObjectName(_fromUtf8("tabSalida"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tabSalida)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label = QtGui.QLabel(self.tabSalida)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.selectorPerfiles = QtGui.QComboBox(self.tabSalida)
        self.selectorPerfiles.setMinimumSize(QtCore.QSize(103, 22))
        self.selectorPerfiles.setStyleSheet(_fromUtf8("QComboBox {\n"
"    border: 2px solid rgb(143,212,0);\n"
"    border-radius: 5px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"    color: dark grey;\n"
"    font-weight: bold;\n"
"}\n"
"QComboBox#selectorPerfiles:editable {\n"
"    background: darkgrey;\n"
"}\n"
"\n"
"QComboBox#selectorPerfiles:!editable, QComboBox::drop-down:editable {\n"
"     background: white;\n"
"    \n"
"}\n"
"\n"
"QComboBox#selectorPerfiles:on { /* shift the text when the popup opens */\n"
"    background: darkgrey;\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox#selectorPerfiles::drop-down {\n"
"    font-weight: light;\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: rgb(143,212,0);\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox#selectorPerfiles::down-arrow {\n"
"    image: url(:/img/desplegado.png);\n"
"}"))
        self.selectorPerfiles.setObjectName(_fromUtf8("selectorPerfiles"))
        self.horizontalLayout_2.addWidget(self.selectorPerfiles)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tabla_2 = QtGui.QTableWidget(self.tabSalida)
        self.tabla_2.setObjectName(_fromUtf8("tabla_2"))
        self.tabla_2.setColumnCount(0)
        self.tabla_2.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tabla_2)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabSalida, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1098, 20))
        self.menubar.setMinimumSize(QtCore.QSize(0, 20))
        self.menubar.setStyleSheet(_fromUtf8("QMenuBar {\n"
"    background-color:white;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    spacing: 3px; /* spacing between menu bar items */\n"
"    padding: 2px 4px;\n"
"    background: transparent;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QMenuBar::item:selected { /* when selected using mouse or keyboard */\n"
"    background: rgb(143,212,0);\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"    background: #888888;\n"
"}\n"
"QMenu {\n"
"    background-color: white; /* sets background of the menu */\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"QMenu::item {\n"
"    /* sets background of menu item. set this to something non-transparent\n"
"        if you want menu color and menu item color to be different */\n"
"    background-color: white;\n"
"}\n"
"\n"
"QMenu::item:selected { /* when user selects item using mouse or keyboard */\n"
"    color: black;\n"
"    background-color:  qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0.5, stop:0 rgba(143, 212, 0, 100), stop:1 rgba(255, 255, 255, 255));;\n"
"}"))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMen = QtGui.QMenu(self.menubar)
        self.menuMen.setObjectName(_fromUtf8("menuMen"))
        self.menuExportar = QtGui.QMenu(self.menubar)
        self.menuExportar.setObjectName(_fromUtf8("menuExportar"))
        MainWindow.setMenuBar(self.menubar)
        self.actionAdministrar_perfiles = QtGui.QAction(MainWindow)
        self.actionAdministrar_perfiles.setObjectName(_fromUtf8("actionAdministrar_perfiles"))
        self.actionCargar_Excel_de_Facturaci_n = QtGui.QAction(MainWindow)
        self.actionCargar_Excel_de_Facturaci_n.setObjectName(_fromUtf8("actionCargar_Excel_de_Facturaci_n"))
        self.actionImportar_datos_desde_FIN_de_Retorno = QtGui.QAction(MainWindow)
        self.actionImportar_datos_desde_FIN_de_Retorno.setEnabled(False)
        self.actionImportar_datos_desde_FIN_de_Retorno.setObjectName(_fromUtf8("actionImportar_datos_desde_FIN_de_Retorno"))
        self.actionImportar_Fichero_de_carga = QtGui.QAction(MainWindow)
        self.actionImportar_Fichero_de_carga.setEnabled(False)
        self.actionImportar_Fichero_de_carga.setObjectName(_fromUtf8("actionImportar_Fichero_de_carga"))
        self.actionA_Excel_de_facturaci_n = QtGui.QAction(MainWindow)
        self.actionA_Excel_de_facturaci_n.setObjectName(_fromUtf8("actionA_Excel_de_facturaci_n"))
        self.actionGenerar_Access_para_BET = QtGui.QAction(MainWindow)
        self.actionGenerar_Access_para_BET.setVisible(False)
        self.actionGenerar_Access_para_BET.setObjectName(_fromUtf8("actionGenerar_Access_para_BET"))
        self.actionImportar_Access_Valores = QtGui.QAction(MainWindow)
        self.actionImportar_Access_Valores.setObjectName(_fromUtf8("actionImportar_Access_Valores"))
        self.menuMen.addAction(self.actionCargar_Excel_de_Facturaci_n)
        self.menuMen.addAction(self.actionImportar_datos_desde_FIN_de_Retorno)
        self.menuMen.addAction(self.actionImportar_Fichero_de_carga)
        self.menuMen.addAction(self.actionImportar_Access_Valores)
        self.menuExportar.addAction(self.actionA_Excel_de_facturaci_n)
        self.menuExportar.addSeparator()
        self.menuExportar.addAction(self.actionGenerar_Access_para_BET)
        self.menubar.addAction(self.menuMen.menuAction())
        self.menubar.addAction(self.menuExportar.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Facturación catastro", None))
        self.but_open.setToolTip(_translate("MainWindow", "Abrir excel para facturación", None))
        self.pushButton_3.setToolTip(_translate("MainWindow", "Aplicar perfil seleccionado", None))
        self.but_Calcular.setToolTip(_translate("MainWindow", "Calcular", None))
        self.but_TI.setToolTip(_translate("MainWindow", "Ver tipos impositivos", None))
        self.tabla.setSortingEnabled(True)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabEntrada), _translate("MainWindow", "Entrada", None))
        self.label.setText(_translate("MainWindow", "Perfil:", None))
        self.tabla_2.setSortingEnabled(True)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSalida), _translate("MainWindow", "Cálculo", None))
        self.menuMen.setTitle(_translate("MainWindow", "Archivo", None))
        self.menuExportar.setTitle(_translate("MainWindow", "Exportar", None))
        self.actionAdministrar_perfiles.setText(_translate("MainWindow", "Administrar perfiles", None))
        self.actionCargar_Excel_de_Facturaci_n.setText(_translate("MainWindow", "Cargar Excel de Facturación", None))
        self.actionImportar_datos_desde_FIN_de_Retorno.setText(_translate("MainWindow", "Importar FIN de Retorno", None))
        self.actionImportar_datos_desde_FIN_de_Retorno.setShortcut(_translate("MainWindow", "Ctrl+F", None))
        self.actionImportar_Fichero_de_carga.setText(_translate("MainWindow", "Importar Fichero de carga", None))
        self.actionA_Excel_de_facturaci_n.setText(_translate("MainWindow", "A Excel de facturación", None))
        self.actionGenerar_Access_para_BET.setText(_translate("MainWindow", "Generar Access para BET", None))
        self.actionImportar_Access_Valores.setText(_translate("MainWindow", "Importar Access Valores", None))

import ficheros_rc
