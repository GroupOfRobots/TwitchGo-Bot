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
