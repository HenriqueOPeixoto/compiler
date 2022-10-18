import my_token

EOF = -1
DIGIT = 1
NOT_DIGIT = 2

class LexScanner:

    content = ""
    pos = 0

    def __init__(self, content) -> None:
        self.content = content

    def next_token(self) -> my_token.Token:
        state = 0
        buffer = []
        while (True):
            c = self.content[self.pos]

            if state == 0:
                if c.isnumeric():
                    buffer.append(c)
                    state = DIGIT
            elif state == DIGIT:
                if c.isnumeric():
                    buffer.append(c)
                else:
                    state = NOT_DIGIT
            elif state == NOT_DIGIT:
                return my_token.Token(int("".join(buffer)), DIGIT)
            
            self.pos += 1

            print(buffer)

            if self.pos == len(self.content):
                return my_token.Token("", EOF)


