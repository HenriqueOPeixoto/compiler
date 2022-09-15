# biblioteca robusta de manipulação de argumentos
# Library to process command line arguments
import argparse

# Parse aguments inserted via command line interface
def parse_cmd_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='The path to the file you wish to compile.')
    args = parser.parse_args()
    return args

args = parse_cmd_args()

try:
    input_file = open(args.file, 'r')
    conteudo = input_file.read()
    print(conteudo)

    input_file.close()

except FileNotFoundError:
    print('Não foi possível encontrar o arquivo especificado.')
