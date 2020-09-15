import time
import threading

import helper as glb
from bullet import Bullet
from canvas import *


def canvasrate():
    glb.canvas = HCanvas()


def start():
    glb.canvas = HCanvas()

    glb.makenewenemy()

    stepr = 0
    time.sleep(0.2)
    frametarget = 60
    framerate = 0
    frametimer = time.time()
    while True:
        stepr += 1
        threading.Thread(target=glb.allstep, daemon=True,).start()
        #glb.allstep()
        glb.canvas.step()

        st = time.time()

        if stepr%250 == 0:
            for i in range(2):
                helper.makenewenemy()

        while time.time()-st <= 1/frametarget:
            pass
        framerate += 1
        if time.time()-frametimer >= 1:
            print("FR: ", framerate)
            frametimer = time.time()
            framerate = 0


if __name__ == "__main__":
    print("\033[1;37;40mStarting Program...")
    glb.init()
    start()
