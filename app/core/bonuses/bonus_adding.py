# app/gui/windows/bonus_adding.py

from PySide6.QtWidgets import QDialog
from app.gui.ui.bonus_adding_ui import Ui_Dialog

class BonusAdding(QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._ui = Ui_Dialog()
        self._ui.setupUi(self)
        self._set_up_bonus_choice()

    def show(self) -> None:
        self._ui.bonus_creation.setCurrentIndex(0)
        self._ui.bonus_duration.setValue(0)
        self._ui.bonus_value.setValue(0)
        self._ui.position_x.setValue(0)
        self._ui.position_y.setValue(0)
        self._ui.file_name.setText("")
        self._ui.bonus_name.setText("")
        return super().show()

    def _set_up_bonus_choice(self):
        self._ui.create_regular.clicked.connect(self._change_to_regular)
        self._ui.create_time.clicked.connect(self._change_to_time)

    def _change_to_time(self):
        self._ui.bonus_creation.setCurrentIndex(1)

    def _change_to_regular(self):
        self._ui.bonus_creation.setCurrentIndex(0)
