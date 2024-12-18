# app/core/bonuses/bonus.py

from typing import Tuple


class Bonus:
    def __init__(self, name: str, bonus_points: int, position: Tuple[int, int], tex_file: str = "") -> None:
        self._name = name
        self._bonus_points = bonus_points
        self._position = position
        self._texture_path = tex_file

    def bonus_points(self) -> int:
        return self._bonus_points

    def texture_file(self) -> str:
        return self._texture_path

    def position(self) -> Tuple[int, int]:
        return self._position

    def name(self) -> str:
        return self._name

    def __str__(self) -> str:
        return f'{self._name:15} Pozycja: {self._position} Punkty Bonusowe: {self._bonus_points}'


