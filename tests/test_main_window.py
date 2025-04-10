# tests/test_main.py

import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Dodanie głównego katalogu do sys.path, aby importować moduły
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestMain(unittest.TestCase):
    @patch('app.ros.obstacle_activator.main')  # Poprawiony import
    @patch('app.core.chat.chat_bot.ChatBot')
    @patch('app.gui.windows.viewers_view.ViewersView')
    @patch('app.gui.windows.main_window.MainWindow')
    @patch('PySide6.QtWidgets.QApplication')
    def test_gui_main(self, mock_app, mock_main_window, mock_viewers_view, mock_chat_bot, mock_ros_main):
        mock_instance_app = MagicMock()
        mock_app.return_value = mock_instance_app

        mock_instance_main_window = MagicMock()
        mock_main_window.return_value = mock_instance_main_window

        mock_instance_viewers_view = MagicMock()
        mock_viewers_view.return_value = mock_instance_viewers_view

        mock_instance_chat_bot = MagicMock()
        mock_chat_bot.return_value = mock_instance_chat_bot

        with patch('app.gui.windows.main_window.MainWindow.set_viewers_view') as mock_set_viewers_view:
            import app.main  # Zakładając, że main.py jest w katalogu app

            # Wywołanie funkcji gui_main
            app.main.gui_main(['main.py'])

        # Sprawdzenie, czy QApplication został uruchomiony
        mock_app.assert_called_once_with(['main.py'])

        # Sprawdzenie, czy MainWindow został utworzony i pokazany
        mock_main_window.assert_called_once()
        mock_instance_main_window.show.assert_called_once()

        # Sprawdzenie, czy ViewersView został utworzony i pokazany
        mock_viewers_view.assert_called_once_with(mock_instance_main_window)
        mock_instance_viewers_view.show.assert_called_once()

        # Sprawdzenie, czy set_viewers_view został wywołany
        mock_set_viewers_view.assert_called_once_with(mock_instance_viewers_view)

        # Sprawdzenie, czy ChatBot został uruchomiony
        mock_chat_bot.assert_called_once_with(
            set_latest_votes=mock_instance_viewers_view.set_latest_votes,
            get_latest_votes=mock_instance_viewers_view.get_latest_votes
        )
        mock_instance_chat_bot.run.assert_called_once()

        # Sprawdzenie, czy ROS został uruchomiony w osobnym wątku
        mock_ros_main.assert_called_once()


if __name__ == '__main__':
    unittest.main()
