from enum import Enum, auto

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

class EVENT_TYPE(Enum):
    KEYBOARD = auto()
    MOUSE = auto()
    GAME = auto()

class SCENE_TYPE(Enum):
    START = 0
    SCENE2 = 1
    SCENE3 = 2
    SCENE4 = 3
    END =  4

class OBJECT_TYPE(Enum):
    PLAYER = 0
    ENEMY = 1
    BACKGROUND= 2
    ITEM = 3
    WEAPON = 4
    TILE= 5
    

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
    a = 97
    b = 98
    c = 99
    d = 100
    e = 101
    f = 102
    g = 103
    h = 104
    i = 105
    j = 106
    k = 107
    l = 108
    m = 109
    n = 110
    o = 111
    p = 112
    q = 113
    r = 114
    s = 115
    t = 116
    u = 117
    v = 118
    w = 119
    x = 120
    y = 121
    z = 122
    LAST = 1000

class KEY_TYPE(Enum):
    NONE = auto()
    TAP = auto()
    HOLD = auto()
    AWAY = auto()
    
def check_collision(a_bb, b_bb):
    """두 객체의 히트박스를 비교하여 충돌 여부를 반환."""
    a_l, a_b, a_r, a_t = a_bb
    b_l, b_b, b_r, b_t = b_bb

    if a_r < b_l or a_l > b_r or a_t < b_b or a_b > b_t:
        return False  # 겹치지 않음
    return True  # 겹침