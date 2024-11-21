from CScene import CScene
from Sprites.Player import Player
# from Manager.SceneMgr import sceneMgr
from Constants import *

class Start_Scene(CScene):
    def __init__(self):
        super().__init__()

    def Update(self):
        for group in self.arrObj.values():
            for sprite in group:
                sprite.Update()

    def Render(self):
        for group in self.arrObj.values():
            for obj in group:
                obj.Render()

    def Enter(self):
        player = Player(
            filename="c:/Users/bigma/Documents/GitHub/Necro-Circus/src/Assets/Images/player_default.png",
            x=400,
            y=300
        )   
        self.addObj(player, OBJECT_TYPE['PLAYER'])
        if player.x > 790:
            sceneMgr.ChangeScene(SCENE_TYPE.TEST)
            
        print("Start_Scene: 플레이어 추가 완료")

    def Exit(self):
        for group in self.arrObj.values():
            for obj in group:
                obj.Clean()
        print("Start_Scene: 종료")
