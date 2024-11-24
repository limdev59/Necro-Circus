from Manager.EventMgr import eventMgr
from Manager.KeyMgr import keyMgr
from Manager.SceneMgr import sceneMgr

class CCore:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._running = True
            cls._instance.eventMgr = eventMgr
            cls._instance.sceneMgr = sceneMgr
            cls._instance.keyMgr = keyMgr
        return cls._instance

    def Init(self):
        print("Core 초기화")
        self.sceneMgr.Init()

    def Update(self):
        self.eventMgr.processEvents()
        self.sceneMgr.Update()
        self.keyMgr.Update()

    def Render(self):
        self.sceneMgr.Render()

    def Clean(self):
        print("Core 종료")
        self.sceneMgr.ChangeScene(None)
        self._running = False

    def is_running(self):
        return self._running

Core = CCore()