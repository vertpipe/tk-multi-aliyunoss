#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author : reliable-天
# @Contact : U{johnny.zxt@gmail.com<johnny.zxt@gmail.com>}
# @Website : http://zxto.top:1580
# @Gitlab  : http://zxto.top:30000
# @Time : 2022/7/18 23:40
# @File : aliyun_ossdialog.py
# @Description :

import sgtk
import os
import sys
import threading
import tempfile
import re

# by importing QT from sgtk rather than directly, we ensure that
# the code will be compatible with both PySide and PyQt.
from sgtk.platform.qt import QtCore, QtGui
from .ui.ui_dialog import Ui_Dialog_AliyunOSS

# screen_grab = sgtk.platform.import_framework("tk-framework-qtwidgets", "screen_grab")
# shotgun_fields = sgtk.platform.import_framework("tk-framework-qtwidgets", "shotgun_fields")
navigation = sgtk.platform.import_framework("tk-framework-qtwidgets", "navigation")
shotgun_model = sgtk.platform.import_framework("tk-framework-shotgunutils", "shotgun_model")
task_manager = sgtk.platform.import_framework("tk-framework-shotgunutils", "task_manager")


def show_dialog(app_instance):
    """
    Shows the main dialog window.
    """
    app_instance.engine.show_dialog("Aliyun OSS Sync", app_instance, AliyunOSSAPPDialog)


class AliyunOSSAPPDialog(QtGui.QWidget):
    """
    Main application dialog window
    """

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_Dialog_AliyunOSS()
        self.ui.setupUi(self)

        self._app = sgtk.platform.current_bundle()
        self._bg_task_manager = task_manager.BackgroundTaskManager(self)

        self._navigating = False

        self.project = self._app.context.project
        self._hierarchy_model = shotgun_model.SimpleShotgunHierarchyModel(
            self, bg_task_manager=self._bg_task_manager
        )
        # 排序
        self._hierarchy_proxy_model = QtGui.QSortFilterProxyModel(self)
        self._hierarchy_proxy_model.setDynamicSortFilter(True)
        # 把 proxy_model 的源设置为 hierarchy model
        self._hierarchy_proxy_model.setSourceModel(self._hierarchy_model)

        self.ui.treeView_hierarchy.setModel(self._hierarchy_proxy_model)
        self.ui.treeView_hierarchy.header().hide()
        self.ui.treeView_hierarchy.setSortingEnabled(True)
        self.ui.treeView_hierarchy.sortByColumn(0, QtCore.Qt.AscendingOrder)

        self._hierarchy_model.load_data('PublishedFile.entity',root=self.project)
        # TODO 添加顶部浏览 ui
        # hierarchy 的选择
        selection_model = self.ui.treeView_hierarchy.selectionModel()
        selection_model.selectionChanged.connect(self._on_hierachy_selection_changed)

        self.ui.search.search_edited.connect(self._on_search_edited)
        self.ui.search.search_changed.connect(self._on_search_changed)

    def destroy(self):
        self._bg_task_manager.shut_down()

    def _on_hierachy_selection_changed(self, selected, deselected):
        indexes = selected.indexes()
        if not indexes:
            return

        selected_item = self._hierarchy_model.itemFromIndex(
            self._hierarchy_proxy_model.mapToSource(indexes[0])
        )

        label = _get_item_label(selected_item)

        if not self._navigating:
            self.ui.nav_widget.add_destination(label, selected_item)
        crumbs = [_HierarchyItemBreadcrumb(selected_item)]

        cur_item = selected_item
        while cur_item.parent() is not None:
            parent = cur_item.parent()
            crumbs.insert(0, _HierarchyItemBreadcrumb(parent))
            cur_item = parent
        self.ui.breadcrumb_widget.set(crumbs)

    def _on_navigate(self, item):
        self._navigating = True
        proxy_index = self._hierarchy_proxy_model.mapFromSource(item.index())
        self.ui.tree_view.selectionModel().select(
            proxy_index, QtGui.QItemSelectionModel.ClearAndSelect
        )
        self._navigating = False

    def _on_home_clicked(self):
        self.ui.tree_view.selectionModel().clearSelection()
        self.ui.breadcrumb_widget.set([])

    def _on_search_edited(self):
        pass

    def _on_search_changed(self):
        pass

class _HierarchyItemBreadcrumb(navigation.Breadcrumb):
    def __init__(self, item):
        self._item = item
        label = _get_item_label(item)
        super(_HierarchyItemBreadcrumb, self).__init__(label)

    def item(self):
        return self._item

def _get_item_label(item):
    """Get a display label for a SG hierarchy item."""

    if item.kind() == "entity":
        label = "<strong>%s</strong> %s" % (item.entity_type(), item.text())
    else:
        label = item.text()

    return label
