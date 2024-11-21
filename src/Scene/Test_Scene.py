from CScene import CScene
from Sprites.Player import Player
from Constants import *

class Test_Scene(CScene):
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
        player1 = Player(
            filename="c:/Users/bigma/Documents/GitHub/Necro-Circus/src/Assets/Images/player_default.png",
            x=300,
            y=300
        )
        self.addObj(player1, OBJECT_TYPE['PLAYER'])

        player2 = Player(
            filename="c:/Users/bigma/Documents/GitHub/Necro-Circus/src/Assets/Images/player_default.png",
            x=500,
            y=300
        )
        self.addObj(player2, OBJECT_TYPE['PLAYER'])

        print("Test_Scene: 두 명의 플레이어 추가 완료")

    def Exit(self):
        for group in self.arrObj.values():
            for obj in group:
                obj.Clean()
        print("Test_Scene: 종료")
