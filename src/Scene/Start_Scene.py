from CScene import CScene
from Manager.SceneMgr import sceneMgr
from Sprites.BackGround import BackGround
from Sprites.Player import Player
from Sprites.Monster import Skeleton1, Skeleton2
from Constants import *
import random

class Start_Scene(CScene):
    def __init__(self):
        super().__init__()
        self.load_world_map("./src/Assets/Images/title.tmj")
    def Enter(self):
        player = Player(960, 550, fps=15, scale=3) 
        
        for i in range(3):
            monster = Skeleton1(600, 600, fps=15, scale=3) 
            monster.target = player
            monster.speed = random.uniform(3.0, 10.0)
            self.addObj(monster,        OBJECT_TYPE['ENEMY'])
            monster2 = Skeleton2(300, 600, fps=15, scale=2) 
            monster2.target = player
            monster2.speed = random.uniform(9.0, 11.0)
            self.addObj(monster2,       OBJECT_TYPE['ENEMY'])
            
        backGround = BackGround(WINDOW_WIDTH//2, WINDOW_HEIGHT//2+170, fps=1, scale=7)

        self.addObj(backGround,     OBJECT_TYPE['BACKGROUND'])
        self.addObj(player,         OBJECT_TYPE['PLAYER'])
        
        print("Start_Scene: 플레이어 추가 완료")

    def Exit(self):
        for group in self.arrObj.values():
            for obj in group:
                obj.Clean()
        print("Start_Scene: 종료")

    def Update(self):
        for group in self.arrObj.values():
            for sprite in group:
                sprite.Update()