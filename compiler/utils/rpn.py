# Um port da minha implementação de RPN em Rust na disciplina de Comp I

import my_token

MIN_PRIORITY = 0 # Used in + and -
MED_PRIORITY = 1 # Used in * and /
MAX_PRIORITY = 2 # Used in ^
UNARY_PRIORITY = 3 # Used in exp[]

def get_precedence(op: str):
    if op == "+" or op == "-":
        return MIN_PRIORITY
    elif op == "*" or op == "/":
        return MED_PRIORITY
    elif op == "^":
        return MAX_PRIORITY
    elif op == "exp":
        return UNARY_PRIORITY
    else:
        return -1;
    


def shunting_yard(tokens: 'list[my_token.Token]'):

    out:'list[my_token.Token]' = []
    stack:'list[my_token.Token]' = []
    precedence = -1

    #tokens.append(my_token.Token('$', my_token.TokenType.EOF))

    for token in tokens:
        if (token.type == my_token.TokenType.DIGIT or
        token.type == my_token.TokenType.REAL_NUM or
        token.type == my_token.TokenType.IDENT):
            out.append(token)
        elif token.type == my_token.TokenType.OPERATOR:
            if token.value == '+' or token.value == '-':
                if len(stack) > 0:
                    precedence = get_precedence(stack[-1])
                else:
                    precedence == -1

                if precedence > MIN_PRIORITY:
                    while len(stack) > 0:
                        if get_precedence(stack[-1].value) <= MIN_PRIORITY:
                            break

                        out.append(stack.pop())
                stack.append(token)
            
            elif token.value == '*' or token.value == '/':
                if len(stack) > 0:
                    precedence = get_precedence(stack[-1])
                else:
                    precedence == -1

                if precedence > MED_PRIORITY:
                    while len(stack) > 0:
                        if get_precedence(stack[-1].value) <= MED_PRIORITY:
                            break

                        out.append(stack.pop())
                stack.append(token)
            
            elif token.value == '^':
                if len(stack) > 0:
                    precedence = get_precedence(stack[-1])
                else:
                    precedence == -1

                if precedence > MAX_PRIORITY:
                    while len(stack) > 0:
                        if get_precedence(stack[-1].value) <= MAX_PRIORITY:
                            break

                        out.append(stack.pop())
                stack.append(token)
        elif token.type == my_token.TokenType.OPEN_PAR:
            stack.append(token)
        elif token.type == my_token.TokenType.CLOSE_PAR:
            while len(stack) > 0:
                if stack[-1].type != my_token.TokenType.OPEN_PAR:
                    out.append(stack.pop())
                else:
                    stack.pop()
                    break
        elif (token.type == my_token.TokenType.NEWLINE_TOKEN or
            token.type == my_token.TokenType.EOF):
            while len(stack) > 0:
                out.append(stack.pop())
            out.append(token)
        # EXP não foi implementado nessa linguagem

    while len(stack) > 0:
        out.append(stack.pop())
    
    return out