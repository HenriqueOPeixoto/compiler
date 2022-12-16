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
            inst_atual = self.code[-1].split(' ') # separa a instrução em opcode e operando
            opcode = inst_atual[0]
            operand = None # Nem todas as instruções tem operando
            
            if opcode == 'INPP':
                pos = -1
            elif opcode == 'ALME':
                self.data
