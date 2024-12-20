from pico2d import *
from CCore import Core

def main():
    open_canvas(w=1920, h=1080,sync=True,full=False)
    Core.Init()

    while Core.is_running():
        clear_canvas()
        Core.Update()
        Core.Render()
        update_canvas()
        delay(0.013)

    Core.Clean()
    close_canvas()



if __name__ == "__main__":
    main()
