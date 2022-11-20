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

        self.resource_view = QStackedWidget(self.centralwidget)
        self.resource_view.setObjectName(u"resource_view")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.choose_resource = QLabel(self.page)
        self.choose_resource.setObjectName(u"choose_resource")
        self.choose_resource.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.choose_resource)

        self.resource_view.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_3 = QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.resource_name = QLabel(self.page_2)
        self.resource_name.setObjectName(u"resource_name")

        self.verticalLayout_3.addWidget(self.resource_name)

        self.resource_description = QLabel(self.page_2)
        self.resource_description.setObjectName(u"resource_description")

        self.verticalLayout_3.addWidget(self.resource_description)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.add_resource_to_first = QPushButton(self.page_2)
        self.add_resource_to_first.setObjectName(u"add_resource_to_first")
        palette = QPalette()
        brush = QBrush(QColor(255, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        self.add_resource_to_first.setPalette(palette)
        self.add_resource_to_first.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.add_resource_to_first)

        self.add_resource_to_second = QPushButton(self.page_2)
        self.add_resource_to_second.setObjectName(u"add_resource_to_second")
        palette1 = QPalette()
        brush1 = QBrush(QColor(0, 85, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        self.add_resource_to_second.setPalette(palette1)
        self.add_resource_to_second.setCursor(QCursor(Qt.SizeBDiagCursor))

        self.horizontalLayout_2.addWidget(self.add_resource_to_second)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.resource_view.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.resource_view)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.score = QLabel(self.centralwidget)
        self.score.setObjectName(u"score")
        font = QFont()
        font.setPointSize(20)
        self.score.setFont(font)
        self.score.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.score)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.add_goal_second = QPushButton(self.centralwidget)
        self.add_goal_second.setObjectName(u"add_goal_second")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        self.add_goal_second.setPalette(palette2)
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.add_goal_second.setFont(font1)
        self.add_goal_second.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_goal_second.setAutoFillBackground(True)

        self.gridLayout.addWidget(self.add_goal_second, 0, 1, 1, 1)

        self.add_goal_first = QPushButton(self.centralwidget)
        self.add_goal_first.setObjectName(u"add_goal_first")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Button, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush)
        self.add_goal_first.setPalette(palette3)
        self.add_goal_first.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.add_goal_first, 0, 0, 1, 1)

        self.subtract_goal_first = QPushButton(self.centralwidget)
        self.subtract_goal_first.setObjectName(u"subtract_goal_first")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Button, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush)
        self.subtract_goal_first.setPalette(palette4)
        self.subtract_goal_first.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.subtract_goal_first, 1, 0, 1, 1)

        self.subtract_goal_second = QPushButton(self.centralwidget)
        self.subtract_goal_second.setObjectName(u"subtract_goal_second")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        self.subtract_goal_second.setPalette(palette5)
        self.subtract_goal_second.setCursor(QCursor(Qt.PointingHandCursor))

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

        self.resource_view.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAdd_Bonus.setText(QCoreApplication.translate("MainWindow", u"Add Bonus", None))
        self.game_logo.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.choose_resource.setText(QCoreApplication.translate("MainWindow", u"Choose Resource", None))
        self.resource_name.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.resource_description.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.add_resource_to_first.setText(QCoreApplication.translate("MainWindow", u"Add resource", None))
        self.add_resource_to_second.setText(QCoreApplication.translate("MainWindow", u"Add resource", None))
        self.score.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.add_goal_second.setText(QCoreApplication.translate("MainWindow", u"Add Goal", None))
        self.add_goal_first.setText(QCoreApplication.translate("MainWindow", u"Add Goal", None))
        self.subtract_goal_first.setText(QCoreApplication.translate("MainWindow", u"Subtract", None))
        self.subtract_goal_second.setText(QCoreApplication.translate("MainWindow", u"Subtract", None))
        self.menuAdd_Bonus.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
    # retranslateUi

