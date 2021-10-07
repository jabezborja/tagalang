#!/usr/bin/env python3

import sys
import time

from interpreter.lexer import Lexer
from interpreter.parser import Parser
from interpreter.interpreter import Interpreter


def main():
    arg = sys.argv[1]
    
    with open(arg) as fs:
        processtime_in_ms = time.time() * 1000
        result = Interpreter(Parser(Lexer(fs.read()).generate_tokens()).parse()).interpret()
        print(result)
        print(f"\nPROCESS TIME: {time.time() * 1000 - processtime_in_ms}ms")
        
if __name__ == '__main__':
    main()