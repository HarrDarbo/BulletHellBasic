import random

from bullet import Bullet
from enemy import Enemy
from player import Player

def init():
    global canvas
    canvas = None
    global clenx
    clenx = 600
    global cleny
    cleny = 700

    global bullets
    bullets = list()
    global enemies
    enemies = list()
    global player
    player = Player(clenx/2,cleny/2)

def makeenemy(enemy):
    enemies.append(enemy)

def makenewenemy():
    enemies.append(Enemy(clenx/2, 50))

def removeenemy(enemy):
    enemies.remove(enemy)
    del enemy

def makebullet(blt):
    bullets.append(blt)

def maketestbullet():
    bullets.append(Bullet(clenx/2,100,random.random()*5 - random.random()*5,random.random()*-50, ddx=0, ddy=1))

def endbullet(blt):
    bullets.remove(blt)
    del blt

def allstep():
    for bullet in bullets:
        bullet.step()
    for enemy in enemies:
        enemy.step()
    player.step()
