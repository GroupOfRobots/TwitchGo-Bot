from resource_gathering_ui import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow, QApplication
import sys


class MainWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self._score = (0, 0)
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._ui.score.setText(f'{self._score[0]} - {self._score[1]}')
        self._ui.add_goal_first.clicked.connect(self._add_goal_first)
        self._ui.add_goal_second.clicked.connect(self._add_goal_second)
        self._ui.subtract_goal_first.clicked.connect(self._sub_goal_first)
        self._ui.subtract_goal_second.clicked.connect(self._sub_goal_second)

    def _add_goal_first(self):
        self._score = (self._score[0]+1, self._score[1])
        self._ui.score.setText(f'{self._score[0]} - {self._score[1]}')

    def _add_goal_second(self):
        self._score = (self._score[0], self._score[1]+1)
        self._ui.score.setText(f'{self._score[0]} - {self._score[1]}')

    def _sub_goal_first(self):
        if self._score[0] > 0:
            self._score = (self._score[0]-1, self._score[1])
            self._ui.score.setText(f'{self._score[0]} - {self._score[1]}')

    def _sub_goal_second(self):
        if self._score[1] > 0:
            self._score = (self._score[0], self._score[1]-1)
            self._ui.score.setText(f'{self._score[0]} - {self._score[1]}')


def guiMain(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    return app.exec_()




if(__name__ == "__main__"):
    guiMain(sys.argv)
