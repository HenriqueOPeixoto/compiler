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
                
                
                elif token_atual.value == 'begin':
                    if self.stack[-1] == '<corpo>':
                        self.derivate(CORPO, T_BEGIN)
                    elif self.stack[-1] == '<dc>':
                        self.derivate(DC, T_BEGIN)
                    elif self.stack[-1] == '<mais_dc>':
                        self.derivate(MAIS_DC, T_BEGIN)
                    elif self.stack[-1] == '<mais_var>':
                        self.derivate(MAIS_VAR, T_BEGIN)
                    elif self.stack[-1] == 'begin':
                        self.match()
                    else:
                        raise Exception('Era esperado o token begin')
                
                elif token_atual.value == 'end':
                    if self.stack[-1] == '<mais_comandos>':
                        self.derivate(MAIS_COMANDOS, T_END)
                    elif self.stack[-1] == '<outros_termos>':
                        self.derivate(OUTROS_TERMOS, T_END)
                    elif self.stack[-1] == '<mais_fatores>':
                        self.derivate(MAIS_FATORES, T_END)

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
                    
                elif token_atual.value == 'integer':
                    if self.stack[-1] == '<corpo>':
                        self.derivate(CORPO, T_INTEGER)
                    elif self.stack[-1] == '<dc>':
                        self.derivate(DC, T_INTEGER)
                    elif self.stack[-1] == '<dc_v>':
                        self.derivate(DC_V, T_INTEGER)
                    elif self.stack[-1] == '<tipo_var>':
                        self.derivate(TIPO_VAR, T_INTEGER)
                    elif self.stack[-1] == 'integer':
                        self.match()
                    else:
                        raise Exception('Era esperado o seguinte token: real ou integer')
                
                elif token_atual.value == 'read':
                    if self.stack[-1] == '<comandos>':
                        self.derivate(COMANDOS, T_READ)
                    elif self.stack[-1] == '<comando>':
                        self.derivate(COMANDO, T_READ)
                    elif self.stack[-1] == 'read':
                        self.match()
                    else:
                        raise Exception('Era esperado um comando')
                
                elif token_atual.value == 'write':
                    if self.stack[-1] == '<comandos>':
                        self.derivate(COMANDOS, T_WRITE)
                    elif self.stack[-1] == '<comando>':
                        self.derivate(COMANDO, T_WRITE)
                    elif self.stack[-1] == 'write':
                        self.match()
                    else:
                        raise Exception('Era esperado um comando')
                
                elif token_atual.value == 'if':
                    if self.stack[-1] == '<comandos>':
                        self.derivate(COMANDOS, T_IF)
                    elif self.stack[-1] == '<comando>':
                        self.derivate(COMANDO, T_IF)
                    elif self.stack[-1] == 'if':
                        self.match()
                
                elif token_atual.value == 'then':
                    if self.stack[-1] == '<outros_termos>':
                        self.derivate(OUTROS_TERMOS, T_THEN)
                    elif self.stack[-1] == '<mais_fatores>':
                        self.derivate(MAIS_FATORES, T_THEN)
                    elif self.stack[-1] == 'then':
                        self.match()

                elif token_atual.value == 'while':
                    if self.stack[-1] == '<comandos>':
                        self.derivate(COMANDOS, T_WHILE)
                    elif self.stack[-1] == '<comando>':
                        self.derivate(COMANDO, T_WHILE)
                    elif self.stack[-1] == 'while':
                        self.match()
                
                elif token_atual.value == 'do':
                    if self.stack[-1] == '<outros_termos>':
                        self.derivate(OUTROS_TERMOS, T_DO)
                    elif self.stack[-1] == '<mais_fatores>':
                        self.derivate(MAIS_FATORES, T_DO)
                    elif self.stack[-1] == 'do':
                        self.match()
                
                elif token_atual.value == 'else':
                    if self.stack[-1] == '<mais_comandos>':
                        self.derivate(MAIS_COMANDOS, T_ELSE)
                    elif self.stack[-1] == '<outros_termos>':
                        self.derivate(OUTROS_TERMOS, T_ELSE)
                    elif self.stack[-1] == '<mais_fatores>':
                        self.derivate(MAIS_FATORES, T_ELSE)
                    elif self.stack[-1] == '<pfalsa>':
                        self.derivate(PFALSA, T_ELSE)
                    elif self.stack[-1] == 'else':
                        self.match()

            elif token_atual.type == my_token.TokenType.IDENT:
                self.match()

            elif (token_atual.type == my_token.TokenType.SPACE or
                token_atual.type == my_token.TokenType.NEWLINE_TOKEN or
                token_atual.type == my_token.TokenType.COMMENT):
                self.tokens.pop()
            
            elif token_atual.type == my_token.TokenType.ATRIB:
                if token_atual.value == ':' and self.stack[-1] == ':':
                    self.match()
                elif token_atual.value == ':=' and self.stack[-1] == ':=':
                    self.match()
            
            else:
                print('stack:', self.stack)
                print('last token:', token_atual.to_string())
                break
                        
