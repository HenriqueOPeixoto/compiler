import my_token

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
            return my_token.Token('$', my_token.TokenType.EOF)
        
        if self.is_end(self.content[self.pos]):
            return my_token.Token('$', my_token.TokenType.EOF)

        self.state = 0
        
        while (True):
            c = self.content[self.pos]

            if self.state == 0:
                if c.isnumeric():
                    buffer.append(c)
                    self.state = my_token.TokenType.DIGIT

                elif c in [' ', '\n']:
                    buffer.append(c)
                    self.state = my_token.TokenType.SPACE

                elif c in OPERATOR_LIST:
                    if c == '/':
                        self.pos += 1 # Avança uma pos para verificar se é comentário
                        if self.content[self.pos] == '*':
                            self.state = my_token.TokenType.COMMENT
                            continue
                        else:
                            self.pos -= 1 # Volta para a posição inicial se não for
                    buffer.append(c)
                    self.state = my_token.TokenType.OPERATOR

                elif c in COMMENT_LIST:
                    self.state = my_token.TokenType.COMMENT
                
                elif c in LOGICAL_OP_LIST:
                    buffer.append(c)
                    self.state = my_token.TokenType.LOGICAL_OP
                
                elif c.isalpha():
                    buffer.append(c)
                    self.state = my_token.TokenType.TXT_LITERAL
                
                elif c == ':':
                    buffer.append(c)
                    self.state = my_token.TokenType.ATRIB
                
                elif c in SEPARATOR_LIST:
                    buffer.append(c)
                    self.state = my_token.TokenType.SEPARATOR
                        

                # ===================END OF STATE 0 ====================
                
                # =================== DIGIT ====================
            elif self.state == my_token.TokenType.DIGIT:
                if c.isnumeric():
                    buffer.append(c)
                else:
                    self.state = my_token.TokenType.NOT_DIGIT

            elif self.state == my_token.TokenType.NOT_DIGIT:
                self.pos -= 1
                return my_token.Token(int("".join(buffer)), my_token.TokenType.DIGIT)
            
            # =================== SPACE ====================

            elif self.state == my_token.TokenType.SPACE:
                if c in [' ', '\n']:
                    buffer.append(c)
                    self.state = my_token.TokenType.SPACE
                else:
                    self.state = my_token.TokenType.NOT_SPACE

            elif self.state == my_token.TokenType.NOT_SPACE:
                self.pos -= 1
                if '\n' in buffer:
                    return my_token.Token(buffer, my_token.TokenType.NEWLINE_TOKEN)
                else:
                    return my_token.Token(buffer, my_token.TokenType.SPACE)

            # =================== OPERATOR ====================

            elif self.state == my_token.TokenType.OPERATOR:
                return my_token.Token(''.join(buffer), my_token.TokenType.OPERATOR)
            
            # =================== COMMENT ====================

            elif self.state == my_token.TokenType.COMMENT:
                if c == '*':
                    self.pos += 1 # Avança uma posição para verificar se há é comentário
                    if self.content[self.pos] == '/':
                        self.pos += 1
                        return my_token.Token('', my_token.TokenType.COMMENT)
                    else:
                        self.pos -= 1 # Volta para a posição inicial se não for
                elif c == '}':
                    return my_token.Token('', my_token.TokenType.COMMENT)

            # =================== LOGICAL OP ====================

            elif self.state == my_token.TokenType.LOGICAL_OP:
                if c in LOGICAL_OP_LIST:
                    buffer.append(c)
                else:
                    self.state = my_token.TokenType.NOT_LOGICAL_OP
            
            elif self.state == my_token.TokenType.NOT_LOGICAL_OP:
                self.pos -= 1
                return my_token.Token(''.join(buffer), my_token.TokenType.LOGICAL_OP)

            # =================== TXT LITERAL OR IDENT ====================
            
            elif self.state == my_token.TokenType.TXT_LITERAL:
                if c.isalnum():
                    buffer.append(c)
                else:
                    self.state = my_token.TokenType.NOT_TXT_LITERAL
            
            elif self.state == my_token.TokenType.NOT_TXT_LITERAL:
                self.pos -= 1
                buffer = ''.join(buffer)
                if buffer in KEYWORD_LIST:
                    return my_token.Token(buffer, my_token.TokenType.KEYWORD)
                else:
                    return my_token.Token(buffer, my_token.TokenType.IDENT)

            # =================== ATRIB ====================

            elif self.state == my_token.TokenType.ATRIB:
                if c == '=':
                    buffer.append(c)
                else:
                    self.state = my_token.TokenType.NOT_ATRIB
            
            elif self.state == my_token.TokenType.NOT_ATRIB:
                self.pos -= 1
                buffer = ''.join(buffer)
                if buffer in [':', ':=']:
                    return my_token.Token(buffer, my_token.TokenType.ATRIB)
                else:
                    raise Exception('Erro: Esperava um token de atribuição.')

            # =================== SEPARATOR ====================

            elif self.state == my_token.TokenType.SEPARATOR:
                return my_token.Token(''.join(buffer), my_token.TokenType.SEPARATOR)


            self.pos += 1

            if self.is_end(c):
                if self.state != my_token.TokenType.OPERATOR:
                    self.state -= 1
                
                return my_token.Token(''.join(buffer), self.state) # Sai do estado NOT_X e vai para o X.


