from interpreter.exceptions import NameErrorException

class Conductor:
    def __init__(self):
        self.pocket = {}
        self.tukuyin_pocket = {}

    def subscribe(self, name, val):
        self.pocket[name] = val

    def subscribe_tukuyin(self, func_name, params, body):
        self.tukuyin_pocket[func_name] = [params, body]

    def use(self, name):
        try: return self.pocket[name]
        except: NameErrorException(f"Yung '{name}' ay hindi pa natutukoy.")

    def use_tukuyin(self, func_name):
        try: return self.tukuyin_pocket[func_name]
        except: NameErrorException(f"Yung '{func_name} ay hindi pa natutukoy.'")