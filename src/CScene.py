from Sprite import Sprite
from Constants import *
from Constants import OBJECT_TYPE

class CScene:
    def __init__(self):
        # Enum 멤버를 사용해 초기화
        self.arrObj = {group: [] for group in OBJECT_TYPE}

    def Update(self):
        for group in self.arrObj.values():
            for sprite in group:
                sprite.Update()

    def Render(self):
        render_order = [
            OBJECT_TYPE.BACKGROUND,
            OBJECT_TYPE.ITEM,
            OBJECT_TYPE.ENEMY,
            OBJECT_TYPE.PLAYER,
        ]
        for group in render_order:
            for obj in self.arrObj[group]:
                obj.Render()

    def Enter(self):
        pass

    def Exit(self):
        pass

    def addObj(self, obj: Sprite, group_type: OBJECT_TYPE):
        self.arrObj[group_type].append(obj)

    def Clean(self):
        # 모든 객체 그룹을 순회하며 각 객체의 Clean 메서드를 호출
        for group, objects in self.arrObj.items():
            for obj in objects:
                obj.Clean()  # 객체의 정리(Clean) 메서드 호출
            objects.clear()  # 그룹 내 모든 객체 제거
        print("CScene: 모든 객체 그룹 정리 완료")
