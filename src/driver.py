"""Handles the execution of all the separate parts of compilation"""

import subprocess
import argparse
import re

parser = argparse.ArgumentParser(
    description="Handles the execution of all the separate parts of compilation",
    epilog="help",
)

parser.add_argument("filename", help="The input file to preprocess")
parser.add_argument(
    "--lex", action="store_const", const=1, help="Run lexer, but stop before parsing"
)
parser.add_argument(
    "--parse",
    action="store_const",
    const=1,
    help="Run lexer and parser, but stop before assembling",
)
parser.add_argument(
    "--codegen",
    action="store_const",
    const=1,
    help="Run lexing, parsing, and assembly generation, but stop before code emission",
)
args = parser.parse_args()

PATTERN = re.compile(
    r"(?P<IDENTIFIER>[a-zA-Z_]\w*\b)|(?P<CONSTANT>[0-9]+\b)|(?P<SYMBOL>[\(\){};])?"
)
KEYWORDS = ["int", "void", "return"]


def preprocess(filename) -> str:
    """Prepare a file to be compiled by performing a preprocessing pass over the source file,
    writing the output to a temporary file"""
    preprocessed_filename = filename.replace(".c", ".i")
    with open(preprocessed_filename, "w+", encoding="utf-8") as f:
        subprocess.run(["gcc", "-E", "-P", filename], check=True, text=True, stdout=f)
    return preprocessed_filename


def compile_c():
    NotImplemented


def lexer(filename):
    """Tokenise contents of a preprocessed file"""
    with open(filename, encoding="utf-8") as f:
        source: str = f.read().rstrip()

    tokens = []

    while source:
        token = ""
        if source[0].isspace():
            source = source.lstrip()
        match = PATTERN.match(source)
        if match:
            token = match.group()
            if token in KEYWORDS:
                token = ("KEYWORD", token)
            else:
                token = (match.lastgroup, token)
        if not token:
            raise KeyError(
                [
                    "Unsupported character provided, unable to tokenise source.",
                    repr(source),
                ]
            )
        tokens.append(token)
        source = source.removeprefix(token[-1])
    return tokens


def link():
    NotImplemented


if __name__ == "__main__":
    if args.lex:
        print(lexer(preprocess(args.filename)))
    if args.parse:
        print("test parse")
    if args.codegen:
        print("test codegen")
    else:
        preprocess(args.filename)
