from viewers_view_ui import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt
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

    def run_window(self):
        if datetime.now().microsecond//500 % 2 == 1:
            with open("score.txt", 'r') as file_handle:
                score = f'{(file_handle.readline()).strip():>2} : {(file_handle.readline()):2}'
                self._ui.score.setText(score)
                line = file_handle.readline()
                if not line.strip() == "":
                    self._ui.bonus_time_first.setText(line)
                line = file_handle.readline()
                if not line.strip() == "":
                    self._ui.bonus_time_second.setText(line)




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
