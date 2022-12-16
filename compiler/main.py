# Library to process command line arguments
import argparse

import lex_scanner
import syntax_parser
import compiler
import copy # Para não modificar a lista original de tokens

import utils.rpn as rpn # for testing purposes
import sys

DEFAULT_FILENAME = 'out.txt'

# Parse arguments inserted via command line interface
def parse_cmd_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='The path to the file you wish to compile.')
    parser.add_argument('-t', '--tokens', help="Toggles token printing for debugging",
                        action='store_true')
    parser.add_argument('--count', help='Prints identified tokens amount (ignores whitespace and newline tokens)',
                        action='store_true')
    parser.add_argument('-p', '--parse_steps', help='Prints all of the parsing steps',
                        action='store_true')
    parser.add_argument('-s', '--symbols', help='Prints the symbol table',
                        action='store_true')
    parser.add_argument('--rpn', help='Debug RPN implementation, use only for testing. Will stop after lexical analysis. ' + 
                                        'The input file must only include numerical values and operators.',
                        action='store_true')
    parser.add_argument('-c', '--code', help='Prints generated object code to standard output.',
                        action='store_true')
    parser.add_argument('-o', '--output',
                        metavar='FILE', help='Saves generated object code to an output file of your choice')
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
    print()

def print_token_amount(tokens):
    token_amount = 0
    for token in tokens:
        if token.type != 3 and token.type != 5:
            token_amount += 1
    print('Number of identified tokens:', token_amount)

args = parse_cmd_args()

try:
    print('===========================================')
    print('| Compilador LAlg v4 por Henrique Peixoto |')
    print('===========================================\n')

    print('Dica: Digite --help ao iniciar o script para ver uma lista de parâmetros.\n')

    input_file = open(args.file, 'r')
    content = input_file.read()
    
    # lex_scanner.next_token(content=input_file)
    print('Iniciando análise léxica...')
    lex = lex_scanner.LexScanner(content)
    tokens = []
    while (True):
        token = lex.next_token()

        if token.type == -1:
            break

        tokens.append(token)
    
    print('|-Análise Léxica concluída\n')

    input_file.close()

    if args.tokens:
        print_tokens(tokens)

    if args.count:
        print_token_amount(tokens)
    
    if args.rpn:
        print('-> -> -> AVISO: o argumento --rpn encerra a execução após a análise léxica. <- <- <-\n')
        print(rpn.shunting_yard(tokens))
        sys.exit()
        
    
    print('Iniciando Análise Sintática e Semântica...')
    
    parser = syntax_parser.Parser(copy.deepcopy(tokens), input_file.name)
    symbol_table = parser.parse_syntax(print_steps=args.parse_steps, print_symbols=args.symbols)

    print('|-Análise sintática concluída\n')

    print('Iniciando geração de código objeto...')
    comp = compiler.Compiler(tokens, symbol_table)
    obj_code = comp.compile(args.code)
    print('|-Geração de código objeto concluída\n')
    
    obj_code_str = ''
    for inst in obj_code:
        obj_code_str += inst + '\n'

    if args.output is not None:
        try:
            out_file = open(args.output, 'w')
            out_file.write(obj_code_str)
            out_file.close()
        except IOError as e:
            print(e)
    else:
        try:
            out_file = open(DEFAULT_FILENAME, 'w')
            out_file.write(obj_code_str)
            out_file.close()
        except IOError as e:
            print(e)
        

except FileNotFoundError:
    print('Não foi possível encontrar o arquivo especificado.')
