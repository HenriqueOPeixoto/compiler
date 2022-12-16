# Executor do código objeto

class Interpreter:

    code = []
    data = []
    pos = 0

    def __init__(self, code: 'list[str]') -> None:
        self.code = code
        self.code.reverse()

    def execute(self):

        while self.code[-1] != 'PARA':
            if self.code[-1] == 'INPP':
                pos = -1
            elif self.code[-1] == 'ALME':
                pass
