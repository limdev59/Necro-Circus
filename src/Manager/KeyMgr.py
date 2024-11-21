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
        # 키가 없으면 KEY_TYPE.NONE 반환
        return self.vecKey.get(key, {"state": KEY_TYPE.NONE})["state"]

    def keyboardDown(self, key):
        # 키가 없으면 초기화
        if key not in self.vecKey:
            self.vecKey[key] = {"state": KEY_TYPE.NONE, "prev": False}
        
        if not self.vecKey[key]["prev"]:  # 처음 눌렸을 때 TAP으로 설정
            self.vecKey[key]["state"] = KEY_TYPE.TAP
            self.vecKey[key]["prev"] = True
        else:  # 이미 눌리고 있으면 HOLD 상태로 유지
            self.vecKey[key]["state"] = KEY_TYPE.HOLD

    def keyboardUp(self, key):
        # 키가 없으면 무시
        if key not in self.vecKey:
            return
        
        if self.vecKey[key]["prev"]:
            self.vecKey[key]["state"] = KEY_TYPE.AWAY
            self.vecKey[key]["prev"] = False
        else :
            self.vecKey[key]["state"] = KEY_TYPE.NONE

        
keyMgr = KeyMgr()