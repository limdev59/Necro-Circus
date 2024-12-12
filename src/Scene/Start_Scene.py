from CScene import CScene
from Manager.SceneMgr import sceneMgr
from Sprite import AnimSprite
from Sprites.BackGround import BackGround
from Sprites.Player import Player, Weapon, Lance, Club, Boomerang
from Sprites.Monster import Skeleton1, Skeleton2
from UI.Button import Button
from Constants import *
import random

class Start_Scene(CScene):
    def __init__(self):
        super().__init__()
        self.load_world_map("./src/Assets/Images/title.json")
    def Enter(self):
        start_button = Button("./src/Assets/Images/button.png", x=100, y=300, width=200, height=50, text="Start", on_click=self.start_game)
        exit_button = Button("./src/Assets/Images/button.png", x=100, y=100, width=200, height=50, text="Exit", on_click=self.exit_game)
        self.add_button(start_button)
        self.add_button(exit_button)
        backGround = AnimSprite(WINDOW_WIDTH//2, WINDOW_HEIGHT//2+170, fps=1, scale=7)

        self.addObj(backGround,     OBJECT_TYPE['BACKGROUND'])
        
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
    def start_game(self):
        sceneMgr.ChangeScene(SCENE_TYPE.SCENE2.value)
        return
    def exit_game(self):
        print("게임 시작!")
        return