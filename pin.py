from compiler.parser import Parser
from compiler.lexer import Lexer
import sys

def main():
    arg = sys.argv[1]
    
    with open(arg) as fs:
        result = Parser(Lexer(fs.read()).generate_tokens())
        
if __name__ == '__main__':
    main()