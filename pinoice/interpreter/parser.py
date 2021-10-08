from interpreter.consts import TokenTypes
from interpreter.nodes import (
    NumeroNode,
    BinOpNode,
    BaryabolAccessNode,
    BaryabolAssignNode,
    LetraNode,
    IpahayagNode
)
from interpreter.consts import KEYWORDS
from interpreter.exceptions import SyntaxErrorException

class Parser: 
    def __init__(self, tokens):
        self.tokens = [str(token).split(":") for token in tokens]
        self.pos = -1
        self.curr_token = None
        self.parses = []
        self.next()

    def next(self):
        self.pos += 1
        self.curr_token = self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def parse(self):

        # Loop through the tokens until the end of file.
        while self.curr_token[0] != TokenTypes.EOF:
            if self.curr_token[0] == TokenTypes.KEYWORD and self.curr_token[1] == KEYWORDS[0]:
                self.baryabol()
            elif self.curr_token[0] == TokenTypes.KEYWORD and self.curr_token[1] == KEYWORDS[1]:
                self.ipahayag()
            else:
                self.next()

        return self.parses

    def baryabol(self):
        self.next()

        if self.curr_token[0] != TokenTypes.IDENTIFIER:
            return SyntaxErrorException("May ineexpect na identifier, pero walang mahanap.")

        baryabol_name = self.curr_token[1]
        self.next() 

        if self.curr_token[0] != TokenTypes.EQUALS:
            return SyntaxErrorException("May ineexpect na 'ay', pero walang mahanap.")

        self.next()

        express = self.expr()

        self.parses.append(BaryabolAssignNode(baryabol_name, express))

    def ipahayag(self):
        self.next()

        if self.curr_token[0] != TokenTypes.PROCEED_IDENTIFIER:
            return SyntaxErrorException("May ineexpect na 'ang' pero walang mahanap.")
        
        self.next()

        ipapahayag = self.expr()

        self.parses.append(IpahayagNode(ipapahayag))

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

        while self.curr_token[0] in (TokenTypes.MULTIPLY, TokenTypes.DIVIDE):
            token = self.curr_token

            if token[0] == TokenTypes.MULTIPLY:
                self.next()
            elif token[0] == TokenTypes.DIVIDE:
                self.next()

            node = BinOpNode(node, token, self.factor())

        return node

    def factor(self):
        token = self.curr_token
        
        if token[0] == TokenTypes.NUMERO:
            self.next()
            return NumeroNode(token)
        elif token[0] == TokenTypes.LETRA:
            return LetraNode(token)
        elif token[0] == TokenTypes.IDENTIFIER:
            return BaryabolAccessNode(token)
        elif token[0] == TokenTypes.LEFT_PARENTHESIS:
            self.next()
            node = self.expr()
            self.next()
            return node

        return self.pow()

    def pow(self):
        return BinOpNode(self.atom(), TokenTypes.POW, self.factor())

    def atom(self):
        token = self.curr_token

        if token[0] == TokenTypes.IDENTIFIER:
            return BaryabolAccessNode(token)

        