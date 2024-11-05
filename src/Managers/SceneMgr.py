from CCore import CCore
from CScene import CScene
from enum import Enum

class SCENE_TYPE(Enum):
    START = 0
    GAME = 1
    END = 2

class SceneMgr:
    def __init__(self):
        self.arrScene = [None] * len(SCENE_TYPE) 
        self.currentScene = None

    def Init(self):
        self.arrScene[SCENE_TYPE.START.value] = CScene()
        self.arrScene[SCENE_TYPE.GAME.value] = CScene()
        self.arrScene[SCENE_TYPE.END.value] = CScene()
        
        self.currentScene = self.arrScene[SCENE_TYPE.START.value]
        self.currentScene.Initialize()

    def Update(self):
        if self.currentScene:
            self.currentScene.Update()

    def Render(self):
        if self.currentScene:
            self.currentScene.Render()

    def ChangeScene(self, new_scene_type):
        if self.currentScene:
            self.currentScene.Cleanup()
        self.currentScene = self.arrScene[new_scene_type.value] 
        self.currentScene.Initialize()
