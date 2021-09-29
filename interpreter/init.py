from interpreter.lexer import Lexer

def interpret(source, name):
    with open(f"{name}") as fs:
        Lexer(fs)