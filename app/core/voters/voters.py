from typing import Set

class Voters:
    def __init__(self, option_name: str):
        self.option_name = option_name
        self.votes: Set[str] = set()

    def add_vote(self, username: str) -> None:
        self.votes.add(username)

    def get_votes(self) -> Set[str]:
        return self.votes

    def __str__(self):
        return f"{self.option_name}: {len(self.votes)} votes"
