class Conductor:
    def __init__(self):
        self.pocket = {}

    def use(self, name):
        return self.pocket[name]
    
    def register(self, name, type):
        self.pocket[name] = type

    def update(self, name, value):
        self.pocket[name] = value