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
    def __init__(self,image, x, y, scale=1):
        self.x, self.y = x, y
        self.scale = scale
        self.image = image
        self.flip = 1

    def Render(self, camera_x, camera_y):
        pass
    def Update(self):
        pass


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
    def __init__(self, x, y, fps=20, scale=1):
        super().__init__(None, x, y, scale)
        self.fps = fps
        self.animations = {}
        self.current_anim = None
        self.created_on = time.time()

    def add_animation(self, state, filename, frame, clip_width, clip_height, start_x=0, start_y=0):
        self.image = load(filename)
        image_height = self.image.h  # 이미지의 전체 높이를 가져옴
        self.animations[state] = {
            "image": self.image,
            "frame_count": frame,
            "clip_width": clip_width,
            "clip_height": clip_height,
            "start_x": start_x,
            "start_y": image_height - start_y - clip_height,  # 상단 기준으로 변환
        }
        self.set_animation(state)

    def set_animation(self, anim_name):
        if anim_name not in self.animations:
            raise ValueError(f"애니메이션 '{anim_name}'이(가) 존재하지 않습니다.")
        self.current_anim = anim_name
        anim_data = self.animations[anim_name]
        self.image = anim_data["image"]
        self.frame_count = anim_data["frame_count"]
        self.clip_width = anim_data["clip_width"]
        self.clip_height = anim_data["clip_height"]
        self.start_x = anim_data["start_x"]
        self.start_y = anim_data["start_y"]
        self.created_on = time.time()

    def get_anim_index(self):
        elapsed = time.time() - self.created_on
        return round(elapsed * self.fps) % self.frame_count
    def get_bb(self):
        if not self.current_anim:
            return 0, 0, 0, 0  # 애니메이션이 없으면 히트박스를 0으로 반환

        width = self.clip_width * self.scale
        height = self.clip_height * self.scale
        l = self.x - width // 2
        b = self.y - height // 2  # 중심에서 clip_height의 절반만큼 내려감
        r = self.x + width // 2
        t = b + height
        return l, b, r, t
    
    def Render(self, camera_x, camera_y):
        if not self.current_anim:
            return

        index = self.get_anim_index()
        src_x = self.start_x + index * self.clip_width
        src_y = self.start_y
        l, b, r, t = self.get_bb()
        
        if self.flip:
            self.image.clip_composite_draw(
                src_x, src_y,
                self.clip_width, self.clip_height,
                0, 'h',
                self.x-camera_x, self.y-camera_y,
                self.clip_width * self.scale, self.clip_height * self.scale
            )
        else:
            self.image.clip_draw(
                src_x, src_y,
                self.clip_width, self.clip_height,
                self.x-camera_x, self.y-camera_y,
                self.clip_width * self.scale, self.clip_height * self.scale
            )
        draw_rectangle(l-camera_x, b-camera_y, r-camera_x, t-camera_y)

    def Clean(self):
        print(f"Cleaning Sprite: {self.filename}")
        self.image = None  # 이미지 참조 해제