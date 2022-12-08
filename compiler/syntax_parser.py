import my_token

from parse_table import *

class Parser:

    def __init__(self, tokens: list[my_token.Token]) -> None:
        self.tokens = tokens
        self.stack = None

    def derivate(self, rule, terminal):
        self.stack.pop()
        derivation = parse_table[rule][terminal].split(' ')
        derivation.reverse()
        self.stack.extend(derivation)
    
    def match(self):
        self.stack.pop()
        self.tokens.pop()


    def parse_syntax(self):

        accepted = False
        self.stack = ['<programa>', '@']
        self.stack.reverse()
        self.tokens.reverse() # makes tokens look like a stack

        while self.stack[0] != '@' or accepted == False:

            token_atual = self.tokens[-1]

            if token_atual.type == my_token.TokenType.KEYWORD:
                if token_atual.value == 'program':
                    if self.stack[-1] == '<programa>':
                        self.derivate(PROGRAMA, T_PROGRAM)
                    elif self.stack[-1] == 'program':
                        self.match()
                    else:
                        raise Exception('Era esperado o seguinte token: program')
                elif token_atual.value == 'real':
                    if self.stack[-1] == '<corpo>':
                        self.derivate(CORPO, T_REAL)
                    elif self.stack[-1] == '<dc>':
                        self.derivate(DC, T_REAL)
                    elif self.stack[-1] == '<dc_v>':
                        self.derivate(DC_V, T_REAL)
                    elif self.stack[-1] == '<tipo_var>':
                        self.derivate(TIPO_VAR, T_REAL)
                    elif self.stack[-1] == 'real':
                        self.match()
                    else:
                        raise Exception('Era esperado o seguinte token: real ou integer')
            elif token_atual.type == my_token.TokenType.IDENT:
                self.match()
            elif (token_atual.type == my_token.TokenType.SPACE or
                token_atual.type == my_token.TokenType.NEWLINE_TOKEN or
                token_atual.type == my_token.TokenType.COMMENT):
                self.tokens.pop()
            else:
                print('stack:', self.stack)
                print('last token:', token_atual)
                break
                        
