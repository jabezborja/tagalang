#!/usr/bin/env python3

import sys
import time

from interpreter.lexer import Lexer
from interpreter.parser import Parser
from interpreter.interpreter import Interpreter
from interpreter.conductor import Conductor


def main():
    arg = sys.argv[1]
    
    with open(arg) as fs:
        processtime_in_ms = time.time() * 1000
        lexer = Lexer(fs.read()).generate_tokens()
        parser = Parser(lexer).parse()
        conductor = Conductor()
        Interpreter(parser, conductor).interpret()
        print(f"\nPROCESS TIME: {time.time() * 1000 - processtime_in_ms}ms")
        
if __name__ == '__main__':
    main()