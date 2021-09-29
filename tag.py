from interpreter.init import interpret
import sys

def main():
    source = sys.argv[0]
    name = sys.argv[1]
    interpret(source, name)

if '__main__' == __name__:
    main()