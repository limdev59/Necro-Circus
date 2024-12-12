from CScene import CScene
from Manager.SceneMgr import sceneMgr
from Sprites.BackGround import BackGround
from Sprites.Player import Player, Weapon, Lance, Club, Boomerang
from Sprites.Monster import Skeleton1, Skeleton2
from UI.Button import Button
from Constants import *
import random

class Scene4(CScene):
    def __init__(self):
        super().__init__()
        self.load_world_map("./src/Assets/Images/title.json")
    def Enter(self):
        start_button = Button("./src/Assets/Images/button.png", x=100, y=300, width=200, height=50, text="Start", on_click=self.start_game)
        exit_button = Button("./src/Assets/Images/button.png", x=100, y=100, width=200, height=50, text="Exit", on_click=self.exit_game)
        self.add_button(start_button)
        self.add_button(exit_button)
        player = Player(960, 550, fps=15, scale=3) 
        weapon = Club(960,550,2,135)
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
        backGround.state = "bg3"
        self.addObj(backGround,     OBJECT_TYPE['BACKGROUND'])
        self.addObj(player,         OBJECT_TYPE['PLAYER'])
        self.addObj(weapon,         OBJECT_TYPE['WEAPON'])
        
        print("Scene4: 플레이어 추가 완료")

    def Exit(self):
        for group in self.arrObj.values():
            for obj in group:
                obj.Clean()
        print("Scene4: 종료")

    def Update(self):
        for group in self.arrObj.values():
            for sprite in group:
                sprite.Update()
    def start_game(self):
        print("게임 시작!")
        return
    def exit_game(self):
        print("게임 시작!")
        return