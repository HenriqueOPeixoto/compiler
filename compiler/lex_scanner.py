import my_token

EOF = -1
DIGIT = 1
NOT_DIGIT = 2

class LexScanner:

    content = ""
    state = 0
    pos = 0

    def __init__(self, content) -> None:
        self.content = content

    def next_token(self) -> my_token.Token:
        buffer = []
        while (True):
            c = self.content[self.pos]

            if self.state == 0:
                if c.isnumeric():
                    buffer.append(c)
                    self.state = DIGIT
            elif self.state == DIGIT:
                if c.isnumeric():
                    buffer.append(c)
                else:
                    self.state = NOT_DIGIT
            elif self.state == NOT_DIGIT:
                return my_token.Token(int(buffer), DIGIT)
            
            self.pos += 1

            print(buffer)

            if self.pos == len(self.content):
                return my_token.Token("", EOF)


