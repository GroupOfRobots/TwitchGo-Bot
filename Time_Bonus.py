from Bonus import Bonus


class TimeBonus (Bonus):
    def __init__(self, name: str, multiplier: int, position: tuple, bonus_time, tex_file="") -> None:
        super().__init__(name, multiplier, position, tex_file)
        self._bonus_time = bonus_time

    def bonus_time(self):
        return self._bonus_time

    def set_bonus_time(self, new_time):
        self._bonus_time = new_time

    def __str__(self) -> str:
        return f'{self._name:14}\nPosition: {self._position}\nBonus points: {self._bonus_points}\nBonus duration: {self._bonus_time}'
