import token

def next_token(content:str) -> 'list[token.Token]':
    tokens = []
    
    for char in content:
        a = token.Token(char, 0)
        tokens.append(a)

    for elem in tokens:
        print(elem.to_string())
    return tokens
