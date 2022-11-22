from resource_gathering_ui import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow, QApplication, QListWidgetItem
import sys
from Bonus import Bonus


class MainWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self._score = (0, 0)
        self._curent_bonus = None
        self._bonuses = [Bonus('first bonus', 2, (1, 2)), Bonus('second bonus', 3, (4, 3))]
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._ui.score.setText(f'{self._score[0]} - {self._score[1]}')
        self._ui.add_goal_first.clicked.connect(self._add_goal_first)
        self._ui.add_goal_second.clicked.connect(self._add_goal_second)
        self._ui.subtract_goal_first.clicked.connect(self._sub_goal_first)
        self._ui.subtract_goal_second.clicked.connect(self._sub_goal_second)
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
            self._ui.resources_list.addItem(item)
        self._ui.resources_list.itemClicked.connect(self._set_up_bonus_view)
        self._ui.add_resource_to_first.clicked.connect(self._add_curent_bonus_first)
        self._ui.add_resource_to_second.clicked.connect(self._add_curent_bonus_second)

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

    def _set_up_bonus_view(self, item):
        self._ui.resource_view.setCurrentIndex(1)
        bonus = item.bonus
        self._curent_bonus = bonus
        self._ui.resource_description.setText(self._create_bonus_description(bonus))

    def _create_bonus_description(self, bonus: Bonus):
        description = bonus.name()
        description += f'\nPosition: {bonus.position()}'
        description += f'\nAdded points: {bonus.bonus_points()}'
        return description


def gui_main(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    return app.exec_()


if(__name__ == "__main__"):
    gui_main(sys.argv)
    print('a')
