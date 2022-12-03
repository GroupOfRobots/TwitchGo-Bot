from resource_gathering_ui import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow, QApplication, QListWidgetItem
import sys
from functools import partial
from Bonus import Bonus


class MainWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self._score = (0, 0)
        self._curent_bonus = None
        self._bonuses = [Bonus('first bonus', -2, (1, 2)), Bonus('second bonus', 3, (4, 3))]
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._ui.score.setText(f'{self._score[0]} - {self._score[1]}')
        self._ui.add_goal_first.clicked.connect(self._add_goal_first)
        self._ui.add_goal_second.clicked.connect(self._add_goal_second)
        self._ui.subtract_goal_first.clicked.connect(self._sub_goal_first)
        self._ui.subtract_goal_second.clicked.connect(self._sub_goal_second)
        self._set_up_go_back_buttons()
        self._set_up_bonusses_list()

    def score(self):
        return self._score

    def set_score(self, new_score: tuple):
        self._score = new_score

    def bunuses(self):
        return self._bonuses

    def set_bunuses(self, new_bonuses: list):
        self._bonuses = new_bonuses

    def _set_up_bonusses_list(self):
        for bonus in self._bonuses:
            item = QListWidgetItem(str(bonus))
            item.bonus = bonus
            item.team_num = 0
            item_s = QListWidgetItem(str(bonus))
            item_s.bonus = bonus
            item_s.team_num = 1
            item.second_one = item_s
            item_s.second_one = item
            self._ui.second_t_bonus_list.addItem(item_s)
            self._ui.first_t_bonus_list.addItem(item)
        self._ui.first_t_bonus_list.itemClicked.connect(self._set_up_bonus_view_first)
        self._ui.second_t_bonus_list.itemClicked.connect(self._set_up_bonus_view_second)
        # self._ui.add_resource_to_first.clicked.connect(self._add_curent_bonus_first)
        # self._ui.add_resource_to_second.clicked.connect(self._add_curent_bonus_second)

    def _add_goal_first(self):
        self._score = (self._score[0]+1, self._score[1])
        self._ui.score.setText(f'{self._score[0]} - {self._score[1]}')

    def _add_goal_second(self):
        self._score = (self._score[0], self._score[1]+1)
        self._ui.score.setText(f'{self._score[0]} - {self._score[1]}')

    def _sub_goal_first(self):
        if self._score[0] > 0:
            self._score = (self._score[0]-1, self._score[1])
            self._ui.score.setText(f'{self._score[0]} - {self._score[1]}')

    def _sub_goal_second(self):
        if self._score[1] > 0:
            self._score = (self._score[0], self._score[1]-1)
            self._ui.score.setText(f'{self._score[0]} - {self._score[1]}')

    def _add_curent_bonus_first(self):
        self._score = (self._score[0]+self._curent_bonus.bonus_points(), self._score[1])
        self._ui.score.setText(f'{self._score[0]} - {self._score[1]}')

    def _add_curent_bonus_second(self):
        self._score = (self._score[0], self._score[1]+self._curent_bonus.bonus_points())
        self._ui.score.setText(f'{self._score[0]} - {self._score[1]}')

    def _set_up_bonus_view_first(self, item):
        self._ui.first_team_bonuses.setCurrentIndex(1)
        bonus = item.bonus
        self._curent_bonus = bonus
        self._ui.resource_description.setText(self._create_bonus_description(bonus))

    def _set_up_bonus_view_second(self, item):
        self._ui.second_team_bonuses.setCurrentIndex(1)
        bonus = item.bonus
        self._curent_bonus = bonus
        self._ui.resource_description_2.setText(self._create_bonus_description(bonus))

    def _create_bonus_description(self, bonus: Bonus):
        description = bonus.name()
        description += f'\nPosition: {bonus.position()}'
        description += f'\nAdded points: {bonus.bonus_points()}'
        return description

    def _set_up_go_back_buttons(self):
        def _go_back_first():
            self._ui.first_team_bonuses.setCurrentIndex(0)

        def _go_back_second():
            self._ui.second_team_bonuses.setCurrentIndex(0)

        self._ui.go_back_1.clicked.connect(_go_back_first)
        self._ui.go_back_2.clicked.connect(_go_back_second)


def gui_main(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    return app.exec_()


if(__name__ == "__main__"):
    gui_main(sys.argv)
    print('a')
