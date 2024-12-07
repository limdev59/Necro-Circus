from CScene import CScene
from Constants import *


class SceneMgr:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def Init(self):
        self.arrScene = {scene_type: None for scene_type in SCENE_TYPE}
        self.currentScene = None

        from Scene.Start_Scene import Start_Scene
        from Scene.Test_Scene import Test_Scene
        
        self.arrScene[SCENE_TYPE.START.value] = Start_Scene() 
        self.arrScene[SCENE_TYPE.TEST.value] = Test_Scene()
        self.arrScene[SCENE_TYPE.END.value] = CScene()

        self.currentScene = self.arrScene[SCENE_TYPE.START.value]
        self.currentScene.Enter()

    def Update(self):
        if self.currentScene:
            self.currentScene.Update()

    def Render(self):
        if self.currentScene:
            self.currentScene.Render()

    def ChangeScene(self, new_scene_type):
        if self.currentScene:
            self.currentScene.Clean()
        self.currentScene = self.arrScene[new_scene_type.value]
        self.currentScene.Enter()
        
    def GetCurrentScene(self):
        return self.currentScene
        
sceneMgr = SceneMgr()