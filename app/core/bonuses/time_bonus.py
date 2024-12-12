# app/core/bonuses/time_bonus.py

from app.core.bonuses.bonus import Bonus

class TimeBonus(Bonus):
    def __init__(self, name: str, multiplier: int, position: tuple, bonus_time: float, tex_file: str = "") -> None:
        super().__init__(name, multiplier, position, tex_file)
        self._bonus_time = bonus_time

    def bonus_time(self) -> float:
        return self._bonus_time

    def __str__(self) -> str:
        return f'{self._name:15} Position: {self._position} Multiplier: {self._bonus_points} Bonus Duration: {self._bonus_time} seconds'
