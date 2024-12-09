from Manager.KeyMgr import keyMgr
from Sprite import Sprite, AnimSprite, load
from Manager.SceneMgr import sceneMgr
import time
from Constants import *

class BackGround(AnimSprite):
    def __init__(self, x, y, fps=20, scale = 1):
        super().__init__(x, y, fps, scale)
        self.velocity = [0, 0]
        self.active = True
        self.speed = 7.5
        self.jump_force = 10
        self.gravity = -0.5
        self.on_ground = True
        self.is_jumping = False
        self.state = "bg1"
        self.animations = {}
        self.add_animation("bg1","./src/Assets/Images/backgrounds1.png",1,240,160)
        self.add_animation("bg2","./src/Assets/Images/backgrounds2.png",1,240,160)
        self.add_animation("bg3","./src/Assets/Images/graveyard-correction.png",1,240,160)
        
        
    def Update(self):
        if not self.active:
            return
        self.handle_input()
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.update_state()
        

    def update_state(self):
        self.set_animation(self.state)   

    def handle_input(self):
        self.velocity[0] = 0
        NUM_1 = keyMgr.getKeyState(KEY.NUM_1.value) in [KEY_TYPE.HOLD, KEY_TYPE.TAP]
        NUM_2 = keyMgr.getKeyState(KEY.NUM_2.value) in [KEY_TYPE.HOLD, KEY_TYPE.TAP]
        NUM_3 = keyMgr.getKeyState(KEY.NUM_3.value) in [KEY_TYPE.HOLD, KEY_TYPE.TAP]

        if   NUM_1:
            self.state = "bg1"
        elif NUM_2:
            self.state = "bg2"
        elif NUM_3:
            self.state = "bg3"



  