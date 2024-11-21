from Sprite import Sprite
from Constants import *
from Constants import OBJECT_TYPE

class CScene:
    def __init__(self):
        # Enum 멤버를 사용해 초기화
        self.arrObj = {group: [] for group in OBJECT_TYPE}

    def Update(self):
        pass

    def Render(self):
        pass

    def Enter(self):
        pass

    def Exit(self):
        pass

    def addObj(self, obj: Sprite, group_type: OBJECT_TYPE):
        # Enum 멤버를 키로 사용
        self.arrObj[group_type].append(obj)
