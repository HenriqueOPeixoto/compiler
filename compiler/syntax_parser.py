import my_token

from parse_table import *

class Parser:

    def parse_syntax(self, tokens: list[my_token.Token]):

        accepted = False
        stack = ['<programa>', '@']
        stack.reverse()
        tokens.reverse() # makes tokens look like a stack

        while stack[0] != '@' or accepted == False:

            token_atual = tokens[-1]

            if token_atual.type == my_token.TokenType.KEYWORD:
                if token_atual.value == 'program':
                    if stack[-1] == '<programa>':
                        stack.pop()
                        derivation = parse_table[PROGRAMA][T_PROGRAM].split(' ')
                        derivation.reverse()
                        stack.extend(derivation)
                    elif stack[-1] == 'program':
                        stack.pop()
                        tokens.pop()
                    else:
                        raise Exception('Era esperado o seguinte token: program')
                if token_atual.value == 'real':
                    if stack[-1] == '<corpo>':
                        stack.pop()
                        derivation = parse_table[CORPO][T_REAL].split(' ')
                        derivation.reverse()
                        stack.extend(derivation)
            elif token_atual.type == my_token.TokenType.IDENT:
                stack.pop()
                tokens.pop()
            elif (token_atual.type == my_token.TokenType.SPACE or
                token_atual.type == my_token.TokenType.NEWLINE_TOKEN or
                token_atual.type == my_token.TokenType.COMMENT):
                tokens.pop()
                        
