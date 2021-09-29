from typing import Any, Tuple
from types import TracebackType

class ExceptionEnum:
    VARIABLE_NOT_FOUND = "commands.not.found"

class ThrowException:
    def __init__(self, name):
        Exception(name)