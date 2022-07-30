# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialoglOuwwp.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sgtk
from sgtk.platform.qt import QtCore, QtGui

navigation = sgtk.platform.import_framework("tk-framework-qtwidgets", "navigation")
search_widget = sgtk.platform.import_framework("tk-framework-qtwidgets", "search_widget")
BreadcrumbWidget = navigation.BreadcrumbWidget
NavigationWidget = navigation.NavigationWidget
SearchWidget = search_widget.SearchWidget


class Ui_Dialog_AliyunOSS(object):
    def setupUi(self, Dialog_AliyunOSS):
        if not Dialog_AliyunOSS.objectName():
            Dialog_AliyunOSS.setObjectName(u"Dialog_AliyunOSS")
        Dialog_AliyunOSS.resize(875, 340)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog_AliyunOSS)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.top_layout = QtGui.QVBoxLayout()
        self.top_layout.setSpacing(8)
        self.top_layout.setObjectName(u"top_layout")

        self.nav_layout = QtGui.QGridLayout()
        self.nav_widget = NavigationWidget(Dialog_AliyunOSS)
        self.nav_widget.setObjectName("nav_widget")
        self.nav_layout.addWidget(self.nav_widget, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.nav_layout.addItem(spacerItem, 0, 1, 1, 1)
        self.nav_layout.setColumnStretch(2, 1)
        self.top_layout.addLayout(self.nav_layout)

        self.breadcrumb_widget = BreadcrumbWidget(Dialog_AliyunOSS)
        self.breadcrumb_widget.setObjectName("breadcrumb_widget")
        self.top_layout.addWidget(self.breadcrumb_widget)

        self.verticalLayout_2.addLayout(self.top_layout)

        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.search = SearchWidget
        self.search.setFixedWidth(QtGui.QWidget(300))
        self.search.set_placeholder_text(u"Search items....")

        self.treeView_hierarchy = QtGui.QTreeView(Dialog_AliyunOSS)
        self.treeView_hierarchy.setObjectName(u"treeView_hierarchy")

        self.horizontalLayout.addWidget(self.treeView_hierarchy)

        self.listView_task = QtGui.QListView(Dialog_AliyunOSS)
        self.listView_task.setObjectName(u"listView_task")

        self.horizontalLayout.addWidget(self.listView_task)

        self.verticalLayout_publish = QtGui.QVBoxLayout()
        self.verticalLayout_publish.setObjectName(u"verticalLayout_publish")
        self.label_publish = QtGui.QLabel(Dialog_AliyunOSS)
        self.label_publish.setObjectName(u"label_publish")

        self.verticalLayout_publish.addWidget(self.label_publish)

        self.listView_publishfiles = QtGui.QListView(Dialog_AliyunOSS)
        self.listView_publishfiles.setObjectName(u"listView_publishfiles")
        self.listView_publishfiles.setEnabled(True)

        self.verticalLayout_publish.addWidget(self.listView_publishfiles)

        self.horizontalLayout.addLayout(self.verticalLayout_publish)

        self.verticalLayout_work = QtGui.QVBoxLayout()
        self.verticalLayout_work.setObjectName(u"verticalLayout_work")
        self.label_work = QtGui.QLabel(Dialog_AliyunOSS)
        self.label_work.setObjectName(u"label_work")

        self.verticalLayout_work.addWidget(self.label_work)

        self.listView_workfiles = QtGui.QListView(Dialog_AliyunOSS)
        self.listView_workfiles.setObjectName(u"listView_workfiles")

        self.verticalLayout_work.addWidget(self.listView_workfiles)

        self.horizontalLayout.addLayout(self.verticalLayout_work)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog_AliyunOSS)

        QtCore.QMetaObject.connectSlotsByName(Dialog_AliyunOSS)

    # setupUi

    def retranslateUi(self, Dialog_AliyunOSS):
        Dialog_AliyunOSS.setWindowTitle(QtGui.QApplication.translate("Dialog_AliyunOSS", u"Report a bug!", None))
        self.label_publish.setText(QtGui.QApplication.translate("Dialog_AliyunOSS", u"PublishFiles", None))
        self.label_work.setText(QtGui.QApplication.translate("Dialog_AliyunOSS", u"WorkFiles", None))
    # retranslateUi
