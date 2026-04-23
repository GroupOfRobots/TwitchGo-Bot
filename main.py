# main.py

from PySide6.QtWidgets import QApplication
import sys
import os
from app.core.chat.chat_bot import ChatBot
from app.gui.windows.main_window import MainWindow
from app.gui.windows.viewers_view import ViewersView
from app.utils.logger import setup_logging
from datetime import datetime
from PySide6.QtCore import QTimer

def gui_main(args):
    # Setup logging once
    today = datetime.today().strftime("%Y-%m-%d")
    log_path = os.path.join("logs", f"{today}.log")
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    setup_logging(log_path)

    # Initialize QApplication
    app = QApplication(args)

    # Initialize MainWindow and ViewersView
    window = MainWindow()
    window.show()
    viewers_view = ViewersView(window)
    viewers_view.show()
    window.set_viewers_view(viewers_view)


    # Initialize ChatBot
    chat_bot = ChatBot()

    # Setup QTimer for periodic UI updates
    timer = QTimer()
    timer.timeout.connect(lambda: (viewers_view.run_window(),
                                   viewers_view._display_last_votes(chat_bot.board_manager.current_voiting_state()),
                                   window._display_bonus_time_left(),
                                   window._update_score_display()))
    timer.start(200)  # Update every 200 ms

    # Execute the application
    try:
        sys.exit(app.exec())
    except KeyboardInterrupt:
        pass
    finally:
        chat_bot.stop()

if __name__ == "__main__":
    gui_main(sys.argv)
