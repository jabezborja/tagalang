
from compiler.conductor import Conductor
from compiler.exceptions import NameErrorException, SyntaxErrorException
from compiler.lexer import Token
from compiler.consts import KEYWORDS, TokenTypes

class Parser: 
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = -1
        self.curr_token = None

        self.conductor = Conductor()

        self.init()
        
    def next(self):
        self.pos += 1
        self.curr_token = self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def future(self, jump=1):
        pos = self.pos
        pos += jump
        
        return self.tokens[pos] if len(self.tokens) > pos else None

    def past(self, jump=1):
        pos = self.pos
        pos -= jump
        
        return self.tokens[pos]

    def init(self):
        self.tokens = [str(token).split(":") for token in self.tokens]

        self.next()

        self.startExecution()

    def startExecution(self):
        
        # Baryabols
        while self.curr_token[0] != TokenTypes.EOF:
            if self.curr_token[0] in TokenTypes.KEYWORD and self.curr_token[1] in KEYWORDS[0]:
                name, val = self.make_baryabols()
                self.conductor.subscribe(name, val)
            elif self.curr_token[0] in TokenTypes.KEYWORD and self.curr_token[1] in KEYWORDS[1]:
                self.do_ipahayag()
            else:
                self.next()

    def make_baryabols(self):
        baryabol_name = ""
        baryabol_value = None
        baryabol_type = None

        # Evaluate the Baryabol type
        if self.future()[0] == TokenTypes.TYPE:
            self.next()

            baryabol_type = self.curr_token[1]

        # Evaluate the Baryabol name
        if self.future()[0] == TokenTypes.IDENTIFIER:
            self.next()
            
            baryabol_name = self.curr_token[1]
            
        else: SyntaxErrorException(self.curr_token[1], self.pos)
            
        self.next()

        # Evaluate the Value
        if self.curr_token[0] == TokenTypes.EQUALS:
            self.next()
            
            prototype = []
            int_prototype = 0

            while self.curr_token[0] != TokenTypes.EOF and self.curr_token[0] != TokenTypes.NEWLINE:
                if self.curr_token[0] == TokenTypes.IDENTIFIER:
                    prototype.append(self.conductor.use(self.curr_token[1]))
                    self.next()
                elif self.curr_token[0] == TokenTypes.LETRA:
                    prototype.append(self.curr_token[1])
                    self.next()
                elif self.curr_token[0] == TokenTypes.NUMERO:
                    int_prototype += int(self.curr_token[1])
                    prototype.append(str(int_prototype))
                    self.next()
                elif self.future() != None and self.future()[0] == TokenTypes.PLUS:
                    self.next()
                    prototype.append(self.do_plus())
                elif self.curr_token[0] == TokenTypes.PLUS:
                    self.next()
                else:
                    SyntaxErrorException(self.curr_token[0], self.pos)
                    self.next()

            if int_prototype != 0 and len(prototype) != 0 and baryabol_type == TokenTypes.KAHITANO:
                baryabol_value = ''.join(prototype)
            elif int_prototype == 0 and baryabol_type == TokenTypes.LETRA or baryabol_type == TokenTypes.KAHITANO:
                prototype = [str(prot) for prot in prototype]
                baryabol_value = ''.join(prototype)
            elif int_prototype > 0 and baryabol_type == TokenTypes.NUMERO or baryabol_type == TokenTypes.KAHITANO:
                baryabol_value = int_prototype
            else:
                SyntaxErrorException(f"invalid literal for KahitAno with: '{baryabol_type}'", self.pos)

        else: ...

        return baryabol_name, baryabol_value

    def do_plus(self):
        answer = None
        identifier_recent_prototype = self.past()
        identifier_type = None
        
        val, eval_type = self.evaluate_identifier(identifier_recent_prototype)

        identifier_type = eval_type

        if identifier_type == TokenTypes.NUMERO:
            self.next()
            num_val, num_type = self.evaluate_identifier(self.curr_token)

            if num_type == TokenTypes.NUMERO:
                answer = int(val) + int(num_val)
        elif identifier_type == TokenTypes.LETRA:
            self.next()
            let_val, let_type = self.evaluate_identifier(self.curr_token)

            if let_type == TokenTypes.LETRA:
                answer = val + let_val
        elif identifier_type == TokenTypes.IDENTIFIER:
            self.next()
            iden_val, iden_type = self.evaluate_identifier(self.curr_token)

            if iden_type == TokenTypes.IDENTIFIER:
                if type(val) == int : val = int(val)
                if type(iden_val) == int : iden_val = int(val)

                answer = val + iden_val

        return answer
    
    def evaluate_identifier(self, token):
        baryabol_value = ""
        type = None

        if token[0] == TokenTypes.IDENTIFIER:
            baryabol_value = self.conductor.use(token[1])
            type = TokenTypes.IDENTIFIER
        elif token[0] == TokenTypes.NUMERO:
            baryabol_value = token[1]
            type = TokenTypes.NUMERO
        else:
            baryabol_value = token[1]
            type = TokenTypes.LETRA

        return baryabol_value, type 

    def do_ipahayag(self):
        # ["keyword:ipahayag", "identifier:nice"]
        print(self.curr_token[1])

        self.next()