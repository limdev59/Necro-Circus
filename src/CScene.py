import json
from Manager.KeyMgr import keyMgr
from Sprite import Sprite, load
from Constants import *
from Constants import OBJECT_TYPE
from tiledmap import TiledMap
from Sprites.BackGround import Tile
from Config import *

class CScene:
    def __init__(self):
        self.arrObj = {group: [] for group in OBJECT_TYPE}
        self.buttons = []  # 버튼 리스트 추가
        self.tiled_map = None 
        self.scale = 18
        self.camera_x = 0  # 카메라 절대 좌표
        self.camera_y = 70
        self.load_world_map("./src/Assets/Images/title.json")
        self.add_tiles()

    def add_button(self, button):
        self.buttons.append(button)

    def handle_mouse_click(self, x, y):
        """마우스 클릭 처리"""
        for button in self.buttons:
            button.handle_click(x, y)
    def load_world_map(self, tmx_file_path):
        with open(tmx_file_path, 'r') as f:
            data = json.load(f)
        
        # 타일맵 데이터를 TiledMap 클래스로 변환
        self.tiled_map = TiledMap.from_dict(data)
        
        # 타일셋 이미지 로딩
        for tileset in self.tiled_map.tilesets:
            image_path = tileset.image
            self.tile_image = load("./src/Assets/Images/" + image_path)

    def Update(self):
        for group in self.arrObj.values():
            for sprite in group:
                sprite.Update()
        pass

    def Render(self):
        # 카메라 절대 좌표 기반 렌더링
        render_order = [    
            OBJECT_TYPE.BACKGROUND,
            OBJECT_TYPE.TILE,
            OBJECT_TYPE.ITEM,
            OBJECT_TYPE.ENEMY,
            OBJECT_TYPE.WEAPON,
            OBJECT_TYPE.PLAYER,
        ]
        for group in render_order:
            for obj in self.arrObj[group]:
                obj.Render(self.camera_x,self.camera_y)
                
        # 버튼 렌더링
        for button in self.buttons:
            button.Render(self.camera_x, self.camera_y)
    
    def add_tiles(self):
        if self.tiled_map:
            # 타일맵의 전역 타일 크기 가져오기
            tile_width = self.tiled_map.tilewidth
            tile_height = self.tiled_map.tileheight

            for layer in self.tiled_map.layers:
                if layer.visible:  # 레이어가 visible일 때만 처리
                    for y in range(layer.height):
                        for x in range(layer.width):
                            tile_index = layer.data[y * layer.width + x]  # 타일의 인덱스를 데이터에서 가져옴
                            if tile_index > 0:  # tile_index가 0이면 빈칸이므로 렌더링하지 않음
                                tileset = self.get_tileset_for_tile(tile_index)
                                tile_x = (tile_index - tileset.firstgid) % tileset.columns
                                tile_y = (tile_index - tileset.firstgid) // tileset.columns

                                tiles = Tile(
                                    self.tile_image,
                                    left=tile_x * tileset.tilewidth,
                                    bottom=tile_y * tileset.tileheight,
                                    width=tileset.tilewidth,
                                    height=tileset.tileheight,
                                    x=(x * tile_width * self.scale),
                                    y=WINDOW_HEIGHT - (y * tile_height * self.scale),
                                    w=tileset.tilewidth * self.scale,
                                    h=tileset.tileheight * self.scale,
                                    scale=self.scale
                                )
                                self.addObj(tiles, OBJECT_TYPE['TILE'])

    def get_tileset_for_tile(self, tile_index):
        # 주어진 타일 인덱스에 맞는 타일셋을 찾는 함수
        for tileset in self.tiled_map.tilesets:
            if tile_index >= tileset.firstgid:
                return tileset
        return None  # 해당 타일셋을 찾을 수 없는 경우

    def Enter(self):
        pass

    def Exit(self):
        pass

    def addObj(self, obj: Sprite, group_type: OBJECT_TYPE):
        self.arrObj[group_type].append(obj)

    def get_camera_x(self):
        return self.camera_x

    # camera_x의 setter 함수
    def set_camera_x(self, value):
        self.camera_x = value

    # camera_y의 getter 함수
    def get_camera_y(self):
        return self.camera_y

    # camera_y의 setter 함수
    def set_camera_y(self, value):
        self.camera_y = value
    
    def Clean(self):
        # 기존 객체 정리
        for group, objects in self.arrObj.items():
            
            objects.clear()
        
        # 버튼 정리
        self.buttons.clear()
        print("CScene: 모든 버튼 정리 완료")