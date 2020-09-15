import random
import threading

from bullet import Bullet
from enemy import Enemy
from player import Player

def init():
    global canvas
    canvas = None
    global clenx
    clenx = 300
    global cleny
    cleny = 350

    global enemybullets
    enemybullets = list()
    global playerbullets
    playerbullets = list()
    global enemies
    enemies = list()
    global player
    player = Player(clenx/2,cleny/2)

    global progressflag
    progressflag = True

def makeenemy(enemy):
    enemies.append(enemy)

def makenewenemy():
    enemies.append(Enemy(random.random()*clenx, random.random()*cleny, random.random()*2-random.random()*2, random.random()*2-random.random()*2, random.random()*2-random.random()*2, random.random()*2-random.random()*2))

def removeenemy(enemy):
    enemies.remove(enemy)
    del enemy

def makebullet(blt):
    if blt.type == 'player':
        playerbullets.append(blt)
    else:
        enemybullets.append(blt)

def endbullet(blt):
    try:
        if blt.type == 'player':
            playerbullets.remove(blt)
        else:
            enemybullets.remove(blt)
    except ValueError:
        pass

def allstep():
    global progressflag
    progressflag = False
    multithread = True
    if multithread:
        threadnum = int(len(playerbullets)/10)+1
        if threadnum > 500:
            threadnum = 500
        threads = list()
        for x in range(threadnum):
            threads.append(threading.Thread(target=allstepthread, daemon=True, args=(x,threadnum,)))
            threads[x].start()
        for enemy in enemies:
            enemy.step()
        player.step()
    else:
        for bullet in playerbullets:
            bullet.step()
        for bullet in enemybullets:
            bullet.step()
        for enemy in enemies:
            enemy.step()
        player.step()
    progressflag = True

def allstepthread(indx,threadnum):
    for list in [playerbullets,enemybullets]:
        start = int((len(list)*indx)/threadnum)
        end = int((len(list)*(indx+1))/threadnum)
        for item in list[start:end]:
            item.step()
