from viewers_view_ui import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow, QApplication, QListWidgetItem
import sys
from datetime import datetime
from time import sleep


class ViewersView(QMainWindow):
    def __init__(self, main_window, parent=None) -> None:
        super().__init__(parent=parent)
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._ui.score.setText('123')
        self._stylesheet = 'background-image: url("twitch_go.png");background-repeat:no-repeat;background-position:center;'
        self.setStyleSheet(self._stylesheet)
        self._main_window = main_window
        self._ui.bonus_time_first.setText("")
        self._ui.bonus_time_second.setText("")
        self._last_bonuses = [["", "", ""], ["", "", ""]]
        self._latest_votes = {"123": "456"}
        self._number_of_bonuses_on_display = 3
        self._display_last_votes()

    def run_window(self):
        score = f'{self._main_window._score[0]:2} : {self._main_window._score[1]:2}'
        self._ui.score.setText(score)
        self._ui.bonus_time_first.setText(f'{(self._main_window._current_time_bonuses[0][1] -datetime.now()).seconds if self._main_window._current_time_bonuses[0][1] > datetime.now() else ""}')
        self._ui.bonus_time_second.setText(f'{(self._main_window._current_time_bonuses[1][1] -datetime.now()).seconds if self._main_window._current_time_bonuses[1][1] > datetime.now() else ""}')
        self._display_previous_bonuses()

    def _display_previous_bonuses(self):
        self._ui.last_bonuses_first.clear()
        for bonus in self._last_bonuses[0]:
            item = QListWidgetItem(bonus)
            item.setText(bonus)
            self._ui.last_bonuses_first.addItem(item)

        self._ui.last_bonuses_second.clear()
        for bonus in self._last_bonuses[1]:
            item = QListWidgetItem(bonus)
            item.setText(bonus)
            self._ui.last_bonuses_second.addItem(item)

    def add_bonus_for_first(self, bonus):
        new_list = self._last_bonuses[0][1:self._number_of_bonuses_on_display]
        new_list.append(bonus.name())
        self._last_bonuses[0] = new_list

    def add_bonus_for_second(self, bonus):
        new_list = self._last_bonuses[1][1:self._number_of_bonuses_on_display]
        new_list.append(bonus.name())
        self._last_bonuses[1] = new_list

    def _display_last_votes(self):
        vote_string = ""
        for vote in self._latest_votes.keys():
            vote_string += f'{vote}: {self._latest_votes[vote]}\t'
        self._ui.votesl.setText(vote_string)

    def set_latest_votes(self, latest_votes: dict):
        self._latest_votes = latest_votes
        self._display_last_votes


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ViewersView()
    #window.setFixedSize(800, 600)
    window.show()

    window._ui.bonus_time_first.setText("")
    window._ui.bonus_time_second.setText("")

    line = None
    while window.isVisible():
        window.run_window()
        app.processEvents()
        sleep(0.2)
