from Constants import *

class KeyMgr:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.vecKey = {key: {"state": KEY_TYPE.NONE, "prev": False} for key in KEY}
        return cls._instance

    def Init(self):     
        print("KeyMgr 초기화 완료")

    def Update(self):
        for key, info in self.vecKey.items():
            if info["state"] == KEY_TYPE.TAP:
                info["state"] = KEY_TYPE.HOLD
            elif info["state"] == KEY_TYPE.AWAY:
                info["state"] = KEY_TYPE.NONE


    def getKeyState(self, key):
        return self.vecKey[key]["state"]

    def keyboardDown(self, key):
        if key not in self.vecKey:
            self.vecKey[key] = {"state": KEY_TYPE.NONE, "prev": False}
        
        if not self.vecKey[key]["prev"]:
            self.vecKey[key]["state"] = KEY_TYPE.TAP
        else:
            self.vecKey[key]["state"] = KEY_TYPE.HOLD
        self.vecKey[key]["prev"] = True


    def keyboardUp(self, key):
        if self.vecKey[key]["prev"]:
            self.vecKey[key]["state"] = KEY_TYPE.AWAY
        self.vecKey[key]["prev"] = False
        
keyMgr = KeyMgr()