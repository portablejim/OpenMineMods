# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(635, 466)
        icon = QtGui.QIcon.fromTheme("minecraft")
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mainTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.mainTabs.setObjectName("mainTabs")
        self.tab_instances = QtWidgets.QWidget()
        self.tab_instances.setObjectName("tab_instances")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_instances)
        self.verticalLayout.setObjectName("verticalLayout")
        self.instance_scroll = QtWidgets.QScrollArea(self.tab_instances)
        self.instance_scroll.setWidgetResizable(True)
        self.instance_scroll.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.instance_scroll.setObjectName("instance_scroll")
        self.fjhgdsf = QtWidgets.QWidget()
        self.fjhgdsf.setGeometry(QtCore.QRect(0, 0, 593, 341))
        self.fjhgdsf.setObjectName("fjhgdsf")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.fjhgdsf)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.instance_box = QtWidgets.QVBoxLayout()
        self.instance_box.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.instance_box.setObjectName("instance_box")
        self.verticalLayout_4.addLayout(self.instance_box)
        self.instance_scroll.setWidget(self.fjhgdsf)
        self.verticalLayout.addWidget(self.instance_scroll)
        self.mainTabs.addTab(self.tab_instances, "")
        self.tab_browse = QtWidgets.QWidget()
        self.tab_browse.setObjectName("tab_browse")
        self.mainTabs.addTab(self.tab_browse, "")
        self.tab_settings = QtWidgets.QWidget()
        self.tab_settings.setObjectName("tab_settings")
        self.mainTabs.addTab(self.tab_settings, "")
        self.verticalLayout_2.addWidget(self.mainTabs)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 635, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.mainTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.tab_instances), _translate("MainWindow", "Instances"))
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.tab_browse), _translate("MainWindow", "Browse Packs"))
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.tab_settings), _translate("MainWindow", "Settings"))

