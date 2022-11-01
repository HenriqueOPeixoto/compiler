import my_token

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

OPERATOR_LIST = ['+', '-', '*', '/']
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
    'while',
    'do'
]
LOGICAL_OP_LIST = ['<', '>', '<>', '>=', '<=', '=']

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
                    buffer.append(c)
                    self.state = OPERATOR
                elif c.isalpha():
                    buffer.append(c)
                    self.state = TXT_LITERAL
            elif self.state == DIGIT:
                if c.isnumeric():
                    buffer.append(c)
                else:
                    self.state = NOT_DIGIT
            elif self.state == NOT_DIGIT:
                self.pos -= 1
                return my_token.Token(int("".join(buffer)), DIGIT)
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
            elif self.state == OPERATOR:
                return my_token.Token(buffer, OPERATOR)
            elif self.state == TXT_LITERAL:
                if c.isalnum():
                    buffer.append(c)
                else:
                    self.state = NOT_TXT_LITERAL
            elif self.state == NOT_TXT_LITERAL:
                text = ''.join(buffer)
                
                if text in KEYWORD_LIST:
                    return my_token.Token(text, KEYWORD)
                else: 
                    return my_token.Token(text, IDENT)
            
            self.pos += 1

            if self.is_end(c):
                if self.state != OPERATOR:
                    self.state -= 1
                
                return my_token.Token(''.join(buffer), self.state) # Sai do estado NOT_X e vai para o X.


