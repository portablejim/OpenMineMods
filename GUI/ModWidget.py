# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/ModWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ModWidget(object):
    def setupUi(self, ModWidget):
        ModWidget.setObjectName("ModWidget")
        ModWidget.resize(400, 41)
        self.horizontalLayout = QtWidgets.QHBoxLayout(ModWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mod_name = QtWidgets.QLabel(ModWidget)
        self.mod_name.setObjectName("mod_name")
        self.horizontalLayout.addWidget(self.mod_name)
        self.mod_info = QtWidgets.QToolButton(ModWidget)
        icon = QtGui.QIcon.fromTheme("info")
        self.mod_info.setIcon(icon)
        self.mod_info.setObjectName("mod_info")
        self.horizontalLayout.addWidget(self.mod_info)
        self.mod_install = QtWidgets.QToolButton(ModWidget)
        icon = QtGui.QIcon.fromTheme("down")
        self.mod_install.setIcon(icon)
        self.mod_install.setObjectName("mod_install")
        self.horizontalLayout.addWidget(self.mod_install)
        self.mod_delete = QtWidgets.QToolButton(ModWidget)
        icon = QtGui.QIcon.fromTheme("edit-delete")
        self.mod_delete.setIcon(icon)
        self.mod_delete.setObjectName("mod_delete")
        self.horizontalLayout.addWidget(self.mod_delete)

        self.retranslateUi(ModWidget)
        QtCore.QMetaObject.connectSlotsByName(ModWidget)

    def retranslateUi(self, ModWidget):
        _translate = QtCore.QCoreApplication.translate
        ModWidget.setWindowTitle(_translate("ModWidget", "Form"))
        self.mod_name.setText(_translate("ModWidget", "TextLabel"))
        self.mod_info.setText(_translate("ModWidget", "..."))
        self.mod_install.setText(_translate("ModWidget", "..."))
        self.mod_delete.setText(_translate("ModWidget", "..."))

