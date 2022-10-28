import my_token

EOF = -1
DIGIT = 1
NOT_DIGIT = 2
SPACE = 3
NOT_SPACE = 4
NEWLINE_TOKEN = 5

class LexScanner:

    content = ""
    state = 0
    pos = 0

    def __init__(self, content) -> None:
        self.content = content

    def next_token(self) -> my_token.Token:
        self.state = 0
        buffer = []
        while (True):
            c = self.content[self.pos]

            if self.state == 0:
                if c.isnumeric():
                    buffer.append(c)
                    self.state = DIGIT
                elif c in [' ', '\n']:
                    buffer.append(c)
                    self.state = SPACE
            elif self.state == DIGIT:
                if c.isnumeric():
                    buffer.append(c)
                else:
                    self.state = NOT_DIGIT
            elif self.state == NOT_DIGIT:
                self.pos -= 1
                return my_token.Token(int(buffer), DIGIT)
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
            
            self.pos += 1

            print(buffer)

            if self.pos == len(self.content):
                return my_token.Token("", EOF)


