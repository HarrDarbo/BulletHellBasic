import time

import helper as glb
from bullet import Bullet
from canvas import *

def start():
    glb.canvas = HCanvas()

    glb.makenewenemy()

    stepr = 0
    time.sleep(0.2)
    while True:
        stepr += 1
        glb.canvas.step()
        glb.allstep()

        #if stepr%250 == 0:


        time.sleep(0.016)


if __name__ == "__main__":
    print("\033[1;37;40mStarting Program...")
    glb.init()
    start()
