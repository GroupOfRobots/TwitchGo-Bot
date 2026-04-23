# app/gui/windows/main_window.py

from typing import Optional

from PySide6.QtWidgets import QMainWindow, QApplication, QListWidgetItem
from PySide6.QtGui import QBrush, QColor, QPalette, QPixmap
from PySide6.QtCore import Qt, QTimer
from app.gui.ui.resource_gathering_ui import Ui_MainWindow
from app.core.bonuses.bonus import Bonus
from app.core.bonuses.time_bonus import TimeBonus
from app.core.traps.board_manager import board_manager
from app.core.scoring.score_manager import ScoreManager
from app.gui.windows.bonus_adding import BonusAdding
from app.utils.logger import setup_logging
from datetime import datetime, timedelta
import os

class MainWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self._bonus_window = BonusAdding()
        self._score_manager = ScoreManager()
        self._setup_logging()
        self._initialize_bonuses()  # Move this line before _initialize_ui()
        self._initialize_ui()
        self._initialize_chat_bot()
        #self._initialize_ros()

        # Setup QTimer for periodic UI updates
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._update_ui)
        self._timer.start(200)  # Update every 200 ms

    def _setup_logging(self):
        today = datetime.today().strftime("%Y-%m-%d")
        log_path = os.path.join("logs", f"{today}.log")
        setup_logging(log_path)

    def _initialize_ui(self):
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._ui.score.setText(f'{self._score_manager.get_score()[0]} - {self._score_manager.get_score()[1]}')
        self._set_up_buttons()
        self._set_up_go_back_buttons()
        self._set_up_bonuses_list()
        self._ui.first_team_bonuses.setCurrentIndex(0)
        self._ui.second_team_bonuses.setCurrentIndex(0)
        self._ui.game_logo.setPixmap(QPixmap("assets/images/logo.png"))
        self._ui.game_logo.setAlignment(Qt.AlignCenter)
        self._display_bonus_time_left()
        self._viewers_view = None

    def set_viewers_view(self, viewers_view):
        self._viewers_view = viewers_view

    def _initialize_bonuses(self):
        self._current_time_bonuses = [[1, datetime.now()], [1, datetime.now()]]
        self._bonuses = [
            Bonus('first bonus', -2, (1, 2)),
            Bonus('second bonus', 3, (4, 3)),
            TimeBonus('time_bonus', 2, (6, 7), 30.0)  # Sample time bonus
        ]

    def _initialize_chat_bot(self):
        """Here we could initialize the chat bot, but it's not necessary for this exercise"""
        pass

    # def _initialize_ros(self):
    #     # Initialize ROS in a separate thread
    #     import threading
    #     from app.ros.ros_main import main as ros_main
    #     ros_thread = threading.Thread(target=ros_main, daemon=True)
    #     ros_thread.start()

    def _set_up_buttons(self):
        self._ui.add_goal_first.clicked.connect(self._add_goal_first)
        self._ui.add_goal_second.clicked.connect(self._add_goal_second)
        self._ui.subtract_goal_first.clicked.connect(self._sub_goal_first)
        self._ui.subtract_goal_second.clicked.connect(self._sub_goal_second)
        self._ui.add_resource_to_first.clicked.connect(self._add_current_bonus_first)
        self._ui.add_resource_to_second.clicked.connect(self._add_current_bonus_second)
        self._ui.add_bonus_all.clicked.connect(self._add_current_bonus_general)
        self._ui.throw_ball_button.clicked.connect(self._throw_ball_button)
        self._ui.actionAdd_Bonus.triggered.connect(self._show_bonus_adding)
        self._bonus_window._ui.decision_buttons.accepted.connect(self._add_bonus)

    def _set_up_go_back_buttons(self):
        self._ui.go_back_1.clicked.connect(lambda: self._ui.first_team_bonuses.setCurrentIndex(0))
        self._ui.go_back_2.clicked.connect(lambda: self._ui.second_team_bonuses.setCurrentIndex(0))
        self._ui.Go_back_general.clicked.connect(lambda: self._ui.general_bonuses.setCurrentIndex(0))

    def _set_up_bonuses_list(self):
        self._bonuses.sort(reverse=True, key=lambda bon: bon.bonus_points())
        for bonus in self._bonuses:
            item = QListWidgetItem(self._create_bonus_description(bonus))
            item.bonus = bonus
            item.team_num = 0
            item_s = QListWidgetItem(self._create_bonus_description(bonus))
            item_s.bonus = bonus
            item_s.team_num = 1
            item_general = QListWidgetItem(self._create_bonus_description(bonus))
            item_general.bonus = bonus
            item_general.team_num = None

            if bonus.bonus_points() < 0:
                magenta_brush = QBrush(QColor("Magenta"))
                item.setForeground(magenta_brush)
                item_s.setForeground(magenta_brush)
                item_general.setForeground(magenta_brush)

            self._ui.second_t_bonus_list.addItem(item_s)
            self._ui.first_t_bonus_list.addItem(item)
            self._ui.general_bonus_list.addItem(item_general)

        self._ui.first_t_bonus_list.itemClicked.connect(self._set_up_bonus_view_first)
        self._ui.second_t_bonus_list.itemClicked.connect(self._set_up_bonus_view_second)
        self._ui.general_bonus_list.itemClicked.connect(self._set_up_bonus_view_general)

    def _add_goal_first(self):
        self._score_manager.add_goal_first()
        self._update_score_display()

    def _add_goal_second(self):
        self._score_manager.add_goal_second()
        self._update_score_display()

    def _sub_goal_first(self):
        self._score_manager.subtract_goal_first()
        self._update_score_display()

    def _sub_goal_second(self):
        self._score_manager.subtract_goal_second()
        self._update_score_display()

    def _update_score_display(self):
        score = self._score_manager.get_score()
        self._ui.score.setText(f'{score[0]} - {score[1]}')

    def _add_current_bonus_first(self):
        if hasattr(self, '_current_item_first') and self._current_item_first:
            bonus = self._current_item_first.bonus
            self._viewers_view.add_bonus_for_first(bonus)
            self._apply_bonus(bonus, team=0)
            self._remove_bonus_from_lists(self._current_item_first)
            self._bonuses.remove(bonus)
            self._current_item_first = None
            self._ui.first_team_bonuses.setCurrentIndex(0)

    def _add_current_bonus_second(self):
        if hasattr(self, '_current_item_second') and self._current_item_second:
            bonus = self._current_item_second.bonus
            self._viewers_view.add_bonus_for_second(bonus)
            self._apply_bonus(bonus, team=1)
            self._remove_bonus_from_lists(self._current_item_second)
            self._bonuses.remove(bonus)
            self._current_item_second = None
            self._ui.second_team_bonuses.setCurrentIndex(0)

    def _add_current_bonus_general(self):
        if hasattr(self, '_current_item_general') and self._current_item_general:
            bonus = self._current_item_general.bonus
            self._viewers_view.add_bonus_for_first(bonus)
            self._viewers_view.add_bonus_for_second(bonus)
            self._apply_bonus(bonus, team=None)
            self._remove_bonus_from_lists(self._current_item_general)
            self._bonuses.remove(bonus)
            self._current_item_general = None
            self._ui.general_bonuses.setCurrentIndex(0)
    
    def _throw_ball_button(self):
        board_manager.throw_ball()
        
    def _apply_bonus(self, bonus, team: Optional[int]):
        if isinstance(bonus, TimeBonus):
            duration = timedelta(seconds=bonus.bonus_time())
            if team == 0:
                self._current_time_bonuses[0] = (bonus.bonus_points(), datetime.now() + duration)
            elif team == 1:
                self._current_time_bonuses[1] = (bonus.bonus_points(), datetime.now() + duration)
            else:
                self._current_time_bonuses[0] = (bonus.bonus_points(), datetime.now() + duration)
                self._current_time_bonuses[1] = (bonus.bonus_points(), datetime.now() + duration)
        else:
            if team == 0:
                self._score_manager.set_score((
                    self._score_manager.get_score()[0] + bonus.bonus_points(),
                    self._score_manager.get_score()[1]
                ))
            elif team == 1:
                self._score_manager.set_score((
                    self._score_manager.get_score()[0],
                    self._score_manager.get_score()[1] + bonus.bonus_points()
                ))
            else:
                self._score_manager.set_score((
                    self._score_manager.get_score()[0] + bonus.bonus_points(),
                    self._score_manager.get_score()[1] + bonus.bonus_points()
                ))
        self._update_score_display()

    def _remove_bonus_from_lists(self, item):
        # Make sure the item is removed from all lists
        if hasattr(item, 'second_one') and hasattr(item, 'general'):
            self._ui.second_t_bonus_list.takeItem(self._ui.second_t_bonus_list.row(item.second_one))
            self._ui.general_bonus_list.takeItem(self._ui.general_bonus_list.row(item.general))
        self._ui.first_t_bonus_list.takeItem(self._ui.first_t_bonus_list.row(item))

    def _set_up_bonus_view_first(self, item: QListWidgetItem):
        self._ui.first_team_bonuses.setCurrentIndex(1)
        bonus = item.bonus
        self._current_item_first = item
        self._ui.resource_description.setText(str(bonus))

    def _set_up_bonus_view_second(self, item: QListWidgetItem):
        self._ui.second_team_bonuses.setCurrentIndex(1)
        bonus = item.bonus
        self._current_item_second = item
        self._ui.resource_description_2.setText(str(bonus))

    def _set_up_bonus_view_general(self, item: QListWidgetItem):
        self._ui.general_bonuses.setCurrentIndex(1)
        bonus = item.bonus
        self._current_item_general = item
        self._ui.bonus_desceiption_general.setText(str(bonus))

    def _create_bonus_description(self, bonus: Bonus) -> str:
        description = f'{bonus.name():15}'
        pos = str(bonus.position())
        description += f'{pos:8}'
        if isinstance(bonus, TimeBonus):
            description += '(t)'
        return description

    def _display_bonus_time_left(self):
        now = datetime.now()
        for idx, (multiplier, end_time) in enumerate(self._current_time_bonuses):
            if end_time > now:
                time_left = (end_time - now).seconds
                if idx == 0:
                    self._ui.bonus_time_first.setText(str(time_left))
                else:
                    self._ui.bonus_time_second.setText(str(time_left))
            else:
                if idx == 0:
                    self._ui.bonus_time_first.setText("")
                else:
                    self._ui.bonus_time_second.setText("")

    def _show_bonus_adding(self):
        self._bonus_window.show()

    def _add_bonus(self):
        name = self._bonus_window._ui.bonus_name.text()
        file_name = self._bonus_window._ui.file_name.text()
        bonus_value = self._bonus_window._ui.bonus_value.value()
        position = (self._bonus_window._ui.position_x.value(), self._bonus_window._ui.position_y.value())
        if self._bonus_window._ui.bonus_creation.currentIndex() == 0:
            new_bonus = Bonus(name, bonus_value, position, file_name)
        else:
            bonus_time = self._bonus_window._ui.bonus_duration.value()
            new_bonus = TimeBonus(name, bonus_value, position, bonus_time, file_name)
        self._bonuses.append(new_bonus)
        self._ui.second_t_bonus_list.clear()
        self._ui.first_t_bonus_list.clear()
        self._ui.general_bonus_list.clear()
        self._set_up_bonuses_list()

    def _update_ui(self):
        self._display_bonus_time_left()
        self._update_score_display()
