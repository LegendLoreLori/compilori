# Compilori

A toy c compiler written with python.
This compiler isn't intended to be used for any real projects and is an active development exercise.

Currently compilori doesn't support Windows and requires `GCC` be installed on your machine.

## CLI

Compilori features a CLI, it accepts a path to a source `.c` file and the optional arguments `lex`, `parse`, and `codegen`
To use the CLI, `cd` to the root directory of the project and run the following:
```
./main.py path/to/your/source.c [OPTIONAL ARGUMENTS] 
```
run with `--help` for full description of each optional argument
