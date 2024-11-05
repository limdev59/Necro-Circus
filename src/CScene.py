# CScene.py

class CScene:
    def __init__(self):
        self.initialized = False

    def Initialize(self):
        print(f"{self.__class__.__name__} 씬 초기화")
        self.initialized = True

    def Update(self):
        if not self.initialized:
            print("씬이 초기화되지 않았습니다.")
            return
        print(f"{self.__class__.__name__} 씬 업데이트")

    def Render(self):
        if not self.initialized:
            print("씬이 초기화되지 않았습니다.")
            return
        
        print(f"{self.__class__.__name__} 씬 렌더링")

    def Cleanup(self):
        print(f"{self.__class__.__name__} 씬 정리 중")
        self.initialized = False
