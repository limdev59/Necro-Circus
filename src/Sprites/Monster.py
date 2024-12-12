from Manager.SceneMgr import sceneMgr
from Manager.KeyMgr import keyMgr
from Sprite import AnimSprite
from Constants import *
import random
import time

class Skeleton1(AnimSprite):
    def __init__(self, x, y, fps=20, scale=1):
        super().__init__(x, y, fps, scale)
        self.velocity = [0, 0]
        self.active = True
        self.speed = 5  # 플레이어를 따라가는 속도
        self.jump_force = 15
        self.gravity = -0.98
        self.on_ground = True
        self.is_jumping = False
        self.target = None  # 따라갈 대상 (플레이어)
        self.animations = {
        }
        self.add_animation("knock_back", "./src/Assets/Images/Skeletons.png", 1, clip_width=31, clip_height=46, start_x=1, start_y=2)
        self.add_animation("walk", "./src/Assets/Images/Skeletons.png", 8, clip_width=31, clip_height=48, start_x=34, start_y=2)
        self.add_animation("idle", "./src/Assets/Images/Skeletons.png", 1, clip_width=31, clip_height=46, start_x=1, start_y=2)
        self.state = "idle"

        # 점프 관련 타이머 설정
        self.jump_interval = random.uniform(1.5, 5.0)  # 랜덤 시간 간격 (1.5초 ~ 3초 사이)
        self.last_jump_time = time.time()  # 마지막 점프 시간 기록

        self.health = 100  # Initial health
        self.invincible_time = 0  # Time when invincibility starts
        self.invincible_duration = 2  # Invincibility lasts for 3 seconds
        self.knockback = 0
    def die(self):
        self.set_animation("death")
        self.Clean()
        
    def Update(self):
        if not self.active:
            return

        current_time = time.time()
        
        if self.health <= 0:
            self.Clean()  # 체력이 0 이하일 때 죽음 처리
            return
        # 랜덤 시간마다 점프하도록 설정
        if current_time - self.last_jump_time > self.jump_interval and self.on_ground:
            self.jump()
            self.last_jump_time = current_time  # 점프한 시간 기록
            self.jump_interval = random.uniform(1.5, 3.0)  # 다음 점프 간격을 랜덤으로 설정

        if self.invincible_time > 0 and current_time - self.invincible_time > self.invincible_duration:
            self.invincible_time = 0  # End invincibility
        
        prev_x, prev_y = self.x, self.y
        self.apply_gravity()
        self.follow_target()
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
        for weapon in sceneMgr.GetCurrentScene().arrObj[OBJECT_TYPE.WEAPON]:
            if check_collision(self.get_bb(), weapon.get_bb()) and self.invincible_time == 0:
                if weapon.name == 'lance':
                    self.take_damage(15, weapon)
                    self.invincible_duration-=1
                elif weapon.name == 'club':
                    self.take_damage(10, weapon)
                    self.invincible_duration-=1
                elif weapon.name == 'boomerang':
                    self.take_damage(25, weapon)
                    self.invincible_duration-=1

    def take_damage(self, damage, enemy):
        self.health -= damage
        self.invincible_time = time.time()
        knockback_direction = -1 if self.x < enemy.x else 1
        self.knockback = knockback_direction * 30
        self.velocity[1] = self.jump_force
        self.set_animation("knock_back")
        self.fps = 10
        self.state = "knock_back"
        
    def jump(self):
        if self.on_ground:
            self.velocity[1] = self.jump_force  # 점프 힘 적용
            self.is_jumping = True
            self.on_ground = False

    def update_state(self):
        if self.is_jumping:
            if self.state != "knock_back":
                self.set_animation("knock_back")
                self.fps = 10
                self.state = "knock_back"
        elif self.velocity[0] != 0:  # 이동 중
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
        if self.on_ground:
            self.velocity[1] = 0
            self.is_jumping = False

    def follow_target(self):
        target_x, target_y = self.target.x, self.target.y

        # x축 방향 이동
        if self.x < target_x:
            self.velocity[0] = self.speed
            self.fliper(True)
        elif self.x > target_x:
            self.velocity[0] = -self.speed
            self.fliper(False)
        else:
            self.velocity[0] = 0  # 정지

    def get_bb(self):
        if not self.current_anim:
            return 0, 0, 0, 0  # 애니메이션이 없으면 히트박스를 0으로 반환

        width = self.clip_width * self.scale
        height = self.clip_height * self.scale
        l = self.x - width // 2
        b = self.y - height // 2
        r = self.x + width // 2
        t = b + height
        return l + 2, b+2, r - 2, t
    
    def handle_tile_collision(self, tile, prev_x, prev_y):
        l, b, r, t = self.get_bb()
        tile_l, tile_b, tile_r, tile_t = tile.get_bb()
        # 겹침 크기 계산
        overlap_x = min(r, tile_r) - max(l, tile_l)
        overlap_y = min(t + 20, tile_t) - max(b, tile_b)

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
                self.y = tile_t + (t - 10 - b) // 2
                self.on_ground = True  # 땅에 닿음
                self.is_jumping = False
                self.velocity[1] = 0
            elif prev_y < tile_b:  # 아래쪽 충돌
                self.y = tile_b - (t - 10 - b) // 2
                self.velocity[1] = min(0, self.velocity[1])  # 아래쪽 충돌 속도 제한

        # 끼임 방지 보정: 아주 작은 겹침이 있을 경우 보정
        if 0 < overlap_x < 2 and 0 < overlap_y < 2:
            self.y += 1  # 위로 살짝 이동
            self.velocity[1] = max(self.velocity[1], 1)  # 속도 멈춤

class Skeleton2(Skeleton1):
    def __init__(self, x, y, fps=20, scale = 1):
        super().__init__(x, y, fps, scale)
        self.add_animation("knock_back","./src/Assets/Images/Skeletons.png",1, clip_width=31, clip_height=46, start_x=1, start_y=55)
        self.add_animation("walk","./src/Assets/Images/Skeletons.png",8, clip_width=31, clip_height=48, start_x=34, start_y=55)
        self.add_animation("idle","./src/Assets/Images/Skeletons.png",1, clip_width=31, clip_height=46, start_x=1, start_y=55)
      
        self.state = "idle"