# LAlg-v4 Compiler
Compilador desenvolvido durante a disciplina de Compiladores II no curso de Ciência da Computação na UFMT.

---

Compiler developed during Compilers II class of the Computer Science Course on UFMT.

## Usage

This repository includes two main scripts: 

* `main.py`: Calls code to compile input to object code.
* `run.py`: Interprets object code.

### Compiling

To compile code in LAlg-v4 language run:

    compiler/main.py file.txt

The default behaviour is to output code to a file named out.txt. Options can be passed when calling script via terminal, mostly to print additional information useful for debugging:

| Options | Description |
|---------|-------------|
| ` -t, --tokens` | Toggles token printing for debugging     
|`--count` | Prints identified tokens amount (ignores whitespace and newline tokens)       
|`-p, --parse_steps` | Prints all of the parsing steps       
| ` -s, --symbols` |  Prints the symbol table           
|`--rpn` | Debug Reverse Poland Notation (RPN) implementation, use only for testing. Will stop after lexical analysis. The input file must only include numerical values and operators.
|`-c, --code` | Prints generated object code to standard output.
|` -o FILE, --output FILE` | Saves generated object code to an output file of your choice

### Executing Object Code

In order to run programs written in LAlg-v4 language, the `run.py` script can be used. It's only argument is the name of the file you will want to run. Example:

    compiler/run.py file.txt
