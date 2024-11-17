from resource_gathering_ui import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow, QApplication, QListWidgetItem
from bonus_adding import BonusAdding
from ui_helpers import create_bonus_item

class MainWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.bonus_window = BonusAdding(self)
        self.bonuses = []
        self.score = (0, 0)
        self.current_time_bonuses = [None, None]

        self.setup_ui()

    def setup_ui(self):
        self.ui.actionAdd_Bonus.triggered.connect(self.show_bonus_adding)
        self.ui.add_goal_first.clicked.connect(lambda: self.update_score((1, 0)))
        self.ui.add_goal_second.clicked.connect(lambda: self.update_score((0, 1)))
        self.ui.subtract_goal_first.clicked.connect(lambda: self.update_score((-1, 0)))
        self.ui.subtract_goal_second.clicked.connect(lambda: self.update_score((0, -1)))

    def show_bonus_adding(self):
        if self.bonus_window.exec_() == QDialog.Accepted:
            new_bonus = self.bonus_window.get_bonus_data()
            self.add_bonus(new_bonus)

    def add_bonus(self, bonus):
        self.bonuses.append(bonus)
        self.refresh_bonus_list()

    def refresh_bonus_list(self):
        self.ui.first_t_bonus_list.clear()
        self.ui.second_t_bonus_list.clear()
        self.ui.general_bonus_list.clear()

        for bonus in self.bonuses:
            item_first = create_bonus_item(bonus, team_num=1)
            item_second = create_bonus_item(bonus, team_num=2)
            item_general = create_bonus_item(bonus)

            self.ui.first_t_bonus_list.addItem(item_first)
            self.ui.second_t_bonus_list.addItem(item_second)
            self.ui.general_bonus_list.addItem(item_general)

    def update_score(self, score_delta):
        self.score = tuple(map(sum, zip(self.score, score_delta)))
        self.ui.score.setText(f"{self.score[0]} - {self.score[1]}")