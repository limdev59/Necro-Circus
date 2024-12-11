import json
from Sprite import Sprite, load
from Constants import *
from Constants import OBJECT_TYPE
from tiledmap import TiledMap

class CScene:
    def __init__(self):
        # Enum 멤버를 사용해 초기화
        self.arrObj = {group: [] for group in OBJECT_TYPE}
        self.tiled_map = None  # TiledMap 객체 추가
        self.scale = 18
        self.load_world_map("./src/Assets/Images/title.tmj")
    def load_world_map(self, tmx_file_path):
        # .tmj 파일을 읽어서 타일맵 정보를 로드
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

    def Render(self):
        # 월드맵 타일을 렌더링
        self.render_tiles()

        render_order = [
            OBJECT_TYPE.BACKGROUND,
            OBJECT_TYPE.ITEM,
            OBJECT_TYPE.ENEMY,
            OBJECT_TYPE.PLAYER,
        ]
        for group in render_order:
            for obj in self.arrObj[group]:
                obj.Render()
    
    def render_tiles(self):
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

                                self.tile_image.clip_draw(
                                    left=tile_x * tileset.tilewidth,
                                    bottom=tile_y * tileset.tileheight,
                                    width=tileset.tilewidth,
                                    height=tileset.tileheight,
                                    x=(x * tile_width * self.scale),
                                    y=WINDOW_HEIGHT - (y * tile_height * self.scale),
                                    w=tileset.tilewidth * self.scale,
                                    h=tileset.tileheight * self.scale
                                )


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

    def Clean(self):
        # 모든 객체 그룹을 순회하며 각 객체의 Clean 메서드를 호출
        for group, objects in self.arrObj.items():
            for obj in objects:
                obj.Clean()  # 객체의 정리(Clean) 메서드 호출
            objects.clear()  # 그룹 내 모든 객체 제거
        print("CScene: 모든 객체 그룹 정리 완료")
