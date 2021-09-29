from interpreter.commands.buildinfunction import BuiltInFunction
from interpreter.conductor import Conductor
from interpreter.exceptions import ThrowException

class Ipahayag(BuiltInFunction):
    def __init__(self, conductor, line):
        super().__init__(conductor, line)
        self.needs_param = True
        print(self.result)

class Itigil(BuiltInFunction):
    def __init__(self, conductor, line):
        super().__init__(conductor, line)
        self.needs_param = False
        exit()