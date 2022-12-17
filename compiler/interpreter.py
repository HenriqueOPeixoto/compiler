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
                operand = int(inst_atual[1])
                self.data.extend([None for address in range(operand)])
                pos += len(self.data)
            elif opcode == 'CRVL':
                operand = int(inst_atual[1])
                self.data.append(self.data[operand])
                pos += 1
            elif opcode == 'CRCT':
                operand = float(inst_atual[1])
                self.data.append(operand)
                pos += 1
            elif opcode == 'ARMZ':
                operand = int(inst_atual[1]) - 1 # data é 0-based, por isso subtrai 1
                self.data[operand] = self.data[-1]
                pos -= 1
            
            self.code.pop()
