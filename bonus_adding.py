from bonus_adding_ui import Ui_Dialog
from PySide2.QtWidgets import QDialog


class BonusAdding(QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._ui = Ui_Dialog()
        self._ui.setupUi(self)

    def show(self) -> None:
        self._ui.bonus_duration.setValue(0)
        self._ui.bonus_value.setValue(0)
        self._ui.position_x.setValue(0)
        self._ui.position_y.setValue(0)
        self._ui.file_name.setText("Enter filename")
        self._ui.file_name.setText("Enter name")
        return super().show()
