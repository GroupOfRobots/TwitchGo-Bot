from resource_gathering_ui import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow, QApplication, QListWidgetItem
from PySide2.QtGui import QBrush, QColor, QPalette, QPixmap
from PySide2.QtCore import Qt
import sys
from bonus_adding import BonusAdding
from Bonus import Bonus
from Time_Bonus import TimeBonus
from datetime import datetime, timedelta, date
import logging
from viewers_view import ViewersView
from chat_bot import ChatBot


class MainWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self._bonus_widwo = BonusAdding()
        self._score = (0, 0)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(162, 213, 198))
        self.setPalette(palette)
        self.setAutoFillBackground(True)
        self._current_item_first = None
        self._current_item_second = None
        self._current_item_general = None
        self._current_time_bonuses = [[1, datetime.now()], [1, datetime.now()]]
        self._bonuses = [Bonus('first bonus', -2, (1, 2)), Bonus('second bonus', 3, (4, 3)), TimeBonus('time_bonus', 2, (6, 7), .5)]
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._ui.score.setText(f'{self._score[0]} - {self._score[1]}')
        self._set_up_buttons()
        self._set_up_go_back_buttons()
        self._set_up_bonusses_list()
        self._ui.first_team_bonuses.setCurrentIndex(0)
        self._ui.second_team_bonuses.setCurrentIndex(0)
        self._ui.game_logo.setText("")
        self._ui.game_logo.setPixmap(QPixmap("logo.png"))
        self._ui.game_logo.setAlignment(Qt.AlignCenter)
        self._display_bonus_time_left()
        self._viewers_view = None

        today = date.today().strftime("%Y-%m-%d")

        logging.basicConfig(
            level=logging.DEBUG,
            format="[%(asctime)s] %(message)s",
            filename=f"logs/{today}.log"
        )

    def score(self):
        return self._score

    def set_score(self, new_score: tuple):
        self._score = new_score

    def bunuses(self):
        return self._bonuses

    def set_bunuses(self, new_bonuses: list):
        self._bonuses = new_bonuses

    def _set_up_bonusses_list(self):
        def custom_sort(bon):
            return bon.bonus_points()

        self._bonuses.sort(reverse=True, key=custom_sort)
        for bonus in self._bonuses:
            item = QListWidgetItem(self._create_bonus_description(bonus))
            item.bonus = bonus
            item.team_num = 0
            item_s = QListWidgetItem(self._create_bonus_description(bonus))
            item_s.bonus = bonus
            item_s.team_num = 1
            item_general = QListWidgetItem(self._create_bonus_description(bonus))
            item_general.bonus = bonus
            item.second_one = item_s
            item.general = item_general
            item_s.second_one = item
            item_s.general = item_general
            item_general.first_team = item
            item_general.second_team = item_s
            if bonus.bonus_points() < 0:
                item.setForeground(QBrush(QColor("Magenta")))
                item_s.setForeground(QBrush(QColor("Magenta")))
                item_general.setForeground(QBrush(QColor("Magenta")))

            self._ui.second_t_bonus_list.addItem(item_s)
            self._ui.first_t_bonus_list.addItem(item)
            self._ui.general_bonus_list.addItem(item_general)
        self._ui.first_t_bonus_list.itemClicked.connect(self._set_up_bonus_view_first)
        self._ui.second_t_bonus_list.itemClicked.connect(self._set_up_bonus_view_second)
        self._ui.general_bonus_list.itemClicked.connect(self._set_up_bonus_viem_general)

    def _add_goal_first(self):
        self._set_score((1, 0))

    def _add_goal_second(self):
        self._set_score((0, 1))

    def _sub_goal_first(self):
        if self._score[0] > 0:
            self._set_score((-1, 0))

    def _sub_goal_second(self):
        if self._score[1] > 0:
            self._set_score((0, -1))

    def _add_curent_bonus_first(self):
        self._viewers_view.add_bonus_for_first(self._current_item_first.bonus)
        if type(self._current_item_first.bonus) == TimeBonus:
            self._current_time_bonuses[0] = (self._current_item_first.bonus.bonus_points(), datetime.now() + timedelta(minutes=self._current_item_first.bonus.bonus_time()))
        else:
            self._set_score((self._current_item_first.bonus.bonus_points(), 0))
        self._ui.second_t_bonus_list.takeItem(self._ui.second_t_bonus_list.row(self._current_item_first.second_one))
        self._ui.first_t_bonus_list.takeItem(self._ui.first_t_bonus_list.row(self._current_item_first))
        self._ui.general_bonus_list.takeItem(self._ui.general_bonus_list.row(self._current_item_first.general))
        self._bonuses.remove(self._current_item_first.bonus)
        self._ui.first_team_bonuses.setCurrentIndex(0)

    def _add_curent_bonus_second(self):
        self._viewers_view.add_bonus_for_second(self._current_item_second.bonus)
        if type(self._current_item_second.bonus) == TimeBonus:
            self._current_time_bonuses[1] = (self._current_item_second.bonus.bonus_points(), datetime.now() + timedelta(minutes=self._current_item_second.bonus.bonus_time()))
        else:
            self._set_score((self._current_item_second.bonus.bonus_points(), 0))
        self._ui.first_t_bonus_list.takeItem(self._ui.first_t_bonus_list.row(self._current_item_second.second_one))
        self._ui.second_t_bonus_list.takeItem(self._ui.second_t_bonus_list.row(self._current_item_second))
        self._ui.general_bonus_list.takeItem(self._ui.general_bonus_list.row(self._current_item_second.general))
        self._bonuses.remove(self._current_item_second.bonus)
        self._ui.second_team_bonuses.setCurrentIndex(0)

    def _add_curent_bonus_general(self):
        self._viewers_view.add_bonus_for_first(self._current_item_general.bonus)
        self._viewers_view.add_bonus_for_second(self._current_item_general.bonus)
        if type(self._current_item_general.bonus) == TimeBonus:
            self._current_time_bonuses[1] = (self._current_item_general.bonus.bonus_points(), datetime.now() + timedelta(minutes=self._current_item_general.bonus.bonus_time()))
            self._current_time_bonuses[0] = (self._current_item_general.bonus.bonus_points(), datetime.now() + timedelta(minutes=self._current_item_general.bonus.bonus_time()))
        else:
            self._set_score((self._current_item_general.bonus.bonus_points(), self._current_item_general.bonus.bonus_points()))
        self._ui.second_t_bonus_list.takeItem(self._ui.second_t_bonus_list.row(self._current_item_general.second_team))
        self._ui.first_t_bonus_list.takeItem(self._ui.first_t_bonus_list.row(self._current_item_general.first_team))
        self._ui.general_bonus_list.takeItem(self._ui.general_bonus_list.row(self._current_item_general))
        self._bonuses.remove(self._current_item_general.bonus)
        self._ui.general_bonuses.setCurrentIndex(0)

    def _set_up_bonus_view_first(self, item):
        self._ui.first_team_bonuses.setCurrentIndex(1)
        bonus = item.bonus
        self._current_item_first = item
        self._ui.resource_description.setText(str(bonus))

    def _set_up_bonus_view_second(self, item):
        self._ui.second_team_bonuses.setCurrentIndex(1)
        bonus = item.bonus
        self._current_item_second = item
        self._ui.resource_description_2.setText(str(bonus))

    def _set_up_bonus_viem_general(self, item):
        self._ui.general_bonuses.setCurrentIndex(1)
        bonus = item.bonus
        self._current_item_general = item
        self._ui.bonus_desceiption_general.setText(str(bonus))

    def _create_bonus_description(self, bonus: Bonus):
        description = f'{bonus.name():15}'
        pos = str(bonus.position())
        description += f'{pos:8}'
        if type(bonus) == TimeBonus:
            description += '(t)'
        return description

    def _display_bonus_time_left(self):
        self._ui.bonus_time_first.setText(f'{(self._current_time_bonuses[0][1] -datetime.now()).seconds if self._current_time_bonuses[0][1] > datetime.now() else ""}')
        self._ui.bonus_time_second.setText(f'{(self._current_time_bonuses[1][1] -datetime.now()).seconds if self._current_time_bonuses[1][1] > datetime.now() else ""}')

    def _set_up_go_back_buttons(self):
        def _go_back_first():
            self._ui.first_team_bonuses.setCurrentIndex(0)

        def _go_back_second():
            self._ui.second_team_bonuses.setCurrentIndex(0)

        def _go_back_general():
            self._ui.general_bonuses.setCurrentIndex(0)

        self._ui.go_back_1.clicked.connect(_go_back_first)
        self._ui.go_back_2.clicked.connect(_go_back_second)
        self._ui.Go_back_general.clicked.connect(_go_back_general)

    def _set_score(self, score_to_add: tuple):
        if datetime.now() < self._current_time_bonuses[0][1]:
            score_to_add = (score_to_add[0] * self._current_time_bonuses[0][0], score_to_add[1])
        if datetime.now() < self._current_time_bonuses[1][1]:
            score_to_add = (score_to_add[0], score_to_add[1] * self._current_time_bonuses[1][0])
        self._score = (self._score[0]+score_to_add[0], self._score[1] + score_to_add[1])
        self._ui.score.setText(f'{self._score[0]} - {self._score[1]}')

    def _set_up_buttons(self):
        self._set_up_go_back_buttons()
        self._ui.add_goal_first.clicked.connect(self._add_goal_first)
        self._ui.add_goal_second.clicked.connect(self._add_goal_second)
        self._ui.subtract_goal_first.clicked.connect(self._sub_goal_first)
        self._ui.subtract_goal_second.clicked.connect(self._sub_goal_second)
        self._ui.add_resource_to_first.clicked.connect(self._add_curent_bonus_first)
        self._ui.add_resource_to_second.clicked.connect(self._add_curent_bonus_second)
        self._ui.add_bonus_all.clicked.connect(self._add_curent_bonus_general)
        self._ui.actionAdd_Bonus.triggered.connect(self._show_bonus_adding)
        self._bonus_widwo._ui.decision_buttons.accepted.connect(self._add_bonus)
        # button = self._bonus_widwo._ui.decision_buttons.button(QDialogButtonBox.Apply)
        # button.clicked.connect(self._add_goal_first)

    def _show_bonus_adding(self):
        self._bonus_widwo.show()

    def _add_bonus(self):
        name = self._bonus_widwo._ui.bonus_name.text()
        file_name = self._bonus_widwo._ui.file_name.text()
        bonus_vla = self._bonus_widwo._ui.bonus_value.value()
        position = (self._bonus_widwo._ui.position_x.value(), self._bonus_widwo._ui.position_y.value())
        if self._bonus_widwo._ui.ponus_creation.currentIndex() == 0:
            self._bonuses.append(Bonus(name, bonus_vla, position, file_name))
        else:
            bonus_time = self._bonus_widwo._ui.bonus_duration.value()
            self._bonuses.append(TimeBonus(name, bonus_vla, position, bonus_time, file_name))
        self._ui.second_t_bonus_list.clear()
        self._ui.first_t_bonus_list.clear()
        self._ui.general_bonus_list.clear()
        self._set_up_bonusses_list()

    def set_viewers_view(self, viewers_view: ViewersView):
        self._viewers_view = viewers_view


def gui_main(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    viewers_view = ViewersView(window)
    viewers_view.show()
    window.set_viewers_view(viewers_view)
    chat_bot = ChatBot(viewers_view.set_latest_votes,
                       viewers_view.get_latest_votes)
    chat_bot.run()

    while window.isVisible():
        viewers_view.run_window()
        window._display_bonus_time_left()
        app.processEvents()


if __name__ == "__main__":
    gui_main(sys.argv)
    # now = datetime.now()
    # now2 = datetime.now()
    # dif = now2 - now
    # print(dif.seconds)
