import my_token

COMMENT = -2
EOF = -1
DIGIT = 1
NOT_DIGIT = 2
SPACE = 3
NOT_SPACE = 4
NEWLINE_TOKEN = 5
OPERATOR = 6
TXT_LITERAL = 7
NOT_TXT_LITERAL = 8
KEYWORD = 9
IDENT = 10
LOGICAL_OP = 11
NOT_LOGICAL_OP = 12
ATRIB = 13
NOT_ATRIB = 14
SEPARATOR = 15

OPERATOR_LIST = ['+', '-', '*', '/']
COMMENT_LIST = ['{']
KEYWORD_LIST = [
    'program',
    'begin',
    'end',
    'real',
    'integer',
    'read',
    'write',
    'if',
    'then',
    'else',
    'while',
    'do'
]
LOGICAL_OP_LIST = ['<', '>', '<>', '>=', '<=', '=']
SEPARATOR_LIST = [',', ';', '$', '.']

class LexScanner:

    content = ""
    state = 0
    pos = 0

    def __init__(self, content) -> None:
        self.content = content + '\0'

    def is_end(self, c: chr) -> bool:
        if c == '\0':
            return True
        
        return False

    def next_token(self) -> my_token.Token:
        buffer = []

        if self.pos == len(self.content):
            return my_token.Token('$', EOF)
        
        if self.is_end(self.content[self.pos]):
            return my_token.Token('$', EOF)

        self.state = 0
        
        while (True):
            c = self.content[self.pos]

            if self.state == 0:
                if c.isnumeric():
                    buffer.append(c)
                    self.state = DIGIT

                elif c in [' ', '\n']:
                    buffer.append(c)
                    self.state = SPACE

                elif c in OPERATOR_LIST:
                    if c == '/':
                        self.pos += 1 # Avança uma pos para verificar se é comentário
                        if self.content[self.pos] == '*':
                            self.state = COMMENT
                            continue
                        else:
                            self.pos -= 1 # Volta para a posição inicial se não for
                    buffer.append(c)
                    self.state = OPERATOR

                elif c in COMMENT_LIST:
                    self.state = COMMENT
                
                elif c in LOGICAL_OP_LIST:
                    buffer.append(c)
                    self.state = LOGICAL_OP
                
                elif c.isalpha():
                    buffer.append(c)
                    self.state = TXT_LITERAL
                
                elif c == ':':
                    buffer.append(c)
                    self.state = ATRIB
                
                elif c in SEPARATOR_LIST:
                    buffer.append(c)
                    self.state = SEPARATOR
                        

                # ===================END OF STATE 0 ====================
                
                # =================== DIGIT ====================
            elif self.state == DIGIT:
                if c.isnumeric():
                    buffer.append(c)
                else:
                    self.state = NOT_DIGIT

            elif self.state == NOT_DIGIT:
                self.pos -= 1
                return my_token.Token(int("".join(buffer)), DIGIT)
            
            # =================== SPACE ====================

            elif self.state == SPACE:
                if c in [' ', '\n']:
                    buffer.append(c)
                    self.state = SPACE
                else:
                    self.state = NOT_SPACE

            elif self.state == NOT_SPACE:
                self.pos -= 1
                if '\n' in buffer:
                    return my_token.Token(buffer, NEWLINE_TOKEN)
                else:
                    return my_token.Token(buffer, SPACE)

            # =================== OPERATOR ====================

            elif self.state == OPERATOR:
                return my_token.Token(''.join(buffer), OPERATOR)
            
            # =================== COMMENT ====================

            elif self.state == COMMENT:
                if c == '*':
                    self.pos += 1 # Avança uma posição para verificar se há é comentário
                    if self.content[self.pos] == '/':
                        self.pos += 1
                        return my_token.Token('', COMMENT)
                    else:
                        self.pos -= 1 # Volta para a posição inicial se não for
                elif c == '}':
                    return my_token.Token('', COMMENT)

            # =================== LOGICAL OP ====================

            elif self.state == LOGICAL_OP:
                if c in LOGICAL_OP_LIST:
                    buffer.append(c)
                else:
                    self.state = NOT_LOGICAL_OP
            
            elif self.state == NOT_LOGICAL_OP:
                self.pos -= 1
                return my_token.Token(''.join(buffer), LOGICAL_OP)

            # =================== TXT LITERAL OR IDENT ====================
            
            elif self.state == TXT_LITERAL:
                if c.isalnum():
                    buffer.append(c)
                else:
                    self.state = NOT_TXT_LITERAL
            
            elif self.state == NOT_TXT_LITERAL:
                self.pos -= 1
                buffer = ''.join(buffer)
                if buffer in KEYWORD_LIST:
                    return my_token.Token(buffer, KEYWORD)
                else:
                    return my_token.Token(buffer, IDENT)

            # =================== ATRIB ====================

            elif self.state == ATRIB:
                if c == '=':
                    buffer.append(c)
                else:
                    self.state = NOT_ATRIB
            
            elif self.state == NOT_ATRIB:
                self.pos -= 1
                buffer = ''.join(buffer)
                if buffer in [':', ':=']:
                    return my_token.Token(buffer, ATRIB)
                else:
                    raise Exception('Erro: Esperava um token de atribuição.')

            # =================== SEPARATOR ====================

            elif self.state == SEPARATOR:
                return my_token.Token(''.join(buffer), SEPARATOR)


            self.pos += 1

            if self.is_end(c):
                if self.state != OPERATOR:
                    self.state -= 1
                
                return my_token.Token(''.join(buffer), self.state) # Sai do estado NOT_X e vai para o X.


