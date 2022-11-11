# Library to process command line arguments
import argparse
import lex_scanner

# Parse arguments inserted via command line interface
def parse_cmd_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='The path to the file you wish to compile.')
    parser.add_argument('-t', '--tokens', help="Toggles token printing for debugging",
                        action='store_true')
    args = parser.parse_args()
    return args

def print_tokens(tokens):
    line_number = 1
    print('\n{:5d} | '.format(line_number), end=' ')
    for token in tokens:
        if token.type == 5:
            line_number += 1
            print('\n{:5d} | '.format(line_number), end=' ')
        elif token.type != 3:
            print(token.to_string(), end=' ')

args = parse_cmd_args()

try:
    input_file = open(args.file, 'r')
    content = input_file.read()
    
    # lex_scanner.next_token(content=input_file)

    lex = lex_scanner.LexScanner(content)
    tokens = []
    while (True):
        token = lex.next_token()

        if token.type == -1:
            break

        tokens.append(token)

    input_file.close()

    if args.tokens:
        print_tokens(tokens)

except FileNotFoundError:
    print('Não foi possível encontrar o arquivo especificado.')
