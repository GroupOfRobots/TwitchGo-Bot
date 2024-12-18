# app/gui/ui/bonus_adding_ui.py

from PySide6.QtCore import Qt, QRect
from PySide6.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QSpinBox, QDoubleSpinBox,
    QStackedWidget, QDialogButtonBox, QGridLayout
)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.horizontalLayout = QHBoxLayout()

        self.create_regular = QPushButton("Regular Bonus", Dialog)
        self.horizontalLayout.addWidget(self.create_regular)

        self.create_time = QPushButton("Time Bonus", Dialog)
        self.horizontalLayout.addWidget(self.create_time)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.bonus_name_label = QLabel("Bonus Name:", Dialog)
        self.verticalLayout.addWidget(self.bonus_name_label)

        self.bonus_name = QLineEdit(Dialog)
        self.verticalLayout.addWidget(self.bonus_name)

        self.bonus_value_label = QLabel("Bonus Value:", Dialog)
        self.verticalLayout.addWidget(self.bonus_value_label)

        self.bonus_value = QSpinBox(Dialog)
        self.bonus_value.setMinimum(-10)
        self.bonus_value.setMaximum(10)
        self.verticalLayout.addWidget(self.bonus_value)

        self.position_label = QLabel("Position (X, Y):", Dialog)
        self.verticalLayout.addWidget(self.position_label)

        self.position_layout = QHBoxLayout()
        self.position_x = QSpinBox(Dialog)
        self.position_x.setMaximum(200)
        self.position_y = QSpinBox(Dialog)
        self.position_y.setMaximum(200)
        self.position_layout.addWidget(self.position_x)
        self.position_layout.addWidget(self.position_y)
        self.verticalLayout.addLayout(self.position_layout)

        self.file_name_label = QLabel("Texture File:", Dialog)
        self.verticalLayout.addWidget(self.file_name_label)

        self.file_name = QLineEdit(Dialog)
        self.verticalLayout.addWidget(self.file_name)

        self.bonus_creation = QStackedWidget(Dialog)
        self.page_regular = QWidget()
        self.bonus_creation.addWidget(self.page_regular)

        self.page_time = QWidget()
        self.time_layout = QVBoxLayout(self.page_time)
        self.bonus_duration_label = QLabel("Bonus Duration (seconds):", self.page_time)
        self.bonus_duration = QDoubleSpinBox(self.page_time)
        self.bonus_duration.setMinimum(1)
        self.bonus_duration.setMaximum(3600)
        self.time_layout.addWidget(self.bonus_duration_label)
        self.time_layout.addWidget(self.bonus_duration)
        self.bonus_creation.addWidget(self.page_time)

        self.verticalLayout.addWidget(self.bonus_creation)

        self.decision_buttons = QDialogButtonBox(Dialog)
        self.decision_buttons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.verticalLayout.addWidget(self.decision_buttons)

        self.bonus_creation.setCurrentIndex(0)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("Add Bonus")
