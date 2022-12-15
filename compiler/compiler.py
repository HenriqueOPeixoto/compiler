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

        atrib = False # É uma atribuição
        last_ident = None # Último identificador. Usado em expressões
        reading_input = False # Está lendo uma variável?

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
                    reading_input = True
                
                elif token_atual.value == 'write':
                    cont = self.pos
                    while self.tokens[cont].type != my_token.TokenType.IDENT:
                        cont += 1
                    self.code.append('CRVL {}'.format(self.symbol_table[self.tokens[cont].value].address))
                    self.code.append('IMPR')

                    self.pos = cont
                
                elif token_atual.value == 'if':
                    cont = self.pos + 1
                    logical_op = None
                    while self.tokens[cont].type != my_token.TokenType.KEYWORD: # até chegar no then
                        if self.tokens[cont].type == my_token.TokenType.IDENT:
                            self.code.append('CRVL {}'.format(self.symbol_table[self.tokens[cont].value].address))
                        elif (self.tokens[cont].type == my_token.TokenType.DIGIT or 
                            self.tokens[cont].type == my_token.TokenType.REAL_NUM):
                            self.code.append('CRCT {}'.format(self.tokens[cont].value))
                        elif self.tokens[cont].type == my_token.TokenType.LOGICAL_OP:
                            logical_op = self.tokens[cont].value
                        cont +=1

                    if logical_op == '>':
                        self.code.append('CPMA')
                    elif logical_op == '<':
                        self.code.append('CPME')
                    elif logical_op == '=':
                        self.code.append('CPIG')
                    elif logical_op == '<>':
                        self.code.append('CDES')
                    elif logical_op == '>=':
                        self.code.append('CMAI')
                    elif logical_op == '<=':
                        self.code.append('CPMI')
                    
                    self.pos = cont - 1 # para voltar para o token 'then'
                
                elif token_atual.value == 'then':
                    cont = self.pos + 1
                    if_tokens = []
                    while self.tokens[cont].value != '$': # Até chegar no fim do bloco if
                        if_tokens.append(self.tokens[cont])
                        cont += 1
                    subcompiler = Compiler(if_tokens, self.symbol_table, subcomp=True)
                    if_obj_code = subcompiler.compile() # compila código dentro do if

                    # calculando número da instrução para fazer o desvio
                    goto = len(self.code) + 1 + len(if_obj_code)  # O +1 é para considerar a instrução de desvio que vou adicionar

                    self.code.append('DSVF {}'.format(goto))
                    self.code.extend(if_obj_code)

                    self.pos = cont


                elif token_atual.value == 'while':
                   pass
                
                elif token_atual.value == 'do':
                   pass
                
                elif token_atual.value == 'else':
                    pass

            elif token_atual.type == my_token.TokenType.IDENT:
                if self.state == PROGRAM:
                    self.state = DC
                elif self.state == DC:
                    self.code.append('ALME 1')
                elif self.state == CORPO:
                    cont = self.pos

                    while (self.tokens[cont].type != my_token.TokenType.SEPARATOR
                        and self.tokens[cont].type != my_token.TokenType.KEYWORD
                        and self.subcomp == False):
                        if self.tokens[cont].type == my_token.TokenType.ATRIB:
                            atrib = True
                        cont += 1
                    
                    if atrib:
                        last_ident = token_atual
                    elif reading_input:
                        self.code.append('ARMZ {}'.format(self.symbol_table[token_atual.value].address))
                        reading_input = False
                    else:
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
                    self.code.append('ARMZ {}'.format(self.symbol_table[last_ident.value].address))

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
            inst_number = 0
            for inst in self.code:
                print('{}. {}'.format(inst_number, inst))
                inst_number += 1
        
        return self.code