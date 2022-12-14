import my_token

# Estados
DC = 0 # DECLARAÇÃO DE VAR
CORPO = 1 # CORPO DO CODIGO

class Compiler:

    def __init__(self, tokens: 'list[my_token.Token]', symbol_table: 'dict') -> None:
        self.tokens = tokens
        self.tokens.reverse()

        self.symbol_table = symbol_table

    # Geração de código objeto
    def compile(self, show_code=False):
        self.code = []
        self.data = []
        self.pos = 0

        self.state = DC

        while self.pos != len(self.tokens):
            token_atual = self.tokens[-1]

            if token_atual.type == my_token.TokenType.KEYWORD:
                if token_atual.value == 'program':
                    self.code.append('INPP')
                
                elif token_atual.value == 'begin':
                    self.state = CORPO
                
                elif token_atual.value == 'end':
                    self.code.append('PARA')

                elif token_atual.value == 'real':
                    pass
                    
                elif token_atual.value == 'integer':
                    pass
                
                elif token_atual.value == 'read':
                    self.code.append('LEIT')
                
                elif token_atual.value == 'write':
                    self.code.append('IMPR')
                
                elif token_atual.value == 'if':
                    pass
                
                elif token_atual.value == 'then':
                    pass

                elif token_atual.value == 'while':
                   pass
                
                elif token_atual.value == 'do':
                   pass
                
                elif token_atual.value == 'else':
                    pass

            elif token_atual.type == my_token.TokenType.IDENT:
                if self.state == DC:
                    self.code.append('ALME 1'.format(self.symbol_table[token_atual.value].address))
                elif self.state == CORPO:
                    self.code.append('CRVL {}'.format(self.symbol_table[token_atual.value].address))

            elif (token_atual.type == my_token.TokenType.SPACE or
                token_atual.type == my_token.TokenType.COMMENT):
                pass
            
            elif token_atual.type == my_token.TokenType.NEWLINE_TOKEN:
                pass
            
            elif token_atual.type == my_token.TokenType.ATRIB:
               pass
            
            elif token_atual.type == my_token.TokenType.SEPARATOR:
                if token_atual.value == ',':
                    pass

                elif token_atual.value == ';':
                    pass

                elif token_atual.value == '$':
                    pass

                elif token_atual.value == '.':
                    if self.code[-1] == '.' and len(self.code) == 1:
                        pass
                    else:
                        pass

            elif token_atual.type == my_token.TokenType.OPEN_PAR:
                if token_atual.value == '(':
                    pass

            elif token_atual.type == my_token.TokenType.CLOSE_PAR:
                if token_atual.value == ')':
                    pass
            
            elif token_atual.type == my_token.TokenType.OPERATOR:
                if token_atual.value == '*':
                    self.code.append('MULT')
                
                elif token_atual.value == '/':
                    self.code.append('DIVI')
                
                elif token_atual.value == '+':
                    self.code.append('SOMA')
                
                elif token_atual.value == '-':
                    self.code.append('SUBT')
            
            
            elif token_atual.type == my_token.TokenType.DIGIT:
                self.code.append('CRCT {}'.format(token_atual.value) )
            
            elif token_atual.type == my_token.TokenType.REAL_NUM:
                self.code.append('CRCT {}'.format(token_atual.value) )

            elif token_atual.type == my_token.TokenType.LOGICAL_OP:
                pass

            else:
                print('stack:', self.code)
                print('last token:', token_atual.to_string())
                break
        
            self.tokens.pop()
        
        if show_code:
            for inst in self.code:
                print(inst)