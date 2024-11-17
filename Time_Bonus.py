from Bonus import Bonus

class TimeBonus(Bonus):
    def __init__(self, name: str, multiplier: int, position: tuple, bonus_time: float, tex_file="") -> None:
        super().__init__(name, multiplier, position, tex_file)
        self.bonus_time = bonus_time

    def __str__(self) -> str:
        return (f"{super().__str__()}\n"
                f"Bonus duration: {self.bonus_time}s")