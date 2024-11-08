from CScene import CScene
#from CObject import CObject
from Constants import *

class Start_Scene(CScene):
    def __init__(self):
        super().__init__()
        # print(f"{self.__class__.__name__} 씬 구성 초기화")

    def Init(self):
        super().Init()
        # print(f"{self.__class__.__name__} 씬 초기화 완료")

    def Update(self):
        super().Update()
        # print(f"{self.__class__.__name__} 씬에서 추가적인 업데이트 수행")

    def Render(self):
        super().Render()
        # print(f"{self.__class__.__name__} 씬에서 추가적인 렌더링 수행")

    def Clean(self):
        super().Clean()
        # print(f"{self.__class__.__name__} 씬 정리 완료")
