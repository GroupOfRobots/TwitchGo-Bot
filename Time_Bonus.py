from Bonus import Bonus


class TimeBonus (Bonus):
    def __init__(self, name: str, multiplier: int, position: tuple, bonus_time, tex_file="") -> None:
        super().__init__(name, multiplier, position, tex_file)
        self._bonus_time = bonus_time

    def bonus_time(self):
        return self._bonus_time

    def set_bonus_time(self, new_time):
        self._bonus_time = new_time
