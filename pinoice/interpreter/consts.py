import string

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

    TAPOS = "interpreter.token.tapos"
    PAGTATAPOS = "interpreter.token.pagtatapos"
    ANG = "interpreter.token.ang"

    PLUS = "interpreter.token.plus"
    MINUS = "interpreter.token.minus"
    MULTIPLY = "interpreter.token.multiply"
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
    "kung",
    "na",
    "ay",
    "itala",
    "ang",
    "tukuyin"
]

class Consts:
    DIGITS = "0123456789"
    LETTERS = "_:"+string.ascii_letters
    LETTERS_DIGITS = LETTERS + DIGITS