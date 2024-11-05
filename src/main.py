from pico2d import *
from CCore import CCore

def main():
    open_canvas()
    
    Core = CCore()
    Core.initialize()

    while Core.is_running():
        clear_canvas()
        Core.update()
        Core.draw()
        update_canvas()
        delay(0.01)

    Core.cleanup()
    close_canvas()

if __name__ == "__main__":
    main()
