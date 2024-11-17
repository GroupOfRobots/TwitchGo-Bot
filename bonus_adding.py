from PySide2.QtWidgets import QDialog
from bonus_adding_ui import Ui_Dialog
from Bonus import Bonus
from Time_Bonus import TimeBonus


class BonusAdding(QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setup_signals()

    def setup_signals(self):
        self.ui.create_regular.clicked.connect(lambda: self.ui.ponus_creation.setCurrentIndex(0))
        self.ui.create_time.clicked.connect(lambda: self.ui.ponus_creation.setCurrentIndex(1))

    def get_bonus_data(self):
        name = self.ui.bonus_name.text()
        file_name = self.ui.file_name.text()
        value = self.ui.bonus_value.value()
        position = (self.ui.position_x.value(), self.ui.position_y.value())

        if self.ui.ponus_creation.currentIndex() == 0:
            return Bonus(name, value, position, file_name)
        else:
            bonus_time = self.ui.bonus_duration.value()
            return TimeBonus(name, value, position, bonus_time, file_name)