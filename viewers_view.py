from viewers_view_ui import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow, QApplication, QListWidgetItem
import sys
from datetime import datetime
import time
import random
from trap import Trap


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
        self._number_of_bonuses_on_display = 3
        self._latest_votes = {}
        self._available_traps = [Trap("trap1"), Trap("trap2"), Trap("trap3"),
                                 Trap("trap4"), Trap("trap5"), Trap("trap6")]
        self._display_last_votes()
        self._time_start = int(time.time())
        self._time_between_commands = 10
        self._number_of_traps_on_display = 3
        self._choose_random_traps(self._number_of_traps_on_display)

    def run_window(self):
        if (int(time.time()) - self._time_start) > self._time_between_commands:
            self._time_start = int(time.time())
            self._finish_voting()

        score = f'{self._main_window._score[0]:2} : {self._main_window._score[1]:2}'
        self._ui.score.setText(score)
        self._ui.bonus_time_first.setText(f'{(self._main_window._current_time_bonuses[0][1] -datetime.now()).seconds if self._main_window._current_time_bonuses[0][1] > datetime.now() else ""}')
        self._ui.bonus_time_second.setText(f'{(self._main_window._current_time_bonuses[1][1] -datetime.now()).seconds if self._main_window._current_time_bonuses[1][1] > datetime.now() else ""}')
        self._display_previous_bonuses()
        self._display_last_votes()

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
            vote_string += f'{vote}: {len(self._latest_votes[vote].get_votes)}\t'
        self._ui.votesl.setText(vote_string)

    def set_latest_votes(self, latest_votes: dict):
        self._latest_votes = latest_votes
        self._display_last_votes

    def _choose_random_traps(self, number_of_traps):
        traps = random.sample(self._available_traps, number_of_traps)
        traps_dict = {}

        for trap in traps:
            traps_dict[trap.get_name] = trap

        self.set_latest_votes(traps_dict)

    def get_latest_votes(self):
        return self._latest_votes

    def _clear_votes(self):
        for trap in self._available_traps:
            trap.clear_votes()

    def _run_trap_with_most_votes(self):
        max_votes = 0
        winning_traps = []

        for trap_name in self._latest_votes.keys():
            trap = self._latest_votes[trap_name]
            max_votes = max(max_votes, len(trap.get_votes))

        for trap_name in self._latest_votes.keys():
            trap = self._latest_votes[trap_name]

            if len(trap.get_votes) == max_votes:
                winning_traps.append(trap)

        random.choice(winning_traps).run()

    def _finish_voting(self):
        self._run_trap_with_most_votes()
        self._choose_random_traps(self._number_of_traps_on_display)
        self._clear_votes()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ViewersView()
    # window.setFixedSize(800, 600)
    window.show()

    window._ui.bonus_time_first.setText("")
    window._ui.bonus_time_second.setText("")

    line = None
    while window.isVisible():
        window.run_window()
        app.processEvents()
        time.sleep(0.2)
