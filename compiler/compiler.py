import my_token
import utils.rpn as rpn

# Estados
PROGRAM = -1 # nome do programa
DC = 0 # DECLARAÇÃO DE VAR
CORPO = 1 # CORPO DO CODIGO

class Compiler:

    def __init__(self, tokens: 'list[my_token.Token]', symbol_table: 'dict', subcomp=False) -> None:
        self.tokens = tokens

        self.symbol_table = symbol_table
        self.subcomp = subcomp # Compiladores auxiliares executados durante a geração de expressões

    # Geração de código objeto
    def compile(self, show_code=False):
        self.code = []
        self.data = []
        self.pos = 0

        if self.subcomp:
            self.state = CORPO
        else:
            self.state = PROGRAM

        while self.pos != len(self.tokens):
            token_atual = self.tokens[self.pos]

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
                if self.state == PROGRAM:
                    self.state = DC
                if self.state == DC:
                    self.code.append('ALME 1')
                elif self.state == CORPO:
                    self.code.append('CRVL {}'.format(self.symbol_table[token_atual.value].address))

            elif (token_atual.type == my_token.TokenType.SPACE or
                token_atual.type == my_token.TokenType.COMMENT):
                pass
            
            elif token_atual.type == my_token.TokenType.NEWLINE_TOKEN:
                pass
            
            elif token_atual.type == my_token.TokenType.ATRIB:
                if token_atual.value == ':=':
                    cont = self.pos + 1
                    expr_tokens = [] # pega os tokens da expressao atual para converter para rpn
                    while self.tokens[cont].type != my_token.TokenType.SEPARATOR:
                        expr_tokens.append(self.tokens[cont])
                        cont += 1
                    expr_tokens = rpn.shunting_yard(expr_tokens) #coloca a expressao em rpn 
                    print(expr_tokens)
                    # Chama um subcompilador para gerar o código da expressão
                    subcomp = Compiler(expr_tokens, self.symbol_table, subcomp=True) 
                    self.code.append(subcomp.compile())

                    # Pula o código que já foi compilado
                    self.pos = cont
                       
            
            elif token_atual.type == my_token.TokenType.SEPARATOR:
                if token_atual.value == ',':
                    pass

                elif token_atual.value == ';':
                    pass

                elif token_atual.value == '$':
                    pass

                elif token_atual.value == '.':
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
        
            self.pos += 1
        
        if show_code:
            for inst in self.code:
                print(inst)
        
        return self.code