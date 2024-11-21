from pico2d import *
import time
_images = {}

def load(file):
    global _images
    if file in _images:
        return _images[file]

    image = load_image(file)
    _images[file] = image
    return image

class Sprite:
    def __init__(self, filename, x, y):
        self.filename = filename
        if filename is None:
          self.image = None
          self.width, self.height = 0, 0
        else:
          self.image = load(filename)
          self.width, self.height = self.image.w, self.image.h
        self.x, self.y = x, y
        self.flip = 1
    def Render(self):
        if self.flip:
            self.image.draw(self.x, self.y, self.width, self.height, -1)  # sx=-1로 반전
        else:
            self.image.draw(self.x, self.y)
    def Update(self):
        pass
    def get_bb(self):
        l = self.x - self.width // 2
        b = self.y - self.height // 2
        r = self.x + self.width // 2
        t = self.y + self.height // 2
        return l, b, r, t
    def contains_xy(self, x, y):
        l,b,r,t = self.get_bb()
        return l <= x < r and b <= y < t
    def fliper(self, fl):
        self.flip = fl
    def __getstate__(self):
        dict = self.__dict__.copy()
        del dict['image']
        return dict
    def __setstate__(self, dict):
        self.__dict__.update(dict)
        # print(f'{self.filename=},')
        Sprite.__init__(self, self.filename, self.x, self.y)

    def __repr__(self):
        return f'{type(self).__name__}({self.filename})'

class AnimSprite(Sprite):
    def __init__(self, filename, x, y, fps, frame_count=0):
        super().__init__(filename, x, y)
        self.fps = fps
        if frame_count == 0: # 정사각형인 경우 0 을 주면 알아서 갯수를 세도록 한다
            frame_count = self.image.w // self.image.h

        if self.image is not None:
          self.width = self.image.w // frame_count
        self.frame_count = frame_count
        self.created_on = time.time()

    def get_anim_index(self):
        elapsed = time.time() - self.created_on
        return round(elapsed * self.fps) % self.frame_count

    def Render(self):
        index = self.get_anim_index()
        if self.flip:  # 좌우반전이 활성화된 경우
            self.image.clip_composite_draw(
                index * self.width, 0,  # 클립 시작 위치
                self.width, self.height,  # 클립 크기
                0,  # 회전 각도 (라디안)
                'h',  # 좌우 반전
                self.x, self.y,  # 그릴 위치
                self.width, self.height  # 크기
            )
        else:
            self.image.clip_draw(
                index * self.width, 0,  # 클립 시작 위치
                self.width, self.height,  # 클립 크기
                self.x, self.y  # 그릴 위치
            )