import my_token
from parse_error import ParseError
from semantic_error import SemanticError
from symbol_struct import SymbolTableData # Define o formato das entradas na symbol table

from parse_table import *

class Parser:

    def __init__(self, tokens: 'list[my_token.Token]', filename) -> None:
        self.tokens = tokens
        self.stack = None
        self.linenum = 1
        self.filename = filename
        self.symbol_table = {}
        
        self.var_type = None
        self.define_type = False # Determina se deve definir o tipo de uma var
        self.atrib = None # Determina se deve atribuir valor a uma var
        self.negation = False # determina se o - indica uma inversão de sinal

    def derivate(self, rule, terminal):
        self.stack.pop()
        derivation = parse_table[rule][terminal].split(' ')
        if 'λ' not in derivation:
            derivation.reverse()
            self.stack.extend(derivation)
    
    def match(self):
        self.stack.pop()
        #self.tokens.pop()
        self.pos += 1


    def parse_syntax(self, print_steps=False, print_symbols=False):

        accepted = False
        self.stack = ['<programa>', '.']
        self.stack.reverse()
        #self.tokens.reverse() # makes tokens look like a stack
        self.pos = 0

        address = 0 # contador de endereço

        while self.stack[0] != '.' or accepted == False:

            token_atual = self.tokens[self.pos]
            
            if print_steps:
                print(token_atual.to_string(), self.stack[-1])

            if token_atual.type == my_token.TokenType.KEYWORD:
                if token_atual.value == 'program':
                    if self.stack[-1] == '<programa>':
                        self.derivate(PROGRAMA, T_PROGRAM)
                    elif self.stack[-1] == 'program':
                        self.define_type = True
                        self.var_type = self.stack[-1]
                        self.match()
                    else:
                        raise ParseError('Era esperado um token da regra {}, mas recebi {}'.format(self.stack[-1], token_atual.to_string()), self.filename, self.linenum)
                
                
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
                        raise ParseError('Era esperado um token da regra {}, mas recebi {}'.format(self.stack[-1], token_atual.to_string()), self.filename, self.linenum)
                
                elif token_atual.value == 'end':
                    if self.stack[-1] == '<mais_comandos>':
                        self.derivate(MAIS_COMANDOS, T_END)
                    elif self.stack[-1] == '<outros_termos>':
                        self.derivate(OUTROS_TERMOS, T_END)
                    elif self.stack[-1] == '<mais_fatores>':
                        self.derivate(MAIS_FATORES, T_END)
                    elif self.stack[-1] == 'end':
                        self.match()

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
                        self.define_type = True
                        self.var_type = self.stack[-1] # Type definition
                        self.match()
                    else:
                        raise ParseError('Era esperado um token da regra {}, mas recebi {}'.format(self.stack[-1], token_atual.to_string()), self.filename, self.linenum)
                    
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
                        self.define_type = True
                        self.var_type = self.stack[-1] # Type definition
                        self.match()
                    else:
                        raise ParseError('Era esperado um token da regra {}, mas recebi {}'.format(self.stack[-1], token_atual.to_string()), self.filename, self.linenum)
                
                elif token_atual.value == 'read':
                    if self.stack[-1] == '<comandos>':
                        self.derivate(COMANDOS, T_READ)
                    elif self.stack[-1] == '<comando>':
                        self.derivate(COMANDO, T_READ)
                    elif self.stack[-1] == 'read':
                        self.match()
                    else:
                        raise ParseError('Era esperado um token da regra {}, mas recebi {}'.format(self.stack[-1], token_atual.to_string()), self.filename, self.linenum)
                
                elif token_atual.value == 'write':
                    if self.stack[-1] == '<comandos>':
                        self.derivate(COMANDOS, T_WRITE)
                    elif self.stack[-1] == '<comando>':
                        self.derivate(COMANDO, T_WRITE)
                    elif self.stack[-1] == 'write':
                        self.match()
                    else:
                        raise ParseError('Era esperado um token da regra {}, mas recebi {}'.format(self.stack[-1], token_atual.to_string()), self.filename, self.linenum)
                
                elif token_atual.value == 'if':
                    if self.stack[-1] == '<comandos>':
                        self.derivate(COMANDOS, T_IF)
                    elif self.stack[-1] == '<comando>':
                        self.derivate(COMANDO, T_IF)
                    elif self.stack[-1] == 'if':
                        self.match()
                    else:
                        raise ParseError('Era esperado um token da regra {}, mas recebi {}'.format(self.stack[-1], token_atual.to_string()), self.filename, self.linenum)
                
                elif token_atual.value == 'then':
                    if self.stack[-1] == '<outros_termos>':
                        self.derivate(OUTROS_TERMOS, T_THEN)
                    elif self.stack[-1] == '<mais_fatores>':
                        self.derivate(MAIS_FATORES, T_THEN)
                    elif self.stack[-1] == 'then':
                        self.match()
                    else:
                        raise ParseError('Era esperado um token da regra {}, mas recebi {}'.format(self.stack[-1], token_atual.to_string()), self.filename, self.linenum)

                elif token_atual.value == 'while':
                    if self.stack[-1] == '<comandos>':
                        self.derivate(COMANDOS, T_WHILE)
                    elif self.stack[-1] == '<comando>':
                        self.derivate(COMANDO, T_WHILE)
                    elif self.stack[-1] == 'while':
                        self.match()
                    else:
                        raise ParseError('Era esperado um token da regra {}, mas recebi {}'.format(self.stack[-1], token_atual.to_string()), self.filename, self.linenum)
                
                elif token_atual.value == 'do':
                    if self.stack[-1] == '<outros_termos>':
                        self.derivate(OUTROS_TERMOS, T_DO)
                    elif self.stack[-1] == '<mais_fatores>':
                        self.derivate(MAIS_FATORES, T_DO)
                    elif self.stack[-1] == 'do':
                        self.match()
                    else:
                        raise ParseError('Era esperado um token da regra {}, mas recebi {}'.format(self.stack[-1], token_atual.to_string()), self.filename, self.linenum)
                
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
                    else:
                        raise ParseError('Era esperado um token da regra {}, mas recebi {}'.format(self.stack[-1], token_atual.to_string()), self.filename, self.linenum)

            elif token_atual.type == my_token.TokenType.IDENT:
                if self.stack[-1] == '<variaveis>':
                    self.derivate(VARIAVEIS, T_IDENT)
                elif self.stack[-1] == '<comandos>':
                    self.derivate(COMANDOS, T_IDENT)
                elif self.stack[-1] == '<comando>':
                    self.derivate(COMANDO, T_IDENT)
                elif self.stack[-1] == '<condicao>':
                    self.derivate(CONDICAO, T_IDENT)
                elif self.stack[-1] == '<expressao>':
                    self.derivate(EXPRESSAO, T_IDENT)
                elif self.stack[-1] == '<termo>':
                    self.derivate(TERMO, T_IDENT)
                elif self.stack[-1] == '<op_un>':
                    self.derivate(OP_UN, T_IDENT)
                elif self.stack[-1] == '<fator>':
                    self.derivate(FATOR, T_IDENT)
                elif self.stack[-1] == 'ident':
                    if self.define_type:
                        if token_atual.value in self.symbol_table:
                            raise SemanticError('Um identificador com o nome \'{}\' já existe.'.format(token_atual.value), self.filename, self.linenum)
                        symbol_details = SymbolTableData(self.var_type, address)
                        self.symbol_table[token_atual.value] = symbol_details # Var type é definido de acordo com
                                                                             # o token mais recente, real ou integer.
                        address += 1
                    self.match()
                else:
                        raise ParseError('Era esperado um token da regra {}, mas recebi {}'.format(self.stack[-1], token_atual.to_string()), self.filename, self.linenum)

            elif (token_atual.type == my_token.TokenType.SPACE or
                token_atual.type == my_token.TokenType.COMMENT):
                #self.tokens.pop()
                self.pos += 1
            
            elif token_atual.type == my_token.TokenType.NEWLINE_TOKEN:
                self.linenum += 1
                #self.tokens.pop()
                self.pos += 1
            
            elif token_atual.type == my_token.TokenType.ATRIB:
                if token_atual.value == ':' and self.stack[-1] == ':':
                    self.match()
                elif token_atual.value == ':=' and self.stack[-1] == ':=':
                    self.match()
                else:
                        raise ParseError('Era esperado um token da regra {}, mas recebi {}'.format(self.stack[-1], token_atual.to_string()), self.filename, self.linenum)
            
            elif token_atual.type == my_token.TokenType.SEPARATOR:
                if token_atual.value == ',':
                    if self.stack[-1] == '<mais_var>':
                        self.derivate(MAIS_VAR, T_COMMA)
                    elif self.stack[-1] == ',':
                        self.match()
                    else:
                        raise ParseError('Era esperado um token da regra {}, mas recebi {}'.format(self.stack[-1], token_atual.to_string()), self.filename, self.linenum)

                elif token_atual.value == ';':
                    if self.stack[-1] == '<mais_dc>':
                        self.derivate(MAIS_DC, T_SEMICOLON)
                    elif self.stack[-1] == '<mais_var>':
                        self.derivate(MAIS_VAR, T_SEMICOLON)
                    elif self.stack[-1] == '<mais_comandos>':
                        self.derivate(MAIS_COMANDOS, T_SEMICOLON)
                    elif self.stack[-1] == '<outros_termos>':
                        self.derivate(OUTROS_TERMOS, T_SEMICOLON)
                    elif self.stack[-1] == '<mais_fatores>':
                        self.derivate(MAIS_FATORES, T_SEMICOLON)
                    elif self.stack[-1] == ';':
                        self.define_type = False
                        self.var_type = None # Resets the var type
                        self.match()
                    else:
                        raise ParseError('Era esperado um token da regra {}, mas recebi {}'.format(self.stack[-1], token_atual.to_string()), self.filename, self.linenum)
                
                elif token_atual.value == '$':
                    if self.stack[-1] == '<mais_comandos>':
                        self.derivate(MAIS_COMANDOS, T_CLOSE_BLOCK)
                    elif self.stack[-1] == '<outros_termos>':
                        self.derivate(OUTROS_TERMOS, T_CLOSE_BLOCK)
                    elif self.stack[-1] == '<mais_fatores>':
                        self.derivate(MAIS_FATORES, T_CLOSE_BLOCK)
                    elif self.stack[-1] == '<pfalsa>':
                        self.derivate(PFALSA, T_CLOSE_BLOCK)
                    elif self.stack[-1] == '$':
                        self.match()
                    else:
                        raise ParseError('Era esperado um token da regra {}, mas recebi {}'.format(self.stack[-1], token_atual.to_string()), self.filename, self.linenum)

                elif token_atual.value == '.':
                    if self.stack[-1] == '.' and len(self.stack) == 1:
                        accepted = True
                    else:
                        raise ParseError('Era esperado um token da regra {}, mas recebi {}'.format(self.stack[-1], token_atual.to_string()), self.filename, self.linenum)

            elif token_atual.type == my_token.TokenType.OPEN_PAR:
                if token_atual.value == '(':
                    if self.stack[-1] == '<condicao>':
                        self.derivate(CONDICAO, T_OPEN_PAR)
                    elif self.stack[-1] == '<expressao>':
                        self.derivate(EXPRESSAO, T_OPEN_PAR)
                    elif self.stack[-1] == '<termo>':
                        self.derivate(TERMO, T_OPEN_PAR)
                    elif self.stack[-1] == '<op_un>':
                        self.derivate(OP_UN, T_OPEN_PAR)
                    elif self.stack[-1] == '<fator>':
                        self.derivate(FATOR, T_OPEN_PAR)
                    elif self.stack[-1] == '(':
                        self.match()
                    else:
                        raise ParseError('Era esperado um token da regra {}, mas recebi {}'.format(self.stack[-1], token_atual.to_string()), self.filename, self.linenum)
            
            elif token_atual.type == my_token.TokenType.CLOSE_PAR:
                if token_atual.value == ')':
                    if self.stack[-1] == '<outros_termos>':
                        self.derivate(OUTROS_TERMOS, T_CLOSE_PAR)
                    elif self.stack[-1] == '<mais_fatores>':
                        self.derivate(MAIS_FATORES, T_CLOSE_PAR)
                    elif self.stack[-1] == ')':
                        self.match()
                    else:
                        raise ParseError('Era esperado um token da regra {}, mas recebi {}'.format(self.stack[-1], token_atual.to_string()), self.filename, self.linenum)
            
            elif token_atual.type == my_token.TokenType.OPERATOR:
                if token_atual.value == '*':
                    if self.stack[-1] == '<mais_fatores>':
                        self.derivate(MAIS_FATORES, T_MUL)
                    elif self.stack[-1] == '<op_mul>':
                        self.derivate(OP_MUL, T_MUL)
                    elif self.stack[-1] == '*':
                        self.match()
                    else:
                        raise ParseError('Era esperado um token da regra {}, mas recebi {}'.format(self.stack[-1], token_atual.to_string()), self.filename, self.linenum)
                
                elif token_atual.value == '/':
                    if self.stack[-1] == '<mais_fatores>':
                        self.derivate(MAIS_FATORES, T_DIV)
                    elif self.stack[-1] == '<op_mul>':
                        self.derivate(OP_MUL, T_DIV)
                    elif self.stack[-1] == '/':
                        self.match()
                    else:
                        raise ParseError('Era esperado um token da regra {}, mas recebi {}'.format(self.stack[-1], token_atual.to_string()), self.filename, self.linenum)
                
                elif token_atual.value == '+':
                    if self.stack[-1] == '<outros_termos>':
                        self.derivate(OUTROS_TERMOS, T_PLUS)
                    elif self.stack[-1] == '<op_ad>':
                        self.derivate(OP_AD, T_PLUS)
                    elif self.stack[-1] == '<mais_fatores>':
                        self.derivate(MAIS_FATORES, T_PLUS)
                    elif self.stack[-1] == '+':
                        self.match()
                    else:
                        raise ParseError('Era esperado um token da regra {}, mas recebi {}'.format(self.stack[-1], token_atual.to_string()), self.filename, self.linenum)
                
                elif token_atual.value == '-':
                    if self.stack[-1] == '<condicao>':
                        self.derivate(CONDICAO, T_MINUS)
                    elif self.stack[-1] == '<expressao>':
                        self.derivate(EXPRESSAO, T_MINUS)
                    elif self.stack[-1] == '<termo>':
                        self.derivate(TERMO, T_MINUS)
                    elif self.stack[-1] == '<op_un>':
                        self.negation = True
                        self.derivate(OP_UN, T_MINUS)
                    elif self.stack[-1] == '<outros_termos>':
                        self.derivate(OUTROS_TERMOS, T_MINUS)
                    elif self.stack[-1] == '<op_ad>':
                        self.derivate(OP_AD, T_MINUS)
                    elif self.stack[-1] == '<mais_fatores>':
                        self.derivate(MAIS_FATORES, T_MINUS)
                    elif self.stack[-1] == '-':
                        if self.negation:
                            token_atual.type = my_token.TokenType.NEGATION
                            self.negation = False
                        self.match()
                    else:
                        raise ParseError('Era esperado um token da regra {}, mas recebi {}'.format(self.stack[-1], token_atual.to_string()), self.filename, self.linenum)
            
            
            elif token_atual.type == my_token.TokenType.DIGIT:
                if self.stack[-1] == '<condicao>':
                    self.derivate(CONDICAO, T_NUMERO_INT)
                elif self.stack[-1] == '<expressao>':
                    self.derivate(EXPRESSAO, T_NUMERO_INT)
                elif self.stack[-1] == '<termo>':
                    self.derivate(TERMO, T_NUMERO_INT)
                elif self.stack[-1] == '<op_un>':
                    self.derivate(OP_UN, T_NUMERO_INT)
                elif self.stack[-1] == '<fator>':
                    self.derivate(FATOR, T_NUMERO_INT)
                elif self.stack[-1] == 'numero_int':
                    self.match()
                else:
                        raise ParseError('Era esperado um token da regra {}, mas recebi {}'.format(self.stack[-1], token_atual.to_string()), self.filename, self.linenum)
            
            elif token_atual.type == my_token.TokenType.REAL_NUM:
                if self.stack[-1] == '<condicao>':
                    self.derivate(CONDICAO, T_NUMERO_REAL)
                elif self.stack[-1] == '<expressao>':
                    self.derivate(EXPRESSAO, T_NUMERO_REAL)
                elif self.stack[-1] == '<termo>':
                    self.derivate(TERMO, T_NUMERO_REAL)
                elif self.stack[-1] == '<op_un>':
                    self.derivate(OP_UN, T_NUMERO_REAL)
                elif self.stack[-1] == '<fator>':
                    self.derivate(FATOR, T_NUMERO_REAL)
                elif self.stack[-1] == 'numero_real':
                    self.match()
                else:
                        raise ParseError('Era esperado um token da regra {}, mas recebi {}'.format(self.stack[-1], token_atual.to_string()), self.filename, self.linenum)

            elif token_atual.type == my_token.TokenType.LOGICAL_OP:
                logical_op_list = ['=', '<>', '>=', '<=', '>', '<']

                # Gets the starting index of the logical operators on the parse table
                start_of_logical_operators = T_EQUAL

                # returns the offset of the operator compared to EQUAL on parse table
                op_offset = logical_op_list.index(token_atual.value)

                logical_op = start_of_logical_operators + op_offset

                if self.stack[-1] == '<relacao>':
                    self.derivate(RELACAO, logical_op)
                elif self.stack[-1] == '<outros_termos>':
                    self.derivate(OUTROS_TERMOS, logical_op)
                elif self.stack[-1] == '<mais_fatores>':
                    self.derivate(MAIS_FATORES, logical_op)
                elif self.stack[-1] in logical_op_list:
                    self.match()
                else:
                        raise ParseError('Era esperado um token da regra {}, mas recebi {}'.format(self.stack[-1], token_atual.to_string()), self.filename, self.linenum)

            else:
                print('stack:', self.stack)
                print('last token:', token_atual.to_string())
                break
        
        if print_symbols:
            print('|-Imprimindo tabela de símbolos:\n')
            print(self.symbol_table)

        return self.symbol_table
                        
