from compiler.exceptions import NameErrorException


class Conductor:
    def __init__(self):
        self.pocket = {}

    def subscribe(self, name, val):
        self.pocket[name] = val

    def use(self, name):
        try: return self.pocket[name]
        except: NameErrorException(f"name '{name}' is not defined.", 0)