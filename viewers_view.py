from viewers_view_ui import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow, QApplication
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

    def run_window(self):
        score = f'{self._main_window._score[0]:2} : {self._main_window._score[1]:2}'
        self._ui.score.setText(score)
        self._ui.bonus_time_first.setText(f'{(self._main_window._current_time_bonuses[0][1] -datetime.now()).seconds if self._main_window._current_time_bonuses[0][1] > datetime.now() else ""}')
        self._ui.bonus_time_second.setText(f'{(self._main_window._current_time_bonuses[1][1] -datetime.now()).seconds if self._main_window._current_time_bonuses[1][1] > datetime.now() else ""}')




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
