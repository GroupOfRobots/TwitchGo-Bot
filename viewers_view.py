from viewers_view_ui import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt
from PySide2.QtMultimediaWidgets import QVideoWidget
from PySide2.QtMultimedia import QMediaPlayer, QCamera, QCameraInfo, QCameraImageCapture, QCameraViewfinderSettings
from PySide6.QtMultimedia import (QMediaDevices)
import sys
from datetime import datetime
from time import sleep


class ViewersView(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._ui.score.setText('123')
        self._ui.background_image.setText("")
        self._ui.background_image.setFixedSize(800, 600)
        self._ui.background_image.setPixmap(QPixmap("twitch_go.png"))
        self._ui.background_image.setAlignment(Qt.AlignCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ViewersView()
    window.setFixedSize(800, 600)
    window.show()

    window._ui.bonus_time_first.setText("")
    window._ui.bonus_time_second.setText("")

    line = None
    while window.isVisible():
        if datetime.now().microsecond//500 % 2 == 1:
            with open("score.txt", 'r') as file_handle:
                score = f'{(file_handle.readline()).strip():>2} : {(file_handle.readline()):2}'
                window._ui.score.setText(score)
                line = file_handle.readline()
                if not line.strip() == "":
                    window._ui.bonus_time_first.setText(line)
                line = file_handle.readline()
                if not line.strip() == "":
                    window._ui.bonus_time_second.setText(line)
        app.processEvents()
        sleep(0.2)
