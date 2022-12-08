# Regras
PROGRAMA = 0
CORPO = 1
DC = 2
MAIS_DC = 3
DC_V = 4
TIPO_VAR = 5
VARIAVEIS = 6
MAIS_VAR = 7
COMANDOS = 8
MAIS_COMANDOS = 9
COMANDO = 10
CONDICAO = 11
RELACAO = 12
EXPRESSAO = 13
TERMO = 14
OP_UN = 15
FATOR = 16
OUTROS_TERMOS = 17
OP_AD = 18
MAIS_FATORES = 19
OP_MUL = 20
PFALSA = 21

# Terminais
T_PROGRAM = 0 # program
T_DOT = 1 # .
T_BEGIN = 2
T_END = 3
T_EOF = 4 # @, provavelmente não será usado
T_SEMICOLON = 5
T_COLON = 6
T_REAL = 7 # real
T_INTEGER = 8 # integer
T_IDENT = 9
T_COMMA = 10
T_READ = 11
T_WRITE = 12
T_OPEN_PAR = 13 # (
T_CLOSE_PAR = 14 # )
T_IF = 15
T_THEN = 16
T_CLOSE_BLOCK = 17 # $ SYMBOL
T_WHILE = 18
T_DO = 19
T_EQUAL = 20
T_UNEQUAL = 21
T_GREATER_OR_EQUAL = 22
T_LESS_OR_EQUAL = 23
T_GREATER = 24
T_LESS = 25
T_MINUS = 26 # -
T_NUMERO_INT = 27 # Qualquer número inteiro
T_NUMERO_REAL = 28 # Qualquer número real
T_PLUS = 29 # +
T_MUL = 30 # *
T_DIV = 31 # /
T_ELSE = 32

parse_table = [
['program ident <corpo>','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
['','', '<dc> begin <comandos> end','','','','', '<dc> begin <comandos> end', '<dc> begin <comandos> end','','','','','','','','','','','','','','','','','','','','','','','',''],
['','', 'λ', '','','','', '<dc_v> <mais_dc>','<dc_v> <mais_dc>','','','','','','','','','','','','','','','','','','','','','','','',''],
['','','λ','','','; <dc>','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
['','','','','','','','<tipo_var> : <variaveis>','<tipo_var> : <variaveis>','','','','','','','','','','','','','','','','','','','','','','','',''],
['','','','','','','','real','integer','','','','','','','','','','','','','','','','','','','','','','','',''],
['','','','','','','','','', 'ident <mais_var>','','','','','','','','','','','','','','','','','','','','','','',''],
['','','λ','','','λ','','','','',', <variaveis>','','','','','','','','','','','','','','','','','','','','','',''],
['','','','','','','','','','<comando> <mais_comandos>','','<comando> <mais_comandos>','<comando> <mais_comandos>','','','<comando> <mais_comandos>','','','<comando> <mais_comandos>','','','','','','','','','','','','','',''],
['','','','λ','','; <comandos>','','','','','','','','','','','','λ','','','','','','','','','','','','','','','λ'],
['','','','','','','','','','ident := <expressao>','','read ( ident )','write ( ident )','','','if <condicao> do <comandos> <pfalsa> $','','','while <condicao> do <comandos> $','','','','','','','','','','','','','',''],
['','','','','','','','','','<expressao> <relacao> <expressao>','','','','<expressao> <relacao> <expressao>','','','','','','','','','','','','','<expressao> <relacao> <expressao>','<expressao> <relacao> <expressao>','<expressao> <relacao> <expressao>','','','',''],
['','','','','','','','','','','','','','','','','','','','','=','<>','>=','<=','>','<','','','','','','',''],
['','','','','','','','','','<termo> <outros_termos>','','','','<termo> <outros_termos>','','','','','','','','','','','','','<termo> <outros_termos>','<termo> <outros_termos>','<termo> <outros_termos>','','','',''],
['','','','','','','','','','<op_un> <fator> <mais_fatores>','','','','<op_un> <fator> <mais_fatores>','','','','','','','','','','','','','<op_un> <fator> <mais_fatores>','<op_un> <fator> <mais_fatores>','<op_un> <fator> <mais_fatores>','','','',''],
['','','','','','','','','','λ','','','','λ','','','','','','','','','','','','','-','λ','λ','','','',''],
['','','','','','','','','','ident','','','','( <expressao> )','','','','','','','','','','','','','','numero_int','numero_real','','','',''],
['','','','λ','','λ','','','','','','','','','λ','','λ','λ','','λ','λ','λ','λ','λ','λ','λ','<op_ad> <termo> <outros_termos>','','','<op_ad> <termo> <outros_termos>','','','λ'],
['','','','','','','','','','','','','','','','','','','','','','','','','','','-','','','+','','',''],
['','','','λ','','λ','','','','','','','','','λ','','λ','λ','','λ','λ','λ','λ','λ','λ','λ','λ','','','λ','<op_mul> <fator> <mais_fatores>','<op_mul> <fator> <mais_fatores>','λ'],
['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','*','/',''],
['','','','','','','','','','','','','','','','','','λ','','','','','','','','','','','','','','','else <comandos>']
]