from enum import IntEnum

class Token:

    def __init__(self, value, type) -> None:
        self.value = value
        self.type = type

    # Prints token type full name
    def to_string(self) -> str:
        return '[{}: {}]'.format(self.value, self.type.name)
    
    # Only prints token type codes
    def to_string_brief(self) -> str:
        return '[{}: {}]'.format(self.value, self.type)

# This class contains token type enumerations..
# All types that start with NOT_ are states used by the LexScanner class.
class TokenType(IntEnum):
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