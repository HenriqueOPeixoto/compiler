import my_token

from parse_table import *

class Parser:

    def parse_syntax(self, tokens: list[my_token.Token]):

        accepted = False
        stack = ['<programa>', '@']
        stack.reverse()

        while stack[0] != '@' or accepted == False:

            token_atual = tokens.pop()

            if token_atual.type == my_token.TokenType.KEYWORD:
                if token_atual.value == 'program':
                    if stack[-1] == '<programa>':
                        stack.pop()
                        derivation = parse_table[PROGRAMA][T_PROGRAM].split(' ')
                        derivation.reverse()
                        stack.extend(derivation)
                    else:
                        raise Exception('Era esperado o seguinte token: program')
                        
