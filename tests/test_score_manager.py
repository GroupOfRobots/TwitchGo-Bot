# tests/test_score_manager.py

import unittest
from app.core.scoring.score_manager import ScoreManager


class TestScoreManager(unittest.TestCase):
    def setUp(self):
        self.score_manager = ScoreManager()

    def test_initial_score(self):
        self.assertEqual(self.score_manager.get_score(), (0, 0))

    def test_add_goal_first(self):
        self.score_manager.add_goal_first()
        self.assertEqual(self.score_manager.get_score(), (1, 0))

    def test_add_goal_second(self):
        self.score_manager.add_goal_second()
        self.assertEqual(self.score_manager.get_score(), (0, 1))

    def test_subtract_goal_first(self):
        self.score_manager.add_goal_first()
        self.score_manager.subtract_goal_first()
        self.assertEqual(self.score_manager.get_score(), (0, 0))

    def test_subtract_goal_first_no_negative(self):
        self.score_manager.subtract_goal_first()
        self.assertEqual(self.score_manager.get_score(), (0, 0))

    def test_subtract_goal_second(self):
        self.score_manager.add_goal_second()
        self.score_manager.subtract_goal_second()
        self.assertEqual(self.score_manager.get_score(), (0, 0))

    def test_subtract_goal_second_no_negative(self):
        self.score_manager.subtract_goal_second()
        self.assertEqual(self.score_manager.get_score(), (0, 0))

    def test_set_score(self):
        self.score_manager.set_score((5, 3))
        self.assertEqual(self.score_manager.get_score(), (5, 3))


if __name__ == '__main__':
    unittest.main()
