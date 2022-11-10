class Bonus:
    def __init__(self, bonus_points: int, tex_file="") -> None:
        self._bonus_points = bonus_points
        self._texture_path = tex_file

    def bonus_points(self):
        return self._bonus_points

    def set_bonus_points(self, new_bonus_points: int):
        self._bonus_points = new_bonus_points

    def texture_file(self):
        return self._texture_path

    def set_texture_file(self, new_tex_file: str):
        self._texture_path = new_tex_file
