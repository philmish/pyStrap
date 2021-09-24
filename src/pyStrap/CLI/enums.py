from enum import Enum, auto


class PathType(Enum):
    ABSOLUTE = auto()
    RELATIVE = auto()
    INVALID = auto()

class Confirm(Enum):
    YES = auto()
    NO = auto()
    INVALID = auto