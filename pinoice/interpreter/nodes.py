# Abstract Syntax Tree Nodes

class NumberNode:
    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return f'({self.token})'
    
class BinOpNode:
    def __init__(self, left, token, right):
        self.left = left
        self.token = token
        self.right = right

    def __repr__(self):
        return f'({self.left} : {self.token} : {self.right})'

class UnaryOpNode:
	def __init__(self, op_tok, node):
		self.op_tok = op_tok
		self.node = node

	def __repr__(self):
		return f'({self.op_tok}, {self.node})'

class BaryabolNode:
    def __init__(self, baryabol_name):
        self.baryabol_name = baryabol_name

    def __repr__(self):
        return f'({self.baryabol_name})'


class LetraNode:
    def __init__(self, tok):
        self.tok = tok

    def __repr__(self):
        return f'({self.tok})'
