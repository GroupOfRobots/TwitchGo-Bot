from app.gui.windows.main_window import MainWindow
from app.gui.windows.viewers_view import ViewersView
from app.core.chat.chat_bot import ChatBot
from app.ros.ros_main import main as ros_main
import sys
import threading

def gui_main(args):
    from PySide6.QtWidgets import QApplication
    app = QApplication(args)
    window = MainWindow()
    window.show()
    viewers_view = ViewersView(window)
    viewers_view.show()
    window.set_viewers_view(viewers_view)

    # Uruchomienie ROS w osobnym wątku
    ros_thread = threading.Thread(target=ros_main, daemon=True)
    ros_thread.start()

    # Uruchomienie Chat Bota
    chat_bot = ChatBot(
        set_latest_votes=viewers_view.set_latest_votes,
        get_latest_votes=viewers_view.get_latest_votes
    )
    chat_bot.run()

    try:
        while window.isVisible():
            viewers_view.run_window()
            window._display_bonus_time_left()
            app.processEvents()
            time.sleep(0.2)
    except KeyboardInterrupt:
        pass
    finally:
        chat_bot.stop()

if __name__ == "__main__":
    gui_main(sys.argv)
