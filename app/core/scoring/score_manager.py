# app/core/scoring/score_manager.py

from typing import Tuple

class ScoreManager:
    def __init__(self):
        self.score = (0, 0)  # (first_team_score, second_team_score)

    def add_goal_first(self) -> None:
        self.score = (self.score[0] + 1, self.score[1])

    def add_goal_second(self) -> None:
        self.score = (self.score[0], self.score[1] + 1)

    def subtract_goal_first(self) -> None:
        if self.score[0] > 0:
            self.score = (self.score[0] - 1, self.score[1])

    def subtract_goal_second(self) -> None:
        if self.score[1] > 0:
            self.score = (self.score[0], self.score[1] - 1)

    def get_score(self) -> Tuple[int, int]:
        return self.score

    def set_score(self, new_score: Tuple[int, int]) -> None:
        self.score = new_score
