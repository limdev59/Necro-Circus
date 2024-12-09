from Manager.KeyMgr import keyMgr
from Sprite import AnimSprite
from Manager.SceneMgr import sceneMgr
from Constants import *

class Player(AnimSprite):
    def __init__(self, x, y, fps=20, scale = 1):
        super().__init__(x, y, fps, scale)
        self.velocity = [0, 0]
        self.active = True
        self.speed = 10
        self.jump_force = 20
        self.gravity = -0.98
        self.on_ground = True
        self.is_jumping = False
        self.state = "idle"
        self.animations = {
        }
        self.add_animation("idle","./src/Assets/Images/player_default.png",5, clip_width=64, clip_height=64, start_x=0, start_y=0)
        self.add_animation("walk","./src/Assets/Images/player_walk.png",8, clip_width=64, clip_height=64, start_x=0, start_y=0)
        
        
    def Update(self):
        if not self.active:
            return
        self.apply_gravity()
        self.handle_input()
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.update_state()
        self.check_bounds()
        

    def update_state(self):
        if self.velocity[0] != 0:  # 이동 중
            if self.state != "walk":
                self.set_animation("walk")
                self.fps =10
                self.state = "walk"
        else:
            if self.state != "idle":
                self.set_animation("idle")
                self.fps =10
                self.state = "idle"
                
    def apply_gravity(self):
        if not self.on_ground:
            self.velocity[1] += self.gravity
        else:
            self.velocity[1] = max(0, self.velocity[1])

    def handle_input(self):
        self.velocity[0] = 0
        left = keyMgr.getKeyState(KEY.a.value) in [KEY_TYPE.HOLD, KEY_TYPE.TAP]
        right = keyMgr.getKeyState(KEY.d.value) in [KEY_TYPE.HOLD, KEY_TYPE.TAP]

        if left:
            self.velocity[0] = -self.speed
            self.fliper(True)
        elif right:
            self.velocity[0] = self.speed
            self.fliper(False)


        space = keyMgr.getKeyState(KEY.SPACE.value) in [KEY_TYPE.TAP]
        if space and self.on_ground:
            self.velocity[1] = self.jump_force
            self.is_jumping = True
            self.on_ground = False

    def check_bounds(self):
        if self.y <= 400:
            self.y = 400
            self.on_ground = True
            self.is_jumping = False

        if self.x < 0:
            self.x = 0
        elif self.x > 1920:
            self.x = 1920

        if self.y > 1080:
            self.y = 1080
            self.velocity[1] = 0
