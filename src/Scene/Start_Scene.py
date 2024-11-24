from CScene import CScene
from Manager.SceneMgr import sceneMgr
from Sprites.BackGround import BackGround
from Sprites.Player import Player
from Constants import *

class Start_Scene(CScene):
    def __init__(self):
        super().__init__()
        
    def Enter(self):
        player = Player(960, 400, fps=15, scale=3) 
        backGround = BackGround(WINDOW_WIDTH//2, WINDOW_HEIGHT//2+170, fps=1, scale=5)

        self.addObj(backGround, OBJECT_TYPE['BACKGROUND'])
        self.addObj(player,     OBJECT_TYPE['PLAYER'])
        
        print("Start_Scene: 플레이어 추가 완료")

    def Exit(self):
        for group in self.arrObj.values():
            for obj in group:
                obj.Clean()
        print("Start_Scene: 종료")
