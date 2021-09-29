from interpreter.exceptions import ThrowException

class Type:
    LETRA = ["baryabol.type.letra", "letra"]
    NUMERO = ["baryabol.type.numero", "numero"]
    OOATHINDI = ["baryabol.type.ooathindi", "ooathindi"]

class Baryabol:
    def __init__(self, line):

        # The name of the Variable
        self.var_name = ""

        # The type of the Variable.
        # Letra = String
        # Numero = Int
        # OoAtHindi = Boolean
        self.var_type = None

        self.var_content = ""

        self.startExecution(line)

    @property
    def name(self):
        return self.var_name

    @property
    def type(self):
        return self.var_type

    @property
    def content(self):
        return self.var_content

    def startExecution(self, line):
        self.var_name = self.get_name(line)
        self.var_type = self.eval_type(self.get_type(line))
        self.var_content = self.eval_content(self.get_content(line))

    def get_name(self, line):
        name_prototype = ""
        start_get_name = False

        for char in line:

            if '=' in char:
                start_get_name = False

            if start_get_name:
                name_prototype += char

            if '>' in char:
                start_get_name = True

        return name_prototype.strip()

    def get_type(self, line):

        type_prototype = ""
        start_get_type = False

        for char in line:

            # Check if end
            if '>' in char:
                start_get_type = False

            ## Executioneers
            if start_get_type:
                type_prototype += char

            ## Checkers
            if '<' in char:
                start_get_type = True

        return type_prototype

    def eval_type(self, type):
        type_enum = None

        if type in Type.LETRA[1]: type_enum = Type.LETRA[0]
        elif type in Type.NUMERO[1]: type_enum = Type.NUMERO[0]
        elif type in Type.OOATHINDI[1]: type_enum = Type.OOATHINDI[0]
        else: ThrowException(f"No type '{type}'")

        return type_enum

    def get_content(self, line):

        content_prototype = ""
        start_get_content = False

        for char in line:

            ## Executioneers
            if start_get_content:
                content_prototype += char

            ## Checkers
            if '=' in char:
                start_get_content = True

        start_get_content = False

        return content_prototype.strip()


    def eval_content(self, content):

        try:
            if '"' in content:
                content = str(content)
            else:
                content = int(content)
        except:
            ThrowException("Invalid type")

        content = content.replace('"', '') if type(content) == str else content

        passed = False

        if type(content) == str and self.type == Type.LETRA[0]: passed = True
        elif type(content) == int and self.type == Type.NUMERO[0]: passed = True
        elif type(content) == bool and self.type == Type.OOATHINDI[0]: passed = True
        else: passed = False

        if passed:
            return content
        else:
            ThrowException("Wrong type")