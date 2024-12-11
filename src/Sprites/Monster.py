from Manager.SceneMgr import sceneMgr
from Manager.KeyMgr import keyMgr
from Sprite import AnimSprite
from Constants import *

class Skeleton1(AnimSprite):
    def __init__(self, x, y, fps=20, scale = 1):
        super().__init__(x, y, fps, scale)
        self.velocity = [0, 0]
        self.active = True
        self.speed = 10
        self.jump_force = 20
        self.gravity = -0.98
        self.on_ground = True
        self.is_jumping = False
        self.animations = {
        }
        self.add_animation("knock_back","./src/Assets/Images/Skeletons2.png",1, clip_width=31, clip_height=46, start_x=1, start_y=2)
        self.add_animation("idle","./src/Assets/Images/Skeletons2.png",1, clip_width=31, clip_height=46, start_x=1, start_y=2)
        self.add_animation("walk","./src/Assets/Images/Skeletons2.png",8, clip_width=31, clip_height=48, start_x=34, start_y=2)
        self.state = "idle"
        
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
        if self.velocity[0] != 0:
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
            self.fliper(False)
        elif right:
            self.velocity[0] = self.speed
            self.fliper(True)


        space = keyMgr.getKeyState(KEY.SPACE.value) in [KEY_TYPE.TAP]
        if space and self.on_ground:
            self.velocity[1] = self.jump_force
            self.is_jumping = True
            self.on_ground = False

    def check_bounds(self):
        ground_y = 400
        screen_width = 1920
        screen_height = 1080
        l, b, r, t = self.get_bb()

        if b <= ground_y:
            self.y += ground_y - b
            self.on_ground = True
            self.is_jumping = False
            self.velocity[1] = 0

        if l < 0:  # 화면 좌측 경계
            self.x += -l  # x 좌표를 조정하여 히트박스가 화면 안으로 들어오게 함
        elif r > screen_width:  # 화면 우측 경계
            self.x -= (r - screen_width)

        # 상단 경계 충돌
        if t > screen_height:  # 화면 상단 경계
            self.y -= (t - screen_height)
            self.velocity[1] = 0


class Skeleton2(Skeleton1):
    def __init__(self, x, y, fps=20, scale = 1):
        super().__init__(x, y, fps, scale)
        self.add_animation("idle","./src/Assets/Images/Skeletons2.png",1, clip_width=31, clip_height=46, start_x=1, start_y=55)
        self.add_animation("walk","./src/Assets/Images/Skeletons2.png",8, clip_width=31, clip_height=48, start_x=34, start_y=55)
        self.state = "idle"