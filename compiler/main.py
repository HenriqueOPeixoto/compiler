# Library to process command line arguments
import argparse
import lex_scanner

# Parse aguments inserted via command line interface
def parse_cmd_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='The path to the file you wish to compile.')
    args = parser.parse_args()
    return args

args = parse_cmd_args()

try:
    input_file = open(args.file, 'r')
    
    lex_scanner.next_token(content=input_file)

    input_file.close()

except FileNotFoundError:
    print('Não foi possível encontrar o arquivo especificado.')
