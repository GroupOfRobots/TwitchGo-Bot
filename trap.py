class Trap:
    def __init__(self, name, command=None):
        self._name = name
        self._command = command

    @property
    def get_name(self):
        return self._name

    def run(self):
        if self._command is not None:
            self._command()
