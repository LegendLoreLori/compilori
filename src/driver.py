"""Handles the execution of all the separate parts of compilation"""

import subprocess
import argparse

parser = argparse.ArgumentParser(
    description="Handles the execution of all the separate parts of compilation",
    epilog="help"
)

parser.add_argument("filename", help="The input file to preprocess")
parser.add_argument("--lex", action="store_const", const=1, help="Run lexer, but stop before parsing")
parser.add_argument("--parse", action="store_const", const=1, help="Run lexer and parser, but stop before assembling")
parser.add_argument("--codegen", action="store_const", const=1,help="Run lexing, parsing, and assembly generation, but stop before code emission")

args = parser.parse_args()

def preprocess(filename):
    """Prepare a file to be compiled by performing a preprocessing pass over the source file,
    writing the output to a temporary file"""
    preprocessed_filename = filename.replace(".c", ".i")
    with open(preprocessed_filename, 'w+', encoding='utf-8') as f:
        subprocess.run(["gcc", "-E", "-P", filename], check=True, text=True, stdout=f)

def compile_c():
    NotImplemented

def link():
    NotImplemented



if __name__ == "__main__":
    if args.lex:
        # none of these options should produce any output files
        print("test lex")
    if args.parse:
        print("test parse")
    if args.codegen:
        print("test codegen")

    preprocess(args.filename)
