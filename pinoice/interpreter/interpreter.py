from interpreter.consts import TokenTypes
from interpreter.exceptions import SyntaxErrorException

class NodeVisitor(object):
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.invalid_visit)
        return visitor(node)

    def invalid_visit(self, node):
        raise Exception(f"No visit_{type(node).__name__} method")


class Interpreter(NodeVisitor):
    def __init__(self, parsers, conductor):
        self.pos = -1
        self.parsers = parsers
        self.curr_parser = None
        self.conductor = conductor

        self.next()

    def next(self):
        self.pos += 1
        self.curr_parser = self.parsers[self.pos] if self.pos < len(self.parsers) else None

    def visit_BinOpNode(self, node):
        if node.token[0] == TokenTypes.PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.token[0] == TokenTypes.MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.token[0] == TokenTypes.MULTIPLY:
            return self.visit(node.left) * self.visit(node.right)
        elif node.token[0] == TokenTypes.DIVIDE:
            return self.visit(node.left) / self.visit(node.right)

    def visit_LetraNode(self, node):
        return node.token[1]

    def visit_NumeroNode(self, node):
        return int(node.token[1])
    
    def visit_BaryabolAccessNode(self, node):
        baryabol_name = node.baryabol_name
        val = self.conductor.use(baryabol_name[1])

        return val

    def visit_BaryabolAssignNode(self, node):
        baryabol_name = node.baryabol_name
        val = self.visit(node.expression)

        self.conductor.subscribe(baryabol_name, val)
        return val

    def visit_IpahayagNode(self, node):
        ipapahayag = self.visit(node.ipapahayag)
        print(ipapahayag)
        
    def interpret(self):
        while self.curr_parser != None:
            self.visit(self.curr_parser)
            self.next()