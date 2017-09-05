# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ti.ui'
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

class Ui_frmTI(object):
    def setupUi(self, frmTI):
        frmTI.setObjectName(_fromUtf8("frmTI"))
        frmTI.resize(483, 422)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/bar-chart-up-3.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmTI.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(frmTI)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabla = QtGui.QTableWidget(frmTI)
        self.tabla.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tabla.setObjectName(_fromUtf8("tabla"))
        self.tabla.setColumnCount(0)
        self.tabla.setRowCount(0)
        self.gridLayout.addWidget(self.tabla, 1, 0, 1, 1)
        self.criterio = QtGui.QLineEdit(frmTI)
        self.criterio.setObjectName(_fromUtf8("criterio"))
        self.gridLayout.addWidget(self.criterio, 0, 0, 1, 1)

        self.retranslateUi(frmTI)
        QtCore.QMetaObject.connectSlotsByName(frmTI)

    def retranslateUi(self, frmTI):
        frmTI.setWindowTitle(_translate("frmTI", "Tipos Impositivos", None))

import ficheros_rc
