from interpreter.commands.functions import Itigil, Ipahayag
from interpreter.conductor import Conductor
from interpreter.commands.baryabol import Baryabol
from interpreter.consts import COMMANDS

class Lexer:
    def __init__(self, fs):
        self.command = COMMANDS
        self.conductor = Conductor()

        self.register()
        self.startExecution(fs)

    def register(self):
        self.conductor.register("baryabols", [])

    def startExecution(self, fs):
        for line in fs:
            for command in self.command:
                if command in line:
                    if "baryabol" in line:
                        curr_baryabols = self.conductor.use("baryabols")
                        curr_baryabols.append(Baryabol(line))
                        self.conductor.update("baryabols", curr_baryabols)
                    elif "ipahayag" in line:
                        Ipahayag(self.conductor, line)
                    elif "itigil" in line:
                        Itigil(self.conductor, line)