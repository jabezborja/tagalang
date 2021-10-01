from compiler.parser import Parser
from compiler.lexer import Lexer
import time
import sys

def main():
    arg = sys.argv[1]
    
    with open(arg) as fs:
        processtime_in_ms = time.time() * 1000
        result = Parser(Lexer(fs.read()).generate_tokens())
        print(f"\nPROCESS TIME: {time.time() * 1000 - processtime_in_ms}ms")
        
if __name__ == '__main__':
    main()