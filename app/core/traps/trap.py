# app/core/traps/trap.py

import logging
from typing import Optional, Callable

class Trap:
    def __init__(self, name: str, command: Optional[Callable] = None):
        self._name = name
        self._command = command
        self._votes = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def votes(self) -> list:
        return self._votes

    def clear_votes(self) -> None:
        self._votes = []

    def add_vote(self, username: str) -> None:
        self._votes.append(username)

    def run(self) -> None:
        logging.info(f"[TRAP] {self._name} is running")
        print(f"{self._name} is running")
        if self._command:
            self._command()

    def __str__(self) -> str:
        """Return the full vote command string with the current vote count."""
        count = len(self._votes)
        return f"!vote {self._name} ({count})"

    def __repr__(self) -> str:
        """Return the same as __str__ for display purposes."""
        return self.__str__()
