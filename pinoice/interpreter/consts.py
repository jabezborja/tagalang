import string

TOKEN_TYPES = {
    "letra": "interpreter.token.letra",
    "numero": "interpreter.token.numero",
    "identifier": "interpreter.token.identifier",
    "keyword": "interpreter.token.keyword",
    "plus": "interpreter.token.plus",
    "minus": "interpreter.token.minus",
    "times": "interpreter.token.times",
    "divide":"interpreter.token.divide",
    "equals": "interpreter.token.equals",
    "left_parenthesis": "interpreter.token.left_parenthesis",
    "right_parenthesis": "interpreter.token.right_parenthesis",
    "left_bracket": "interpreter.token.left_bracket",
    "right_bracket": "interpreter.token.right_bracker",
    "double_equals": "interpreter.token.double_equals",
    "comma": "interpreter.token.comma",
    "newline": "interpreter.token.newline",
    "eof": "interpreter.token.eof",
}

class TokenTypes:

    # String
    LETRA = "interpreter.token.letra"
    # Integer
    NUMERO = "interpreter.token.numero"
    # Boolean
    ANO = "interpreter.token.ano"
    # Any
    KAHITANO = "interpreter.token.kahitano"

    IDENTIFIER = "interpreter.token.identifier"
    KEYWORD = "interpreter.token.keyword"
    TYPE = "interpreter.token.type"

    PROCEED_IDENTIFIER = "interpreter.token.proc_ident"

    PLUS = "interpreter.token.plus"
    MINUS = "interpreter.token.minus"
    TIMES = "interpreter.token.times"
    DIVIDE = "interpreter.token.divide"
    EQUALS = "interpreter.token.equals"
    POW = "interpreter.token.pow"
    LEFT_PARENTHESIS = "interpreter.token.left_parenthesis"
    RIGHT_PARENTHESIS = "interpreter.token.right_parenthesis"
    LEFT_BRACKET = "interpreter.token.left_bracket"
    RIGHT_BRACKET = "interpreter.token.right_bracker"
    LEFT_ARROW = "interpreter.token.left_arrow"
    RIGHT_ARROW = "interpreter.token.right_arrow"
    DOUBLE_EQUALS = "interpreter.token.double_equals"
    COMMA = "interpreter.token.comma"
    NEWLINE = "interpreter.token.newline"
    EOF = "interpreter.token.eof"

KEYWORDS = [
    "baryabol",
    "ipahayag",
    "na",
    "ay",
    "ang",
    "itala"
]

class Consts:
    DIGITS = "0123456789"
    LETTERS = "_:"+string.ascii_letters
    LETTERS_DIGITS = LETTERS + DIGITS