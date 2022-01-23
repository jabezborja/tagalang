#!/usr/bin/env python3

import sys
import time

from interpreter.lexer import Lexer
from interpreter.parser import Parser
from interpreter.interpreter import Interpreter
from interpreter.conductor import Conductor


def main():
    arg = sys.argv[1]
    
    processtime_in_ms = time.time() * 1000

    with open(arg) as fs:

        # Generate Tokens
        lexer = Lexer(fs.read())
        tokens = lexer.generate_tokens()

        # Generate AST
        parser = Parser(tokens)
        ast = parser.parse()

        # Global conductor instance
        conductor = Conductor()

        # Interpret AST
        interpreter = Interpreter(ast, conductor)
        interpreter.interpret()

        print(f"\nPROCESS TIME: {time.time() * 1000 - processtime_in_ms}ms")
        
if __name__ == '__main__':
    main()