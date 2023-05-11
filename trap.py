class Trap:
    def __init__(self, name, command=None):
        self._name = name
        self._command = command
        self._votes = []

    @property
    def get_name(self):
        return self._name

    @property
    def get_votes(self):
        return self._votes

    def set_votes(self, votes: list):
        self._votes = votes

    def add_vote(self, username):
        self._votes.append(username)

    def run(self):
        if self._command is not None:
            self._command()
