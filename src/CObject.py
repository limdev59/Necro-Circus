class CObject:
    def __init__(self, position=(0, 0), velocity=(0, 0)):
        self.position = list(position)
        self.velocity = list(velocity)
        self.active = True

    def Init(self):
        print(f"{self.__class__.__name__} 초기화")
        self.active = True

    def Update(self):
        if self.active:
            self.position[0] += self.velocity[0]
            self.position[1] += self.velocity[1]
            print(f"{self.__class__.__name__} 업데이트 - 위치: {self.position}")

    def Render(self):
        if self.active:
            print(f"{self.__class__.__name__} 렌더링 - 위치: {self.position}")

    def Clean(self):
        print(f"{self.__class__.__name__} 정리 중")
        self.active = False

    def SetPosition(self, x, y):
        self.position = [x, y]

    def SetVelocity(self, vx, vy):
        self.velocity = [vx, vy]

    def IsActive(self):
        return self.active
