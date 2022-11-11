class Token:

    def __init__(self, value, type) -> None:
        self.value = value
        self.type = type

    def to_string(self) -> str:
        return '[{}: {}]'.format(self.value, self.type)