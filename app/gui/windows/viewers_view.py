# app/gui/windows/viewers_view.py

from PySide6.QtWidgets import QMainWindow, QListWidgetItem
import os
from PySide6.QtGui import QBrush, QColor, QPalette, QPixmap, QPainter
from PySide6.QtCore import Qt, QTimer
from app.gui.ui.viewers_view_ui import Ui_MainWindow
from app.core.traps.trap import Trap
from app.utils.logger import setup_logging
import logging
from datetime import datetime

class ViewersView(QMainWindow):
    def __init__(self, main_window, parent=None) -> None:
        super().__init__(parent=parent)
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._ui.score.setText('0 - 0')
        # self.setStyleSheet('background-image: url("assets/images/picture.png");background-repeat:no-repeat;background-position:center;background-size: cover;')
        self.set_background_image("assets/images/picture.png")
        self._main_window = main_window
        self.setAutoFillBackground(True)

        self._last_bonuses = [["", "", ""], ["", "", ""]]
        self._number_of_bonuses_on_display = 3
        self._latest_votes = {}


        self._setup_logging()
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

    def _display_last_votes(self, votes_string: str = ""): 
        self._ui.votesl.setText(votes_string)

    def _update_score(self):
        """Refresh the score display from the host's ScoreManager."""
        score = self._main_window._score_manager.get_score()
        self._ui.score.setText(f"{score[0]} - {score[1]}")

    def set_background_image(self, image_path):
        # palette = QPalette()
        # pixmap = QPixmap(image_path)

        # scaled_pixmap = pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        # palette.setBrush(QPalette.Window, QBrush(scaled_pixmap))
        # self.setPalette(palette)
        # self.setAutoFillBackground(True)

        self.background_pixmap = QPixmap(image_path)
        self.update()  # Trigger paintEvent


    def paintEvent(self, event):
        super().paintEvent(event)  # Call base class paintEvent
        if hasattr(self, 'background_pixmap'):
            painter = QPainter(self)
            scaled = self.background_pixmap.scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            painter.drawPixmap(0, 0, scaled)
