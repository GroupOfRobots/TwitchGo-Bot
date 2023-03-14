# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bonus_adding_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.create_regular = QPushButton(Dialog)
        self.create_regular.setObjectName(u"create_regular")

        self.horizontalLayout.addWidget(self.create_regular)

        self.create_time = QPushButton(Dialog)
        self.create_time.setObjectName(u"create_time")

        self.horizontalLayout.addWidget(self.create_time)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.file_name = QLineEdit(Dialog)
        self.file_name.setObjectName(u"file_name")
        self.file_name.setDragEnabled(True)

        self.verticalLayout.addWidget(self.file_name)

        self.bonus_name = QLineEdit(Dialog)
        self.bonus_name.setObjectName(u"bonus_name")

        self.verticalLayout.addWidget(self.bonus_name)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.bonus_value = QSpinBox(Dialog)
        self.bonus_value.setObjectName(u"bonus_value")
        self.bonus_value.setMinimum(-10)
        self.bonus_value.setMaximum(10)

        self.horizontalLayout_3.addWidget(self.bonus_value)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.position_y = QSpinBox(Dialog)
        self.position_y.setObjectName(u"position_y")
        self.position_y.setMaximum(200)

        self.horizontalLayout_2.addWidget(self.position_y)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.position_x = QSpinBox(Dialog)
        self.position_x.setObjectName(u"position_x")
        self.position_x.setMaximum(200)

        self.horizontalLayout_2.addWidget(self.position_x)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.ponus_creation = QStackedWidget(Dialog)
        self.ponus_creation.setObjectName(u"ponus_creation")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.ponus_creation.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.bonus_duration = QDoubleSpinBox(self.page_2)
        self.bonus_duration.setObjectName(u"bonus_duration")

        self.horizontalLayout_4.addWidget(self.bonus_duration)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 46, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.ponus_creation.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.ponus_creation)

        self.decision_buttons = QDialogButtonBox(Dialog)
        self.decision_buttons.setObjectName(u"decision_buttons")
        self.decision_buttons.setOrientation(Qt.Horizontal)
        self.decision_buttons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.decision_buttons)


        self.retranslateUi(Dialog)
        self.decision_buttons.accepted.connect(Dialog.accept)
        self.decision_buttons.rejected.connect(Dialog.reject)

        self.ponus_creation.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.create_regular.setText(QCoreApplication.translate("Dialog", u"Regular Bonus", None))
        self.create_time.setText(QCoreApplication.translate("Dialog", u"Time Bonus", None))
        self.file_name.setInputMask("")
        self.file_name.setText(QCoreApplication.translate("Dialog", u"Enter filename", None))
        self.bonus_name.setText(QCoreApplication.translate("Dialog", u"Enter name", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Bonus value", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Position X", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Position Y", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Bonus duration [s]", None))
    # retranslateUi

