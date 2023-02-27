# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewers_view.ui'
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_8 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.last_bonuses_first = QListWidget(self.centralwidget)
        self.last_bonuses_first.setObjectName(u"last_bonuses_first")
        self.last_bonuses_first.setMaximumSize(QSize(100, 100))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        brush2 = QBrush(QColor(0, 0, 0, 127))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        brush3 = QBrush(QColor(255, 255, 220, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
        brush4 = QBrush(QColor(255, 255, 255, 128))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.last_bonuses_first.setPalette(palette)

        self.verticalLayout_4.addWidget(self.last_bonuses_first)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.bonus_time_first = QLabel(self.centralwidget)
        self.bonus_time_first.setObjectName(u"bonus_time_first")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush5 = QBrush(QColor(255, 255, 0, 0))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        brush6 = QBrush(QColor(190, 190, 190, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        brush7 = QBrush(QColor(0, 0, 0, 128))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.bonus_time_first.setPalette(palette1)
        self.bonus_time_first.setStyleSheet(u"")
        self.bonus_time_first.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.bonus_time_first)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.score = QLabel(self.centralwidget)
        self.score.setObjectName(u"score")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.score.setPalette(palette2)
        font = QFont()
        font.setPointSize(36)
        self.score.setFont(font)

        self.verticalLayout_3.addWidget(self.score)

        self.verticalSpacer_4 = QSpacerItem(20, 264, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bonus_time_second = QLabel(self.centralwidget)
        self.bonus_time_second.setObjectName(u"bonus_time_second")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush8 = QBrush(QColor(85, 170, 255, 0))
        brush8.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush8)
        brush9 = QBrush(QColor(48, 140, 198, 0))
        brush9.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Highlight, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        brush10 = QBrush(QColor(145, 145, 145, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Disabled, QPalette.Highlight, brush10)
        self.bonus_time_second.setPalette(palette3)
        self.bonus_time_second.setStyleSheet(u"")
        self.bonus_time_second.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout.addWidget(self.bonus_time_second)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.last_bonuses_second = QListWidget(self.centralwidget)
        self.last_bonuses_second.setObjectName(u"last_bonuses_second")
        self.last_bonuses_second.setMaximumSize(QSize(100, 100))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush11 = QBrush(QColor(239, 239, 239, 0))
        brush11.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush11)
        brush12 = QBrush(QColor(255, 255, 255, 0))
        brush12.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Light, brush12)
        brush13 = QBrush(QColor(247, 247, 247, 0))
        brush13.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        brush14 = QBrush(QColor(119, 119, 119, 0))
        brush14.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush14)
        brush15 = QBrush(QColor(159, 159, 159, 0))
        brush15.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush15)
        brush16 = QBrush(QColor(0, 0, 0, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush16)
        palette4.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush16)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette4.setBrush(QPalette.Active, QPalette.Shadow, brush16)
        brush17 = QBrush(QColor(247, 247, 247, 127))
        brush17.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush17)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipBase, brush3)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipText, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette4.setBrush(QPalette.Inactive, QPalette.Light, brush12)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush16)
        palette4.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush16)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette4.setBrush(QPalette.Inactive, QPalette.Shadow, brush16)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush17)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush14)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette4.setBrush(QPalette.Disabled, QPalette.Light, brush12)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush14)
        palette4.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush14)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette4.setBrush(QPalette.Disabled, QPalette.Shadow, brush16)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush16)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.last_bonuses_second.setPalette(palette4)

        self.verticalLayout_7.addWidget(self.last_bonuses_second)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_6)


        self.horizontalLayout.addLayout(self.verticalLayout_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 216, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bonus_time_first.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.score.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.bonus_time_second.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

