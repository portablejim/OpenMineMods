# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/InstanceWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InstanceWindow(object):
    def setupUi(self, InstanceWindow):
        InstanceWindow.setObjectName("InstanceWindow")
        InstanceWindow.resize(500, 400)
        InstanceWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(InstanceWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_mods = QtWidgets.QWidget()
        self.tab_mods.setObjectName("tab_mods")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_mods)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mod_scroll = QtWidgets.QScrollArea(self.tab_mods)
        self.mod_scroll.setWidgetResizable(True)
        self.mod_scroll.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.mod_scroll.setObjectName("mod_scroll")
        self.fjhgdsf_2 = QtWidgets.QWidget()
        self.fjhgdsf_2.setGeometry(QtCore.QRect(0, 0, 458, 301))
        self.fjhgdsf_2.setObjectName("fjhgdsf_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.fjhgdsf_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.mod_box = QtWidgets.QVBoxLayout()
        self.mod_box.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.mod_box.setObjectName("mod_box")
        self.verticalLayout_5.addLayout(self.mod_box)
        self.mod_scroll.setWidget(self.fjhgdsf_2)
        self.verticalLayout_2.addWidget(self.mod_scroll)
        self.tabWidget.addTab(self.tab_mods, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pack_search = QtWidgets.QLineEdit(self.frame)
        self.pack_search.setObjectName("pack_search")
        self.horizontalLayout_4.addWidget(self.pack_search)
        self.pack_search_button = QtWidgets.QToolButton(self.frame)
        icon = QtGui.QIcon.fromTheme("search")
        self.pack_search_button.setIcon(icon)
        self.pack_search_button.setObjectName("pack_search_button")
        self.horizontalLayout_4.addWidget(self.pack_search_button)
        self.verticalLayout_3.addWidget(self.frame)
        self.browse_scroll = QtWidgets.QScrollArea(self.tab)
        self.browse_scroll.setWidgetResizable(True)
        self.browse_scroll.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.browse_scroll.setObjectName("browse_scroll")
        self.fjhgdsf_3 = QtWidgets.QWidget()
        self.fjhgdsf_3.setGeometry(QtCore.QRect(0, 0, 458, 248))
        self.fjhgdsf_3.setObjectName("fjhgdsf_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.fjhgdsf_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.loading_label = QtWidgets.QLabel(self.fjhgdsf_3)
        self.loading_label.setAlignment(QtCore.Qt.AlignCenter)
        self.loading_label.setObjectName("loading_label")
        self.verticalLayout_6.addWidget(self.loading_label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.browse_scroll.setWidget(self.fjhgdsf_3)
        self.verticalLayout_3.addWidget(self.browse_scroll)
        self.tabWidget.addTab(self.tab, "")
        self.tab_info = QtWidgets.QWidget()
        self.tab_info.setObjectName("tab_info")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_info)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pack_version = QtWidgets.QLabel(self.tab_info)
        self.pack_version.setObjectName("pack_version")
        self.verticalLayout_8.addWidget(self.pack_version)
        self.pack_pack = QtWidgets.QLabel(self.tab_info)
        self.pack_pack.setObjectName("pack_pack")
        self.verticalLayout_8.addWidget(self.pack_pack)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem1)
        self.pack_update = QtWidgets.QPushButton(self.tab_info)
        self.pack_update.setObjectName("pack_update")
        self.verticalLayout_8.addWidget(self.pack_update)
        self.tabWidget.addTab(self.tab_info, "")
        self.verticalLayout.addWidget(self.tabWidget)
        InstanceWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(InstanceWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        InstanceWindow.setMenuBar(self.menubar)

        self.retranslateUi(InstanceWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(InstanceWindow)

    def retranslateUi(self, InstanceWindow):
        _translate = QtCore.QCoreApplication.translate
        InstanceWindow.setWindowTitle(_translate("InstanceWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mods), _translate("InstanceWindow", "Installed Mods"))
        self.pack_search_button.setText(_translate("InstanceWindow", "..."))
        self.loading_label.setText(_translate("InstanceWindow", "Loading..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("InstanceWindow", "Browse Mods"))
        self.pack_version.setText(_translate("InstanceWindow", "TextLabel"))
        self.pack_pack.setText(_translate("InstanceWindow", "TextLabel"))
        self.pack_update.setText(_translate("InstanceWindow", "Check For Updates"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_info), _translate("InstanceWindow", "Info"))

