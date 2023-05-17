from obstacle import ObstacleActivator

class Trap:
    obstacleActivator = ObstacleActivator([])

    def __init__(self, name, command=None):
        self._name = name
        self._command = command
        self._votes = []
        Trap.obstacleActivator.append(self._name)

    @property
    def get_name(self):
        return self._name

    @property
    def get_votes(self):
        return self._votes

    def clear_votes(self):
        self._votes = []

    def add_vote(self, username):
        self._votes.append(username)

    def run(self):
        print(f"{self.get_name} is running")
        if self._command is not None:
            self._command()
        else:
            Trap.obstacleActivator.start_obstacle(self._name)

    def __str__(self):
        return f"{self._name}: {len(self._votes)}"
