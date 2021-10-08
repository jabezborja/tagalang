""" Abstract Syntax Tree Nodes """

class AST: ...

class LetraNode(AST):
    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return f'{self.token}'

class NumeroNode(AST):
    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return f'{self.token}'
    
class BinOpNode(AST):
    def __init__(self, left, token, right):
        self.left = left
        self.token = token
        self.right = right

    def __repr__(self):
        return f'{self.left} : {self.token} : {self.right}'

class UnaryOpNode(AST):
	def __init__(self, op_tok, node):
		self.op_tok = op_tok
		self.node = node

	def __repr__(self):
		return f'{self.op_tok}, {self.node}'

class BaryabolAccessNode(AST):
    def __init__(self, baryabol_name):
        self.baryabol_name = baryabol_name

    def __repr__(self):
        return f'{self.baryabol_name}'

class BaryabolAssignNode(AST):
    def __init__(self, baryabol_name, expression):
        self.baryabol_name = baryabol_name
        self.expression = expression

    def __repr__(self):
        return f'{self.baryabol_name} : {self.expression}'

class IpahayagNode(AST):
    def __init__(self, ipapahayag):
        self.ipapahayag = ipapahayag

    def __repr__(self):
        return f'{self.ipapahayag}'

class KungNode(AST):
    def __init__(self, expressions, condition, body):
        self.expressions = expressions
        self.condition = condition
        self.body = body

    def __repr__(self):
        return f'{self.condition}'


