# app/gui/windows/viewers_view.py

from PySide6.QtWidgets import QMainWindow, QListWidgetItem
import os
from PySide6.QtGui import QBrush, QColor
from PySide6.QtCore import Qt, QTimer
from app.gui.ui.viewers_view_ui import Ui_MainWindow
from app.core.traps.trap import Trap
from app.utils.logger import setup_logging
import logging
import random
import time
from datetime import datetime

class ViewersView(QMainWindow):
    def __init__(self, main_window, parent=None) -> None:
        super().__init__(parent=parent)
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._ui.score.setText('0 - 0')
        self.setStyleSheet('background-image: url("assets/images/picture.png");background-repeat:no-repeat;background-position:center;background-size: cover;')
        self._main_window = main_window

        self._last_bonuses = [["", "", ""], ["", "", ""]]
        self._number_of_bonuses_on_display = 3
        self._latest_votes = {}

        self._available_traps = [
            Trap("white"),
            Trap("yellow"),
            Trap("orange"),
            Trap("violet")
        ]

        self._setup_logging()
        self._choose_random_traps(3)

        # Periodically update score display to reflect host panel changes
        self._score_timer = QTimer(self)
        self._score_timer.timeout.connect(self._update_score)
        self._score_timer.start(200)

    def _setup_logging(self):
        today = datetime.today().strftime("%Y-%m-%d")
        log_path = os.path.join("logs", f"{today}.log")
        setup_logging(log_path)

    def run_window(self):
        self._display_previous_bonuses()
        self._display_last_votes()

    def _display_previous_bonuses(self):
        # Implement this method to display the previous bonuses
        pass

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
        # Sort traps by vote count descending
        sorted_traps = sorted(
            self._latest_votes.values(),
            key=lambda t: len(t.votes),   # lub: key=lambda t: len(t.get_votes())
            reverse=True
        )
        for trap in sorted_traps:
            vote_string += f"{str(trap)}    "
        self._ui.votesl.setText(vote_string)

    def set_latest_votes(self, latest_votes: dict):
        self._latest_votes = latest_votes
        self._display_last_votes()

    def get_latest_votes(self) -> dict:
        return self._latest_votes

    def _choose_random_traps(self, number_of_traps: int):
        traps = random.sample(self._available_traps, number_of_traps)
        traps_dict = {trap.name: trap for trap in traps}
        self.set_latest_votes(traps_dict)

    def _clear_votes(self):
        for trap in self._available_traps:
            trap.clear_votes()

    def _run_trap_with_most_votes(self):
        max_votes = 0
        winning_traps = []

        for trap in self._latest_votes.values():
            vote_count = len(trap.votes)
            if vote_count > max_votes:
                max_votes = vote_count

        for trap in self._latest_votes.values():
            if len(trap.votes) == max_votes:
                winning_traps.append(trap)

        if winning_traps:
            selected_trap = random.choice(winning_traps)
            selected_trap.run()

    def _finish_voting(self):
        self._run_trap_with_most_votes()
        self._choose_random_traps(self._number_of_traps_on_display)
        self._clear_votes()

    def _update_score(self):
        """Refresh the score display from the host's ScoreManager."""
        score = self._main_window._score_manager.get_score()
        self._ui.score.setText(f"{score[0]} - {score[1]}")
