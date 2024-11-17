class Bonus:
    def __init__(self, name: str, bonus_points: int, position: tuple, tex_file="") -> None:
        self.name = name
        self.bonus_points = bonus_points
        self.position = position
        self.texture_file = tex_file

    def __str__(self) -> str:
        return (f"{self.name:14}\n"
                f"Position: {self.position}\n"
                f"Bonus points: {self.bonus_points}")