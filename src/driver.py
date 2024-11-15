"""Handles the execution of all the separate parts of compilation"""

import subprocess
import argparse
import re
from pathlib import Path


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
    r"(?P<IDENTIFIER>[a-zA-Z_]\w*\b)|(?P<CONSTANT>[0-9]+\b)|(?P<SYMBOL>[\(\){};])"
)
KEYWORDS = ["int", "void", "return"]


def preprocess(filename) -> str:
    """Prepare a file to be compiled by performing a preprocessing pass over the source file"""
    source_file = Path(filename)
    # TODO: this can be removed and the output of gcc can be piped directly into a string instead of wastefully creating a new file
    processed_file = source_file.with_suffix(".i")

    with processed_file.open(mode="w+", encoding="utf-8") as f:
        try:
            subprocess.run(
                ["gcc", "-E", "-P", source_file], check=True, text=True, stdout=f
            )
        except subprocess.CalledProcessError as e:
            processed_file.unlink()
            # TODO: standardise error return logic
            raise e
        f.seek(0)
        source_content = f.read().rstrip()
    processed_file.unlink()

    return source_content


# TODO: rename
def compile_c():
    NotImplemented


def lexer(source: str):
    """Tokenise contents of a preprocessed file"""

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
            # TODO: standardise error return logic
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


def main():
    if args.lex:
        lexer(preprocess(args.filename))
        return 0
    if args.parse:
        return 0
    if args.codegen:
        return 0
    else:
        preprocess(args.filename)
        return 0
