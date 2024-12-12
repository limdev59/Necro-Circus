from pico2d import *
from Sprite import Sprite, load

class Button(Sprite):
    def __init__(self, image, x, y, width, height, text="", on_click=None):
        super().__init__(load(image), x, y, 1)
        self.width = width
        self.height = height
        self.text = text
        self.on_click = on_click  # 클릭 이벤트 핸들러
        self.enabled = True
        self.font = None  # 폰트를 나중에 로드하거나 설정
        self.scale = 5

    def set_font(self, font_path, font_size):
        """폰트를 설정합니다."""
        self.font = load_font(font_path, font_size)

    def contains_point(self, px, py):
        l, b, r, t = self.get_bb()  # get_bb()는 스프라이트의 bounding box를 가져옵니다
        return l <= px <= r and b <= 1080-py <= t  # 클릭 위치가 버튼 영역 내에 있는지 확인

    def Render(self, camera_x, camera_y):
        if self.enabled:
            if self.image:
                self.image.draw(self.x, self.y , self.image.w * self.scale, self.image.h * self.scale)

            if self.text and self.font:
                # 텍스트의 중심을 버튼의 중심으로 설정
                text_x = self.x - camera_x
                text_y = self.y - camera_y
                text_width = self.font.get_width(self.text)
                text_height = self.font.get_height()
                self.font.draw(
                    text_x - text_width // 2,  # 텍스트 중심을 버튼 중심에 맞춤
                    text_y - text_height // 2,  # 텍스트 높이를 기준으로 중심 배치
                    self.text,
                    (255, 255, 255)  # 텍스트 색상 (흰색)
                )

    def handle_click(self, px, py):
        if self.contains_point(px, py):  # 클릭한 위치가 버튼 영역 안에 있을 때
            if self.on_click:
                self.on_click()  # 버튼 클릭 시 실행할 함수 호출