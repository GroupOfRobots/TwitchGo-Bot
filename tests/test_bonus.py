# tests/test_bonus.py

import unittest
from app.core.bonuses.bonus import Bonus
from app.core.bonuses.time_bonus import TimeBonus


class TestBonus(unittest.TestCase):
    def test_bonus_initialization(self):
        bonus = Bonus(name="Test Bonus", bonus_points=10, position=(5, 5), tex_file="path/to/texture.png")
        self.assertEqual(bonus.name(), "Test Bonus")
        self.assertEqual(bonus.bonus_points(), 10)
        self.assertEqual(bonus.position(), (5, 5))
        self.assertEqual(bonus.texture_file(), "path/to/texture.png")

    def test_bonus_str(self):
        bonus = Bonus(name="Test Bonus", bonus_points=10, position=(5, 5))
        expected_str = "Test Bonus      Pozycja: (5, 5) Punkty Bonusowe: 10"
        self.assertEqual(str(bonus), expected_str)


class TestTimeBonus(unittest.TestCase):
    def test_time_bonus_initialization(self):
        time_bonus = TimeBonus(name="Time Bonus", multiplier=2, position=(10, 10), bonus_time=30.0,
                               tex_file="path/to/texture.png")
        self.assertEqual(time_bonus.name(), "Time Bonus")
        self.assertEqual(time_bonus.bonus_points(), 2)
        self.assertEqual(time_bonus.position(), (10, 10))
        self.assertEqual(time_bonus.bonus_time(), 30.0)
        self.assertEqual(time_bonus.texture_file(), "path/to/texture.png")

    def test_time_bonus_str(self):
        time_bonus = TimeBonus(name="Time Bonus", multiplier=2, position=(10, 10), bonus_time=30.0)
        expected_str = "Time Bonus      Pozycja: (10, 10) Mnożnik: 2 Czas Bonusu: 30.0 sekund"
        self.assertEqual(str(time_bonus), expected_str)


if __name__ == '__main__':
    unittest.main()
