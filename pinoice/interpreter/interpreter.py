from interpreter.consts import TokenTypes

class NodeVisitor(object):
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))


class Interpreter(NodeVisitor):
    def __init__(self, parser):
        self.parser = parser

    def visit_BinOpNode(self, node):
        if node.token[0] == TokenTypes.PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.token[0] == TokenTypes.MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.token[0] == TokenTypes.TIMES:
            return self.visit(node.left) * self.visit(node.right)
        elif node.token[0] == TokenTypes.DIVIDE:
            return self.visit(node.left) / self.visit(node.right)

    def visit_NumberNode(self, node):
        return int(node.token[1])

    def interpret(self):
        return self.visit(self.parser)