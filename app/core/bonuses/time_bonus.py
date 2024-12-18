# app/core/bonuses/time_bonus.py

from app.core.bonuses.bonus import Bonus

class TimeBonus(Bonus):
    def __init__(self, name: str, multiplier: int, position: tuple[int, int], bonus_time: float,
                 tex_file: str = "") -> None:
        super().__init__(name, multiplier, position, tex_file)
        self._bonus_time = bonus_time

    def bonus_time(self) -> float:
        return self._bonus_time

    def __str__(self) -> str:
        return f'{self._name:15} Pozycja: {self._position} Mnożnik: {self._bonus_points} Czas Bonusu: {self._bonus_time} sekund'
