class Bonus:
    def __init__(self, bonus_points: int, position: tuple, tex_file="") -> None:
        self._bonus_points = bonus_points
        self._texture_path = tex_file
        self._position = position

    def bonus_points(self) -> int:
        return self._bonus_points

    def set_bonus_points(self, new_bonus_points: int) -> None:
        self._bonus_points = new_bonus_points

    def texture_file(self) -> str:
        return self._texture_path

    def set_texture_file(self, new_tex_file: str) -> None:
        self._texture_path = new_tex_file

    def position(self) -> tuple:
        return self._position

    def set_position(self, new_position: tuple) -> None:
        self._position = new_position
