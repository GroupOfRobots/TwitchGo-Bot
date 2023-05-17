from PySide2.QtWidgets import QApplication
import sys
from chat_bot import ChatBot
import rclpy

def gui_main(args):
    rclpy.init(args=args)
    app = QApplication(args)
    from MainWindow import MainWindow
    window = MainWindow()
    window.show()
    from viewers_view import ViewersView
    viewers_view = ViewersView(window)
    viewers_view.show()
    window.set_viewers_view(viewers_view)
    chat_bot = ChatBot(viewers_view.set_latest_votes,
                       viewers_view.get_latest_votes)
    chat_bot.run()

    from trap import Trap
    while window.isVisible():
        viewers_view.run_window()
        window._display_bonus_time_left()
        app.processEvents()
        # rclpy.spin_once(Trap.obstacleActivator)
        # print('Spin once test')

    rclpy.shutdown()


if __name__ == "__main__":
    gui_main(sys.argv)