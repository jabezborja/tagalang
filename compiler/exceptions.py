ERROR_TEMPLATE = """
May natagpuang error banda sa line %s
    %s
    ^
%s: %s
"""

class ExceptionType:
    SyntaxError = ["interpreter.error.syntaxerror", "Syntax Error"]

class Exception:
    def __init__(self, type, text, messege, line):
        self.type = type
        self.messege = messege
        self.text = text
        self.line = line + 1
        self.exec()
        
    def exec(self):
        if self.type == ExceptionType.SyntaxError[1]:
            msg = ERROR_TEMPLATE % (self.line, self.text, self.type, self.messege)

        print(msg)
        exit()

class SyntaxErrorException(Exception):
    def __init__(self, text, line):
        super().__init__(ExceptionType.SyntaxError[1], text, "invalid syntax", line)
        ...