# Regras
T_PROGRAMA = 0

# Terminais


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
['','','','','','','','','','ident := <expressao>','','read (ident)','write (ident)','','','if <condicao> do <comandos> <pfalsa> $','','','while <condicao> do <comandos>$','','','','','','','','','','','','','',''],
['','','','','','','','','','<expressao> <relacao> <expressao>','','','','<expressao> <relacao> <expressao>','','','','','','','','','','','','','<expressao> <relacao> <expressao>','<expressao> <relacao> <expressao>','<expressao> <relacao> <expressao>','','','',''],
['','','','','','','','','','','','','','','','','','','','','=','<>','>=','<=','>','<','','','','','','',''],
['','',,,,,,,,<expressao> -> <termo> <outros_termos>,,,,<expressao> -> <termo> <outros_termos>,,,,,,,,,,,,,<expressao> -> <termo> <outros_termos>,<expressao> -> <termo> <outros_termos>,<expressao> -> <termo> <outros_termos>,,,,]
,,,,,,,,,<termo> -> <op_un> <fator> <mais_fatores>,,,,<termo> -> <op_un> <fator> <mais_fatores>,,,,,,,,,,,,,<termo> -> <op_un> <fator> <mais_fatores>,<termo> -> <op_un> <fator> <mais_fatores>,<termo> -> <op_un> <fator> <mais_fatores>,,,,
,,,,,,,,,<op_un> -> λ,,,,<op_un> -> λ,,,,,,,,,,,,,<op_un> -> -,<op_un> -> λ,<op_un> -> λ,,,,
,,,,,,,,,<fator> -> ident,,,,<fator> -> (<expressao>),,,,,,,,,,,,,,<fator> -> numero_int,<fator> -> numero_real,,,,
,,,<outros_termos> -> λ,,<outros_termos> -> λ,,,,,,,,,<outros_termos> -> λ,,<outros_termos> -> λ,<outros_termos> -> λ,,<outros_termos> -> λ,<outros_termos> -> λ,<outros_termos> -> λ,<outros_termos> -> λ,<outros_termos> -> λ,<outros_termos> -> λ,<outros_termos> -> λ,<outros_termos> -> <op_ad> <termo> <outros_termos> ,,,<outros_termos> -> <op_ad> <termo> <outros_termos> ,,,<outros_termos> -> λ
,,,,,,,,,,,,,,,,,,,,,,,,,,<op_ad> -> -,,,<op_ad> -> +,,,
,,,<mais_fatores> -> λ,,<mais_fatores> -> λ,,,,,,,,,<mais_fatores> -> λ,,<mais_fatores> -> λ,<mais_fatores> -> λ,,<mais_fatores> -> λ,<mais_fatores> -> λ,<mais_fatores> -> λ,<mais_fatores> -> λ,<mais_fatores> -> λ,<mais_fatores> -> λ,<mais_fatores> -> λ,<mais_fatores> -> λ,,,<mais_fatores> -> λ,<mais_fatores> -> <op_mul> <fator> <mais_fatores>,<mais_fatores> -> <op_mul> <fator> <mais_fatores>,<mais_fatores> -> λ
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,<op_mul> -> *,<op_mul> -> /,
,,,,,,,,,,,,,,,,,<pfalsa> -> λ,,,,,,,,,,,,,,,<pfalsa> -> else <comandos>
]