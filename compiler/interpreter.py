# Executor do código objeto

class Interpreter:

    code = []
    data = []
    pos = 0

    def __init__(self, code: 'list[str]') -> None:
        self.code = code
        #self.code.reverse()

    def execute(self):

        while self.code[self.pos] != 'PARA':
            inst_atual = self.code[self.pos].split(' ') # separa a instrução em opcode e operando
            opcode = inst_atual[0]
            operand = None # Nem todas as instruções tem operando
            
            if opcode == 'INPP':
                #self.pos = -1
                pass
            elif opcode == 'ALME':
                operand = int(inst_atual[1])
                self.data.extend([None for address in range(operand)])
                #self.pos += len(self.data)
            elif opcode == 'CRVL':
                operand = int(inst_atual[1])
                self.data.append(self.data[operand - 1])
                #pos += 1
            elif opcode == 'CRCT':
                operand = float(inst_atual[1])
                self.data.append(operand)
                #pos += 1
            elif opcode == 'ARMZ':
                operand = int(inst_atual[1]) - 1 # data é 0-based, por isso subtrai 1
                self.data[operand] = self.data[-1]
                #pos -= 1
                self.data.pop()
            elif opcode == 'IMPR':
                print(self.data[-1])
                self.data.pop()
            elif opcode == 'LEIT':
                self.data.append(int(input('>>> ')))
            elif opcode == 'SOMA':
                op1 = self.data.pop()
                op2 = self.data.pop()

                self.data.append(op1 + op2)
            elif opcode == 'MULT':
                op1 = self.data.pop()
                op2 = self.data.pop()

                self.data.append(op1 * op2)
            elif opcode == 'SUBT':
                op2 = self.data.pop()
                op1 = self.data.pop()

                self.data.append(op1 - op2)
            elif opcode == 'DIVI':
                op2 = self.data.pop()
                op1 = self.data.pop()

                self.data.append(op1 / op2)
            elif opcode == 'CPME':
                op1 = self.data.pop()
                op2 = self.data.pop()

                self.data.append(int(op1 < op2))
            elif opcode == 'CPMA':
                op1 = self.data.pop()
                op2 = self.data.pop()

                self.data.append(int(op1 > op2))
            elif opcode == 'CPIG':
                op1 = self.data.pop()
                op2 = self.data.pop()

                self.data.append(int(op1 == op2))
            elif opcode == 'CDES':
                op1 = self.data.pop()
                op2 = self.data.pop()

                self.data.append(int(op1 != op2))
            elif opcode == 'CPMI':
                op1 = self.data.pop()
                op2 = self.data.pop()

                self.data.append(int(op1 <= op2))
            elif opcode == 'CMAI':
                op1 = self.data.pop()
                op2 = self.data.pop()

                self.data.append(int(op1 >= op2))
                

            self.pos += 1
