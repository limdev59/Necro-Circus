from CObject import CObject
from Constants import *


class CScene:
    def __init__(self):
        self.arrObj = {group: [] for group in OBJECT_TYPE}
        self.initialized = False

    def Init(self):
        self.initialized = True

    def Update(self):
        if not self.initialized:
            print("씬이 초기화되지 않았습니다.")
            return

    def Render(self):
        if not self.initialized:
            print("씬이 초기화되지 않았습니다.")
            return

    def Clean(self):
        self.initialized = False

    def addObj(self, obj: CObject, group_type: OBJECT_TYPE):
        self.arrObj[group_type].append(obj)
