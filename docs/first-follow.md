# First e Follow da Linguagem LAlg-v4

## Linguagem original

    <programa> -> program ident <corpo> .

    <corpo> -> <dc> begin <comandos> end

    <dc> -> <dc_v> <mais_dc>  | λ

    <mais_dc> -> ; <dc> | λ

    <dc_v> ->  <tipo_var> : <variaveis>

    <tipo_var> -> real | integer

    <variaveis> -> ident <mais_var>

    <mais_var> -> , <variaveis> | λ

    <comandos> -> <comando> <mais_comandos>

    <mais_comandos> -> ; <comandos> | λ

    <comando> -> 	read (ident) |
                    write (ident) |
                    ident := <expressao>
                    if <condicao> then <comandos> <pfalsa> $ |
                    while <condicao> do <comandos> $

    <condicao> -> <expressao> <relacao> <expressao>

    <relacao> -> = | <> | >= | <= | > | <

    <expressao> -> <termo> <outros_termos>
    
    <termo> -> <op_un> <fator> <mais_fatores>
    
    <op_un> -> - | λ
    
    <fator> -> ident | numero_int | numero_real | (<expressao>)
    
    <outros_termos> -> <op_ad> <termo> <outros_termos> | λ

    <op_ad> -> + | -
    
    <mais_fatores> -> <op_mul> <fator> <mais_fatores> | λ

    <op_mul> -> * | /

    <pfalsa> -> else <comandos> | λ



## First

    First(<programa>) = {program}
    
    First(<corpo>) = {} U First(<dc>) = {real, integer, begin} # Pode ser begin, pois <dc> pode ser λ
    First(<dc>) = {λ} U First(<dc_v>) = {λ, real, integer}
    First(<mais_dc>) = {;, λ}
    First(<dc_v>) = {} U First(<tipo_var>) = {real, integer}
    First(<tipo_var>) = {real, integer}


    First(<variaveis>) = {ident}
    First(<mais_var>) =  {,} U {λ}
    
    First(<comandos>) = {} U First(<comando>) = {read, write, ident, if, while}
    First(<mais_comandos>) = {;, λ}
    First(<comando>) = {read, write, ident, if, while}

    First(<relacao>) = {=, <>, >=, <=, >, <}

    First(<condicao>) = {} U First(<expressao>) = {-, ident, numero_int, numero_real, ( }
    First(<expressao>) = {} U First(<termo>) = {-, ident, numero_int, numero_real, ( }
    First(<termo>) = {} U First(<op_un>) = {-, First(<fator>)} = {-, ident, numero_int, numero_real, ( } 
    
    First(<op_un>) = {-, λ}

    First(<fator>) = {ident, numero_int, numero_real, ( }
    
    First(<outros_termos>) = {λ} U First(<op_ad>) = {λ, +, -}
    First(<op_ad>) = {+, -}
    
    First(<mais_fatores>) = {λ} U First(<op_mul>) = {λ, *, /}
    First(<op_mul>) = {*, /}

    First(<pfalsa>) = {else, λ}


## Follow

Usei o símbolo @ para identificar o fim de cadeia.

    Follow(<programa>) = {@}
    
    Follow(<corpo>) = {.}
    Follow(<dc>) = {begin}
    Follow(<mais_dc>) = {begin}
    Follow(<dc_v>) = {} U First(<mais_dc>) = {;, begin}, onde o lambda vira begin pois o follow não pode ter vazio, daí pega o follow de <mais_dc> também
    Follow(<tipo_var>) = {:}


    Follow(<variaveis>) = {} U Follow(<dc_v>) = {;, begin}
    
    Follow(<mais_var>) =  {} U Follow(<variaveis>) = {;, begin}
    
    Follow(<comandos>) = {end, $} U First(<pfalsa>) = {end, $, else}
    Follow(<mais_comandos>) = {} U Follow(<comandos>) = {end, $, else}
    Follow(<comando>) = {} U First(<mais_comandos>) = {;, end, $, else}

    Follow(<relacao>) = {} U First(<expressao>) = {-, ident, numero_int, numero_real, ( }
    
    Follow(<condicao>) = {then, do}
    Follow(<expressao>) = { ) } U First(<relacao>) U Follow(<condicao>) = { ), =, <>, >=, <=, >, <, then, do}
    Follow(<termo>) = {} U First(<outros_termos>) = {+, -, Follow(<expressao>)} = {+, -, ), =, <>, >=, <=, >, <, then, do}
    Follow(<op_un>) = {} U First(<fator>) = {ident, numero_int, numero_real, ( }

    Follow(<fator>) = {} U First(<mais_fatores>) = {*, /, Follow(<termo>)} = {*, /, +, -, ), =, <>, >=, <=, >, <, then, do}
    
    Follow(<outros_termos>) = {} U Follow(<expressao>) = { ), =, <>, >=, <=, >, <, then, do}
    Follow(<op_ad>) = {} U First(<termo>) = {-, ident, numero_int, numero_real, ( }
    
    Follow(<mais_fatores>) = {} U Follow(<termo>) = {+, -, ), =, <>, >=, <=, >, <, then, do}
    
    Follow(<op_mul>) = {} U First(<fator>) = {ident, numero_int, numero_real, ( }

    Follow(<pfalsa>) = {$}
