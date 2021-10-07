from interpreter.consts import TokenTypes
from interpreter.nodes import NumberNode, BinOpNode

class Parser: 
    def __init__(self, tokens):
        self.tokens = [str(token).split(":") for token in tokens]
        self.pos = -1
        self.curr_token = None
        self.next()

    def next(self):
        self.pos += 1
        self.curr_token = self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def parse(self):
        return self.expr()

    def expr(self):
        node = self.term()

        while self.curr_token[0] in (TokenTypes.PLUS, TokenTypes.MINUS):
            token = self.curr_token

            if token[0] == TokenTypes.PLUS:
                self.next()
            elif token[0] == TokenTypes.MINUS:
                self.next()

            right = self.term()

            node = BinOpNode(node, token, right)

        return node

    def term(self):
        node = self.factor()

        while self.curr_token[0] in (TokenTypes.TIMES, TokenTypes.DIVIDE):
            token = self.curr_token

            if token[0] == TokenTypes.TIMES:
                self.next()
            elif token[0] == TokenTypes.DIVIDE:
                self.next()

            node = BinOpNode(node, token, self.factor())

        return node

    def factor(self):
        token = self.curr_token
        
        if token[0] == TokenTypes.NUMERO:
            self.next()
            return NumberNode(token)
        elif token[0] == TokenTypes.LEFT_PARENTHESIS:
            self.next()
            node = self.expr()
            self.next()
            return node