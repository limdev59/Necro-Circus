
class CCore:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.initialized = False
        return cls._instance

    def initialize(self):
        if not self.initialized:
            print("Core 초기화")
            self.running = True
            self.initialized = True

    def is_running(self):
        return self.running

    def update(self):
        pass

    def draw(self):
        pass

    def cleanup(self):
        print("Core 종료")
        self.running = False
