from pico2d import *
from Manager.KeyMgr import keyMgr, KEY, KEY_TYPE
from Constants import *

class Event:
    def __init__(self, event_type, data=None):
        self.type = event_type
        self.data = data

class EventMgr:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.event_queue = []
        return cls._instance

    def addEvent(self, event):
        print(f"이벤트 추가: {event.type}, 데이터: {event.data}")
        self.event_queue.append(event)

    def getEvents(self):
        events = get_events()
        for e in events:
            if e.type == SDL_KEYDOWN:
                keyMgr.keyboardDown(e.key)
                self.addEvent(Event(EVENT_TYPE.KEYBOARD, e.key))
            elif e.type == SDL_KEYUP:
                keyMgr.keyboardUp(e.key)
                self.addEvent(Event(EVENT_TYPE.KEYBOARD, e.key))
            elif e.type == SDL_MOUSEMOTION or e.type == SDL_MOUSEBUTTONDOWN or e.type == SDL_MOUSEBUTTONUP:
                event_type = EVENT_TYPE.MOUSE
                event_data = (e.x, e.y)
                self.addEvent(Event(event_type, event_data))

    def processEvents(self):
        self.getEvents()
        while self.event_queue:
            event = self.event_queue.pop(0)
            self.handleEvent(event)

    def handleEvent(self, event):
        if event.type == EVENT_TYPE.KEYBOARD:
            self.handleKeyboardEvent(event)
        elif event.type == EVENT_TYPE.MOUSE:
            self.handleMouseEvent(event)

    def handleKeyboardEvent(self, event):
        key = event.data
        key_state = keyMgr.getKeyState(key)
        print(f"키보드 이벤트: {key} 상태: {key_state}")

    def handleMouseEvent(self, event):
        print(f"마우스 이벤트: {event.data}")

eventMgr = EventMgr()
