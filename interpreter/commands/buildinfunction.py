from interpreter.conductor import Conductor
from interpreter.exceptions import ThrowException

class BuiltInFunction:
    def __init__(self, conductor, line):
        self.param = ""
        self.needs_param = False
        self.has_param = self.check_param()

        self.conductor = conductor

        self.result = self.execute(line)

    def __repr__(self):
        return self.result

    def execute(self, line):
        self.param = self.evaluate(self.tokenize(self.get_content(line))) if not self.needs_param else None

        return self.param

    def get_content(self, line):
        content_prototype = ""
        start_get_content = False

        for char in line:

            # Check if end
            if ')' in char:
                start_get_content = False

            ## Executioneers
            if start_get_content:
                content_prototype += char

            ## Checkers
            if '(' in char:
                start_get_content = True

        return content_prototype

    def tokenize(self, content):
        tokens = []

        content = content.split("+")

        # Strip every token
        content = [cont.strip() for cont in content]

        for cont in content:
            if '"' in cont:
                tokens.append(f"LETRA:{cont}".replace('"', ''))
            else:
                tokens.append(f"IDENTIFIER:{cont}")

        return tokens
                

    def evaluate(self, tokens):
        evaluated_tokens = ""
        content_observer = False

        for token in tokens:
            token = token.split(":")
            if "LETRA" in token:
                evaluated_tokens += token[1]
            elif "IDENTIFIER" in token:
                for variable in self.conductor.use("baryabols"):
                    if variable.name == token[1]:
                        content_observer = True
                        
                        evaluated_tokens += str(variable.content)

                if not content_observer:
                    ThrowException(f"No variable '{token[1]}'")

        return evaluated_tokens

    def check_param(self):
        if self.param is None or self.param == "":
            if self.needs_param:
                ThrowException("Needs a paramater but found none.")
            return False
        return True