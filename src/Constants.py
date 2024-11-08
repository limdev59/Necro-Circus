from enum import Enum, auto

class EVENT_TYPE(Enum):
    KEYBOARD = auto()
    MOUSE = auto()
    GAME = auto()

class SCENE_TYPE(Enum):
    START = 0
    GAME = 1
    END = 2

class OBJECT_TYPE(Enum):
    END = 0

class KEY(Enum):
    LEFT = 37     # 화살표 왼쪽
    RIGHT = 39    # 화살표 오른쪽
    UP = 38       # 화살표 위
    DOWN = 40     # 화살표 아래
    Q = 81
    W = 87
    E = 69
    R = 82
    T = 84
    Y = 89
    U = 85
    I = 73
    O = 79
    P = 80
    A = 65
    S = 83
    D = 68
    F = 70
    G = 71
    H = 72
    J = 74
    K = 75
    L = 76
    Z = 90
    X = 88
    C = 67
    V = 86
    B = 66
    N = 78
    M = 77
    SPACE = 32
    ENTER = 13
    ESC = 27
    NUM_0 = 48
    NUM_1 = 49
    NUM_2 = 50
    NUM_3 = 51
    NUM_4 = 52
    NUM_5 = 53
    NUM_6 = 54
    NUM_7 = 55
    NUM_8 = 56
    NUM_9 = 57
    LAST = 1000

class KEY_TYPE(Enum):
    NONE = auto()
    TAP = auto()
    HOLD = auto()
    AWAY = auto()