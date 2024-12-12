from Manager.KeyMgr import keyMgr
from Sprite import AnimSprite, Sprite, load
from Manager.SceneMgr import sceneMgr
from Constants import *
from Config import *
import time

class Weapon(Sprite):
    def __init__(self, x, y, image_file, scale=1, angle=0):
        super().__init__(load(image_file), x, y, scale, angle)  # 부모 클래스의 초기화 호출
        self.angle = angle  # 각도 초기화
        self.weapon_image = self.image  # 무기 이미지 저장

    def set_angle(self, angle):
        """무기의 회전 각도를 설정하는 메서드"""
        self.angle = angle

    def Render(self, camera_x, camera_y):
        """회전된 무기를 화면에 그리는 메서드"""
        if self.weapon_image:
            self.weapon_image.draw_rot(self.x - camera_x, self.y - camera_y, self.scale, self.angle)

    def Update(self):
        """무기의 상태를 업데이트하는 메서드 (추후 추가 기능을 위해 정의 가능)"""
        pass

    def Clean(self):
        """무기 이미지 메모리 해제"""
        print(f"Cleaning Weapon: {self.weapon_image}")
        self.weapon_image = None

class Player(AnimSprite):
    def __init__(self, x, y, fps=20, scale=1):
        super().__init__(x, y, fps, scale)
        self.velocity = [0, 0]
        self.active = True
        self.speed = PLAYER_SPEED
        self.jump_force = 25
        self.gravity = -0.98
        self.on_ground = False  # 초기 상태는 공중으로 설정
        self.is_jumping = False
        self.animations = {}
        self.add_animation("walk", "./src/Assets/Images/player_walk.png", 8, clip_width=64, clip_height=64, start_x=0, start_y=0)
        self.add_animation("idle", "./src/Assets/Images/player_default.png", 5, clip_width=64, clip_height=64, start_x=0, start_y=0)
        self.state = "idle"

        # Health and Invincibility
        self.health = 50  # Initial health
        self.invincible_time = 0  # Time when invincibility starts
        self.invincible_duration = 3  # Invincibility lasts for 3 seconds
        self.knockback = 0

    def Update(self):
        if not self.active:
            return

        # Check if invincibility has expired
        if self.invincible_time > 0 and time.time() - self.invincible_time > self.invincible_duration:
            self.invincible_time = 0  # End invincibility

        prev_x, prev_y = self.x, self.y
        self.apply_gravity()
        self.handle_input()
        self.x += self.velocity[0]+self.knockback
        self.y += self.velocity[1]
        if self.knockback>0:
            self.knockback-=1
        elif self.knockback<0:
            self.knockback+=1

        self.on_ground = False  # 타일 충돌 전까지 공중 상태로 설정
        for tile in sceneMgr.GetCurrentScene().arrObj[OBJECT_TYPE.TILE]:
            if check_collision(self.get_bb(), tile.get_bb()):
                self.handle_tile_collision(tile, prev_x, prev_y)

        self.update_state()

        # Handle collision with enemies (OBJECT_TYPE.ENEMY)
        for enemy in sceneMgr.GetCurrentScene().arrObj[OBJECT_TYPE.ENEMY]:
            if check_collision(self.get_bb(), enemy.get_bb()) and self.invincible_time == 0:
                self.take_damage(10, enemy)  # Take 10 damage from the enemy

    def take_damage(self, damage, enemy):
        self.health -= damage
        self.invincible_time = time.time()  # Start invincibility timer
        knockback_direction = -1 if self.x < enemy.x else 1
        self.knockback = knockback_direction * 30  # Knockback force
        self.velocity[1] = self.jump_force
    def update_state(self):
        if self.velocity[0] != 0:  # 이동 중
            if self.state != "walk":
                self.set_animation("walk")
                self.fps = 10
                self.state = "walk"
        else:
            if self.state != "idle":
                self.set_animation("idle")
                self.fps = 10
                self.state = "idle"

    def apply_gravity(self):
        if not self.on_ground:
            self.velocity[1] += self.gravity

    def handle_input(self):
        left = keyMgr.getKeyState(KEY.a.value) in [KEY_TYPE.HOLD, KEY_TYPE.TAP]
        right = keyMgr.getKeyState(KEY.d.value) in [KEY_TYPE.HOLD, KEY_TYPE.TAP]
        leftoff = keyMgr.getKeyState(KEY.a.value) in [KEY_TYPE.AWAY, KEY_TYPE.NONE]
        rightoff = keyMgr.getKeyState(KEY.d.value) in [KEY_TYPE.AWAY, KEY_TYPE.NONE]
        
        current_scene = sceneMgr.GetCurrentScene()
        
        
        if right:
            self.velocity[0] = self.speed
            self.fliper(False)
            if 960 <= self.x:
                new_camera_x = current_scene.get_camera_x() + self.speed+self.knockback
                current_scene.set_camera_x(min(2615, new_camera_x))

        elif left:
            self.velocity[0] = -self.speed
            self.fliper(True)
            if 3590 >= self.x:
                new_camera_x = current_scene.get_camera_x() - self.speed+self.knockback
                current_scene.set_camera_x(max(0, new_camera_x))
                
        elif rightoff:
            self.velocity[0] = 0
            new_camera_x = current_scene.get_camera_x() +self.knockback
            current_scene.set_camera_x(max(0, new_camera_x))

        elif leftoff:
            new_camera_x = current_scene.get_camera_x() +self.knockback
            current_scene.set_camera_x(max(0, new_camera_x))
            self.velocity[0] = 0  
                
        # 점프 처리
        space = keyMgr.getKeyState(KEY.SPACE.value) in [KEY_TYPE.TAP]
        if space and self.on_ground:
            self.velocity[1] = self.jump_force
            self.is_jumping = True
            self.on_ground = False

    def get_bb(self):
        if not self.current_anim:
            return 0, 0, 0, 0  # 애니메이션이 없으면 히트박스를 0으로 반환

        width = self.clip_width * self.scale
        height = self.clip_height * self.scale
        l = self.x - width // 2
        b = self.y - height // 2
        r = self.x + width // 2
        t = b + height
        return l + 60, b + 5, r - 60, t - 10

    def handle_tile_collision(self, tile, prev_x, prev_y):
        l, b, r, t = self.get_bb()
        tile_l, tile_b, tile_r, tile_t = tile.get_bb()

        # 겹침 크기 계산
        overlap_x = min(r, tile_r) - max(l, tile_l)
        overlap_y = min(t, tile_t) - max(b, tile_b)

        # 겹침 값이 0 이하이면 충돌 아님
        if overlap_x <= 0 or overlap_y <= 0:
            return

        # 가장 작은 겹침 값 기준으로 충돌 보정
        if overlap_x < overlap_y:
            # 좌/우 충돌
            if prev_x < tile_l:  # 왼쪽 충돌
                self.x = tile_l - (r - l) // 2
            elif prev_x > tile_r:  # 오른쪽 충돌
                self.x = tile_r + (r - l) // 2
            self.velocity[0] = 0  # 수평 속도 제거 (벽 매달림 방지)
        else:
            # 상/하 충돌
            if prev_y > tile_t:  # 위쪽 충돌
                self.y = tile_t + (t - b) // 2
                self.on_ground = True  # 땅에 닿음
                self.is_jumping = False
                self.velocity[1] = 0
            elif prev_y < tile_b:  # 아래쪽 충돌
                self.y = tile_b - (t - b) // 2
                self.velocity[1] = min(0, self.velocity[1])  # 아래쪽 충돌 속도 제한

        # 끼임 방지 보정: 아주 작은 겹침이 있을 경우 보정
        if 0 < overlap_x < 2 and 0 < overlap_y < 2:
            self.y += 1  # 위로 살짝 이동
            self.velocity[1] = max(self.velocity[1], 0)  # 속도 멈춤

