# LAlg-v4 Compiler
Compilador desenvolvido durante a disciplina de Compiladores II no curso de Ciência da Computação na UFMT.

---

Compiler developed during Compilers II class of the Computer Science Course on UFMT.

GitHub Page: https://github.com/HenriqueOPeixoto/compiler

## Usage

This repository includes two main scripts: 

* `main.py`: Calls code to compile input to object code.
* `run.py`: Interprets object code.

### Compiling

To compile code in LAlg-v4 language run:

    python compiler/main.py file.txt

The default behavior is to output code to a file named `out.txt`. Options can be passed when calling script via terminal, mostly to print additional information useful for debugging. Run script with `--help` option to see a list of them.

| Options | Description |
|---------|-------------|
| ` -t, --tokens` | Toggles token printing for debugging     
|`--count` | Prints identified tokens amount (ignores whitespace and newline tokens)       
|`-p, --parse_steps` | Prints all of the parsing steps       
| ` -s, --symbols` |  Prints the symbol table           
|`--rpn` | Debug Reverse Poland Notation (RPN) implementation, use only for testing. Will stop after lexical analysis and does not consider inversion sign (-). The input file must only include numerical values and operators.
|`-c, --code` | Prints generated object code to standard output.
|` -o FILE, --output FILE` | Saves generated object code to an output file of your choice

### Executing Object Code

In order to run programs written in LAlg-v4 language, the `run.py` script can be used. It's only argument is the name of the file you will want to run. Example:

    python compiler/run.py file.txt

## More info:

The `docs/` folder contains information regarding the language, such as grammar, first-follow sets, parse table and a working example of LAlg-v4 code. A `tests/` folder is also included in the repository. Some tests were made purposefully incorrect to test scenarios where code was written wrong. Others require special options to be passed to the terminal.

