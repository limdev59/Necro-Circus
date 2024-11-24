from pico2d import *
import time
_images = {}

def load(file):
    global _images
    print(f"Attempting to load image from: {file}")  # 경로 출력
    if file in _images:
        return _images[file]

    image = load_image(file)
    _images[file] = image
    return image


class Sprite:
    def __init__(self, filename, x, y, scale=1):
        self.filename = filename
        if filename is None:
            self.image = None
            self.width, self.height = 0, 0
        else:
            self.image = load(filename)
            self.width, self.height = self.image.w, self.image.h
        self.x, self.y = x, y
        self.scale = scale
        self.flip = 1

    def Render(self):
        if self.flip:
            self.image.draw(self.x, self.y, self.width * self.scale, self.height * self.scale, -1)  # sx=-1로 반전
        else:
            self.image.draw(self.x, self.y, self.width * self.scale, self.height * self.scale)

    def Update(self):
        pass

    def get_bb(self):
        l = self.x - self.width // 2
        b = self.y - self.height // 2
        r = self.x + self.width // 2
        t = self.y + self.height // 2
        return l, b, r, t

    def contains_xy(self, x, y):
        l, b, r, t = self.get_bb()
        return l <= x < r and b <= y < t

    def fliper(self, fl):
        self.flip = fl

    def __getstate__(self):
        dict = self.__dict__.copy()
        del dict['image']
        return dict

    def __setstate__(self, dict):
        self.__dict__.update(dict)
        Sprite.__init__(self, self.filename, self.x, self.y)

    def __repr__(self):
        return f'{type(self).__name__}({self.filename})'


class AnimSprite(Sprite):
    def __init__(self, x, y, fps=20, scale = 1):
        super().__init__(None, x, y, scale)
        self.fps = fps
        self.animations = {}
        self.current_anim = None
        self.created_on = time.time()

    def add_animation(self, state, filename, frame):
        if state in self.animations:
            anim = self.animations[state]
            
        self.state = state
        self.image = load(filename)
        self.created_on = time.time()
        self.frame_count = frame
        self.width = self.image.w // self.frame_count
        self.height = self.image.h
        self.animations[state] = {
            "image": self.image,
            "frame_count": self.frame_count,
            "width": self.width,
            "height": self.height,
        }
        if not self.current_anim:
            self.set_animation(state)

    def set_animation(self, anim_name):
        if anim_name not in self.animations:
            raise ValueError(f"애니메이션 '{anim_name}'이(가) 존재하지 않습니다.")
        self.current_anim = anim_name
        anim_data = self.animations[anim_name]
        self.image = anim_data["image"]
        self.frame_count = anim_data["frame_count"]
        self.width = anim_data["width"]
        self.height = anim_data["height"]
        self.created_on = time.time()

    def get_anim_index(self):
        elapsed = time.time() - self.created_on
        return round(elapsed * self.fps) % self.frame_count

    def Render(self):
        if not self.current_anim:
            return

        index = self.get_anim_index()
        if self.flip:
            self.image.clip_composite_draw(
                index * self.width, 0,
                self.width, self.height,
                0,
                'h',
                self.x, self.y,
                self.width * self.scale, self.height *  self.scale, 
            )
        else:
            self.image.clip_draw(
                index * self.width, 0,
                self.width, self.height,
                self.x, self.y,
                self.width*  self.scale, self.height*  self.scale,
            )

    def Clean(self):
        print(f"Cleaning Sprite: {self.filename}")
        self.image = None  # 이미지 참조 해제
