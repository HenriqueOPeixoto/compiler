# Chama o interpretador para executar o código

import argparse
import interpreter

def parse_cmd_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='The path to the file you wish to compile.')
    args = parser.parse_args()
    return args

args = parse_cmd_args()

try:
    input_file = open(args.file, 'r')
    
    obj_code_str = input_file.read()
    obj_code = obj_code_str.split('\n')

    runner = interpreter.Interpreter(obj_code)
    runner.execute()

    input_file.close()
except FileNotFoundError as e:
    print(e)
