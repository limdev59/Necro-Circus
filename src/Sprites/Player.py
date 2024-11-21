from Manager.KeyMgr import keyMgr
from Sprite import Sprite, AnimSprite
from Constants import *

class Player(AnimSprite):
    def __init__(self, filename, x, y, fps=10, frame_count=5):
        # AnimSprite 초기화
        super().__init__(filename, x, y, fps, frame_count)
        
        # 기본적인 이동과 점프 관련 속성 설정
        self.velocity = [0, 0]
        self.active = True
        self.speed = 5
        self.jump_force = 10
        self.gravity = -0.5
        self.on_ground = True
        self.is_jumping = False
        self.frame = 0  # 애니메이션 프레임 초기화
        self.frame_count = frame_count

    def Update(self):
        if not self.active:
            return
        
        self.apply_gravity()
        self.handle_input()

        self.x += self.velocity[0]
        self.y += self.velocity[1]

        self.check_bounds()

    def apply_gravity(self):
        if not self.on_ground:
            self.velocity[1] += self.gravity 
        else:
            self.velocity[1] = max(0, self.velocity[1])

    def handle_input(self):
        self.velocity[0] = 0
        left = keyMgr.getKeyState(KEY.a.value) in [KEY_TYPE.HOLD, KEY_TYPE.TAP]
        right = keyMgr.getKeyState(KEY.d.value) in [KEY_TYPE.HOLD, KEY_TYPE.TAP]

        if left and not right:
            self.velocity[0] = -self.speed
            self.fliper(False)
        elif right and not left:
            self.velocity[0] = self.speed
            self.fliper(True)

        space = keyMgr.getKeyState(KEY.SPACE.value) in [KEY_TYPE.TAP]
        if space and self.on_ground:
            self.velocity[1] = self.jump_force
            self.is_jumping = True
            self.on_ground = False

    def check_bounds(self):
        if self.y <= 300:  # 지면과의 충돌 처리
            self.y = 300
            self.on_ground = True
            self.is_jumping = False

        if self.x < 0:  # 좌측 경계 처리
            self.x = 0
        elif self.x > 800:  # 우측 경계 처리
            self.x = 800

        if self.y > 600:  # 상단 경계 처리
            self.y = 600
            self.velocity[1] = 0  # y 속도 초기화