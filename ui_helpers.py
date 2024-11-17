from PySide2.QtWidgets import QListWidgetItem
from PySide2.QtGui import QBrush, QColor


def create_bonus_item(bonus, team_num=0):
    item = QListWidgetItem(f"{bonus.name:15}{str(bonus.position):8}")
    if bonus.bonus_points < 0:
        item.setForeground(QBrush(QColor("Magenta")))
    item.bonus = bonus
    item.team_num = team_num
    return item