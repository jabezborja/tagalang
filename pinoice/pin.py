#!/usr/bin/env python3

import sys
import time

from compiler.lexer import Lexer
from compiler.parser import Parser


def main():
    arg = sys.argv[1]
    
    with open(arg) as fs:
        processtime_in_ms = time.time() * 1000
        result = Parser(Lexer(fs.read()).generate_tokens())
        print(f"\nPROCESS TIME: {time.time() * 1000 - processtime_in_ms}ms")
        
if __name__ == '__main__':
    main()