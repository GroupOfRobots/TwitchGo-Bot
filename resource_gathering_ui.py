# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'resource_gathering_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionAdd_Bonus = QAction(MainWindow)
        self.actionAdd_Bonus.setObjectName(u"actionAdd_Bonus")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.game_logo = QLabel(self.centralwidget)
        self.game_logo.setObjectName(u"game_logo")

        self.verticalLayout.addWidget(self.game_logo)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.resources_list = QListWidget(self.centralwidget)
        self.resources_list.setObjectName(u"resources_list")

        self.horizontalLayout.addWidget(self.resources_list)

        self.resources_view = QScrollArea(self.centralwidget)
        self.resources_view.setObjectName(u"resources_view")
        self.resources_view.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 385, 434))
        self.resources_view.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.resources_view)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.score = QLabel(self.centralwidget)
        self.score.setObjectName(u"score")
        self.score.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.score)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.add_goal_second = QPushButton(self.centralwidget)
        self.add_goal_second.setObjectName(u"add_goal_second")

        self.gridLayout.addWidget(self.add_goal_second, 0, 1, 1, 1)

        self.add_goal_first = QPushButton(self.centralwidget)
        self.add_goal_first.setObjectName(u"add_goal_first")

        self.gridLayout.addWidget(self.add_goal_first, 0, 0, 1, 1)

        self.subtract_goal_first = QPushButton(self.centralwidget)
        self.subtract_goal_first.setObjectName(u"subtract_goal_first")

        self.gridLayout.addWidget(self.subtract_goal_first, 1, 0, 1, 1)

        self.subtract_goal_second = QPushButton(self.centralwidget)
        self.subtract_goal_second.setObjectName(u"subtract_goal_second")

        self.gridLayout.addWidget(self.subtract_goal_second, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 20))
        self.menuAdd_Bonus = QMenu(self.menubar)
        self.menuAdd_Bonus.setObjectName(u"menuAdd_Bonus")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAdd_Bonus.menuAction())
        self.menuAdd_Bonus.addAction(self.actionAdd_Bonus)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAdd_Bonus.setText(QCoreApplication.translate("MainWindow", u"Add Bonus", None))
        self.game_logo.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.score.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.add_goal_second.setText(QCoreApplication.translate("MainWindow", u"Add Goal", None))
        self.add_goal_first.setText(QCoreApplication.translate("MainWindow", u"Add Goal", None))
        self.subtract_goal_first.setText(QCoreApplication.translate("MainWindow", u"Subtract", None))
        self.subtract_goal_second.setText(QCoreApplication.translate("MainWindow", u"Subtract", None))
        self.menuAdd_Bonus.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
    # retranslateUi

