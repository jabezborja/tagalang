from interpreter.consts import TokenTypes
from interpreter.conductor import Conductor
from interpreter.consts import KEYWORDS
from interpreter.exceptions import SyntaxErrorException

class Parser: 
    def __init__(self, tokens):
        self.tokens = tokens

        """Used to track current position in the tokens"""
        self.pos = -1

        """Current token in the tokens using self.pos as pointer.
        Token: [TokenType, value]"""
        self.curr_token = None

        """Conductor instance in the class"""
        self.conductor = Conductor()

        self.init()
        
    """Proceed to the next token"""
    def next(self):
        self.pos += 1
        self.curr_token = self.tokens[self.pos] if self.pos < len(self.tokens) else None

    """Peek the future tokens
    Params Jump: How far does the future() will jump"""
    def future(self, jump=1):
        pos = self.pos
        pos += jump
        
        return self.tokens[pos] if len(self.tokens) > pos else None

     # Peek the past tokens.
    def past(self, jump=1):
        pos = self.pos
        pos -= jump
        
        return self.tokens[pos]

    def init(self):
        """Tokens that are passed by the Lexer
        are splitted into two parts.
        from ["TokenType:value"]
        to [[TokenType, value]]"""
        self.tokens = [str(token).split(":") for token in self.tokens]

        self.next()

        self.startExecution()

    def startExecution(self):
        
        while self.curr_token[0] != TokenTypes.EOF:
            # If the keyword is a 'baryabol'
            if self.curr_token[0] in TokenTypes.KEYWORD and self.curr_token[1] in KEYWORDS[0]:
                # baryabol name and value.
                name, val = self.make_baryabols()
                # Submit the baryabol into conductor for future use.
                self.conductor.subscribe(name, val)

            # Builtins
            elif self.curr_token[0] in TokenTypes.KEYWORD and self.curr_token[1] in KEYWORDS[1]:
                val = self.do_ipahayag()
                print(val)
            elif self.curr_token[0] in TokenTypes.KEYWORD and self.curr_token[1] in KEYWORDS[5]:
                val = self.do_itala()
            else:
                self.next()

    # Returns the baryabol name with the value.
    def make_baryabols(self):
        baryabol_name = ""
        baryabol_value = None
        baryabol_type = None

        # Get the Baryabol type   
        if self.future()[0] == TokenTypes.TYPE:
            self.next()

            baryabol_type = self.curr_token[1]

        else: baryabol_type = TokenTypes.KAHITANO

        # Get the Baryabol name
        if self.future()[0] == TokenTypes.IDENTIFIER:
            self.next()
            
            baryabol_name = self.curr_token[1]
            
        else: SyntaxErrorException("May ineexpect na pangalan ng baryabol pero walang nahanap")
            
        self.next()

        baryabol_value = self.get_value(TokenTypes.EQUALS, baryabol_type)

        return baryabol_name, baryabol_value

    def do_ipahayag(self):
        # ["keyword:ipahayag", "identifier:nice"]

        self.next()
        
        ipapahayag = self.get_value(KEYWORDS[4])

        return ipapahayag

    def do_itala(self):
        # ["keyword:ipahayag", "identifier:nice"]

        self.next()
        
        itatala = self.get_value(KEYWORDS[4])

        tala = input(itatala)

        try: tala = int(tala)
        except: ...

        return tala

    # Returns value
    def get_value(self, entry_identifier, val_type=TokenTypes.KAHITANO):
        value = None

        if self.curr_token[0] == entry_identifier or self.curr_token[1] == entry_identifier:
            self.next()
            
            # Values
            prototype = []

            # Integer values
            int_prototype = 0

            # Loop to the tokens after 'proc_identifier' until the next line or end of file (EOF)
            while self.curr_token[0] != TokenTypes.EOF and self.curr_token[0] != TokenTypes.NEWLINE:

                # If the token is itala
                if self.curr_token[0] == TokenTypes.KEYWORD:
                    if self.curr_token[1] == KEYWORDS[5]:
                        prototype.append(self.do_itala())

                # If the token is an identifier
                elif self.curr_token[0] == TokenTypes.IDENTIFIER:

                    # Find the token in the conductor
                    # Returns a value of the baryabol
                    name, _ = self.evaluate_identifier(self.curr_token)

                    # If the type of the value is an integer
                    # submit it on int_prototype
                    # instead submit it on prototype
                    if type(name) == int: int_prototype += int(name)
                    else: prototype.append(name)
                    
                    self.next()

                # If the token is LETRA or with quotes
                elif self.curr_token[0] == TokenTypes.LETRA:
                    prototype.append(self.curr_token[1])
                    self.next()

                # If the token is NUMERO or an integer
                elif self.curr_token[0] == TokenTypes.NUMERO:

                    # Submit it on int_prototype
                    int_prototype += int(self.curr_token[1])

                    self.next()

                # If the next token is not none and will be PLUS or '+'.
                elif self.future() != None and self.future()[0] == TokenTypes.PLUS:
                    self.next()

                    # Returns the sum of the inputs
                    prototype.append(self.do_plus())

                # If the current token is PLUS then skip
                elif self.curr_token[0] == TokenTypes.PLUS:
                    self.next()

                # Else, send an Syntax Error Exception
                else:
                    SyntaxErrorException(f"Hindi valid ang iyong syntax, ang '{self.curr_token[1]}' ay hindi identifier.")
                    self.next()

            try:
                prototype = [int(prot) for prot in prototype]
            except: ...

            # If there is an integer and a LETRA or IDENTIFIER each at the same time, throw an error.
            if int_prototype != 0 and len(prototype) != 0 and val_type == TokenTypes.KAHITANO:
                SyntaxErrorException(f"Hindi suportado ang mga input para sa +: 'numero' at 'letra'")

            # If the value is an integer
            elif int_prototype > 0 and val_type == TokenTypes.NUMERO or int_prototype > 0 and val_type == TokenTypes.KAHITANO:
                value = int_prototype

            # If the value is a string
            elif int_prototype == 0 and val_type == TokenTypes.LETRA or int_prototype == 0 and val_type == TokenTypes.KAHITANO:
                prototype = [str(prot) for prot in prototype]
                value = ''.join(prototype)

            # If the value is invalid
            else:
                SyntaxErrorException(f"Hindi valid ang iyong syntax para sa: '{val_type}'")

        else: SyntaxErrorException(f"May ineexpect na '{entry_identifier}' pero walang mahanap.")

        return value

    # Returns the answer of the operation '+'
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
        else:
            SyntaxErrorException(f"Hindi valid: {self.curr_token}")

        return answer
    
    def evaluate_identifier(self, token):
        baryabol_value = ""
        type = None

        try:
            baryabol_value = int(token[1])
            token[0] = TokenTypes.NUMERO
        except: ...

        if token[0] == TokenTypes.IDENTIFIER:
            baryabol_value = self.conductor.use(token[1])

            try:
                type = TokenTypes.NUMERO
                baryabol_value = int(baryabol_value)
            except: ...

            type = TokenTypes.IDENTIFIER
        elif token[0] == TokenTypes.NUMERO:
            baryabol_value = int(token[1])
            type = TokenTypes.NUMERO
        else:
            baryabol_value = token[1]
            type = TokenTypes.LETRA

        return baryabol_value, type 