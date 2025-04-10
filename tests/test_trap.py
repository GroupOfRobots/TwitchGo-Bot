# tests/test_trap.py

import unittest
from unittest.mock import Mock
from app.core.traps.trap import Trap


class TestTrap(unittest.TestCase):
    def test_trap_initialization(self):
        trap = Trap(name="Spike Trap")
        self.assertEqual(trap.name, "Spike Trap")
        self.assertEqual(trap.votes, [])
        self.assertIsNone(trap._command)

    def test_trap_with_command(self):
        mock_command = Mock()
        trap = Trap(name="Fire Trap", command=mock_command)
        trap.run()
        mock_command.assert_called_once()

    def test_add_vote(self):
        trap = Trap(name="Ice Trap")
        trap.add_vote("user1")
        self.assertIn("user1", trap.votes)

    def test_clear_votes(self):
        trap = Trap(name="Poison Trap")
        trap.add_vote("user1")
        trap.add_vote("user2")
        trap.clear_votes()
        self.assertEqual(trap.votes, [])

    def test_run_without_command(self):
        trap = Trap(name="No-Op Trap")
        trap.run()  # Should not raise any exception


if __name__ == '__main__':
    unittest.main()
