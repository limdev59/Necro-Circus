from typing import Any, List, TypeVar, Type, cast, Callable


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, (int, float))
    return x



class Layer:
    def __init__(self, data, height, id, name, opacity, type, visible, width, x, y):
        self.data = data
        self.height = height
        self.id = id
        self.name = name
        self.opacity = opacity
        self.type = type
        self.visible = visible
        self.width = width
        self.x = x
        self.y = y

    @staticmethod
    def from_dict(obj):
        data = from_list(from_int, obj.get("data"))
        height = from_int(obj.get("height"))
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        opacity = from_int(obj.get("opacity"))
        type = from_str(obj.get("type"))
        visible = from_bool(obj.get("visible"))
        width = from_int(obj.get("width"))
        x = from_int(obj.get("x"))
        y = from_int(obj.get("y"))
        return Layer(data, height, id, name, opacity, type, visible, width, x, y)

    def to_dict(self):
        result = {}
        result["data"] = from_list(from_int, self.data)
        result["height"] = from_int(self.height)
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["opacity"] = from_int(self.opacity)
        result["type"] = from_str(self.type)
        result["visible"] = from_bool(self.visible)
        result["width"] = from_int(self.width)
        result["x"] = from_int(self.x)
        result["y"] = from_int(self.y)
        return result


class Tileset:
    def __init__(self, columns, firstgid, image, imageheight, imagewidth, margin, name, spacing, tilecount, tileheight, tilewidth):
        self.columns = columns
        self.firstgid = firstgid
        self.image = image
        self.imageheight = imageheight
        self.imagewidth = imagewidth
        self.margin = margin
        self.name = name
        self.spacing = spacing
        self.tilecount = tilecount
        self.tileheight = tileheight
        self.tilewidth = tilewidth

    @staticmethod
    def from_dict(obj):
        columns = from_int(obj.get("columns"))
        firstgid = from_int(obj.get("firstgid"))
        image = from_str(obj.get("image"))
        imageheight = from_int(obj.get("imageheight"))
        imagewidth = from_int(obj.get("imagewidth"))
        margin = from_int(obj.get("margin"))
        name = from_str(obj.get("name"))
        spacing = from_int(obj.get("spacing"))
        tilecount = from_int(obj.get("tilecount"))
        tileheight = from_int(obj.get("tileheight"))
        tilewidth = from_int(obj.get("tilewidth"))
        return Tileset(columns, firstgid, image, imageheight, imagewidth, margin, name, spacing, tilecount, tileheight, tilewidth)

    def to_dict(self):
        result = {}
        result["columns"] = from_int(self.columns)
        result["firstgid"] = from_int(self.firstgid)
        result["image"] = from_str(self.image)
        result["imageheight"] = from_int(self.imageheight)
        result["imagewidth"] = from_int(self.imagewidth)
        result["margin"] = from_int(self.margin)
        result["name"] = from_str(self.name)
        result["spacing"] = from_int(self.spacing)
        result["tilecount"] = from_int(self.tilecount)
        result["tileheight"] = from_int(self.tileheight)
        result["tilewidth"] = from_int(self.tilewidth)
        return result


class TiledMap:
    def __init__(self, compressionlevel, height, infinite, layers, nextlayerid, nextobjectid, orientation, renderorder, tiledversion, tileheight, tilesets, tilewidth, type, version, width):
        self.compressionlevel = compressionlevel
        self.height = height
        self.infinite = infinite
        self.layers = layers
        self.nextlayerid = nextlayerid
        self.nextobjectid = nextobjectid
        self.orientation = orientation
        self.renderorder = renderorder
        self.tiledversion = tiledversion
        self.tileheight = tileheight
        self.tilesets = tilesets
        self.tilewidth = tilewidth
        self.type = type
        self.version = version
        self.width = width
    
    @staticmethod
    def from_dict(obj):
        compressionlevel = from_int(obj.get("compressionlevel"))
        height = from_int(obj.get("height"))
        infinite = from_bool(obj.get("infinite"))
        layers = from_list(Layer.from_dict, obj.get("layers"))
        nextlayerid = from_int(obj.get("nextlayerid"))
        nextobjectid = from_int(obj.get("nextobjectid"))
        orientation = from_str(obj.get("orientation"))
        renderorder = from_str(obj.get("renderorder"))
        tiledversion = from_str(obj.get("tiledversion"))
        tileheight = from_int(obj.get("tileheight"))
        tilesets = from_list(Tileset.from_dict, obj.get("tilesets"))
        tilewidth = from_int(obj.get("tilewidth"))
        type = from_str(obj.get("type"))
        version = from_str(obj.get("version"))
        width = from_int(obj.get("width"))
        return TiledMap(compressionlevel, height, infinite, layers, nextlayerid, nextobjectid, orientation, renderorder, tiledversion, tileheight, tilesets, tilewidth, type, version, width)
    
    def to_dict(self):
        result = {}
        result["compressionlevel"] = from_int(self.compressionlevel)
        result["height"] = from_int(self.height)
        result["infinite"] = from_bool(self.infinite)
        result["layers"] = from_list(lambda x: to_class(Layer, x), self.layers)
        result["nextlayerid"] = from_int(self.nextlayerid)
        result["nextobjectid"] = from_int(self.nextobjectid)
        result["orientation"] = from_str(self.orientation)
        result["renderorder"] = from_str(self.renderorder)
        result["tiledversion"] = from_str(self.tiledversion)
        result["tileheight"] = from_int(self.tileheight)
        result["tilesets"] = from_list(lambda x: to_class(Tileset, x), self.tilesets)
        result["tilewidth"] = from_int(self.tilewidth)
        result["type"] = from_str(self.type)
        result["version"] = from_str(self.version)
        result["width"] = from_int(self.width)
        return result


def tiled_map_from_dict(s):
    return TiledMap.from_dict(s)


def tiled_map_to_dict(x):
    return to_class(TiledMap, x)
