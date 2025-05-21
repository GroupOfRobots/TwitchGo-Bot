# app/core/traps/trap.py

import logging
from typing import Optional, Callable
from rclpy.node import Node
from std_msgs.msg import Bool

class Trap(Node):
    def __init__(self, name: str, label:str, topicName: str):
        super().__init__(name)
        self._name = name
        self._label = label
        self._votes = []
        self.publisher = self.create_publisher(Bool, topicName, 10)
        
    @property
    def name(self) -> str:
        return self._name

    @property
    def votes(self) -> list:
        return self._votes

    def clear_votes(self) -> None:
        self._votes = []

    def add_vote(self, username: str) -> None:
        if username not in self._votes:
            self._votes.append(username)

    def count_votes(self):
        return len(self._votes)

    def run(self) -> None:
        msg = Bool()
        msg.data = True
        self.publisher.publish(msg)
        logging.info(f"[TRAP] {self._name} is running")


    def stop(self) -> None:
        msg = Bool()
        msg.data = False
        self.publisher.publish(msg)
        logging.info(f"[TRAP] {self._name} is stopping")
        
    def __str__(self) -> str:
        """Return the full vote command string with the current vote count."""
        count = len(self._votes)
        return f"!vote {self._name} ({count})"

    def __repr__(self) -> str:
        """Return the same as __str__ for display purposes."""
        return self.__str__()
