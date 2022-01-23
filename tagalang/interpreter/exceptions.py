ERROR_TEMPLATE = """
May natagpuang error:
    %s
%s: %s
"""

class ExceptionType:
    SyntaxError = ["interpreter.error.syntaxerror", "Syntax Error"]
    NameError = ["interpreter.error.nameerror", "Name Error"]
    ...

class Exception:
    def __init__(self, type, text, messege):
        self.type = type
        self.messege = messege
        self.text = text
        self.exec()
        ...
        
    def exec(self):
        if self.type == ExceptionType.SyntaxError[1]:
            msg = ERROR_TEMPLATE % (self.text, self.type, self.messege)
        elif self.type == ExceptionType.NameError[1]:
            msg = ERROR_TEMPLATE % (self.text, self.type, self.messege)
        ...

        print(msg)
        exit()

class SyntaxErrorException(Exception):
    def __init__(self, text):
        super().__init__(ExceptionType.SyntaxError[1], text, "hindi valid na syntax")
        ...

class NameErrorException(Exception):
    def __init__(self, text):
        super().__init__(ExceptionType.NameError[1], text, "hindi natukoy")
        ...