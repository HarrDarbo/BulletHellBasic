import helper
import random

from bullet import Bullet

class Enemy(object):
    x = 0
    y = 0
    dx = 2
    dy = 0

    lx = 20
    ly = 20

    health = 20

    colour = 'blue'

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def step(self):
        self.x += self.dx
        self.y += self.dy
        if self.x % 5 == 0:
            helper.makebullet(Bullet(self.x,self.y,random.random()*2 - random.random()*2,random.random()*-40, ddx=0, ddy=1, type='enemy'))
            #helper.makebullet(Bullet(self.x+self.lx/2,self.y+self.ly,random.random()-random.random(),5,type='enemy'))
        if self.x >= helper.clenx or self.x <= 0:
            self.dx *= -1
        self.checkhurt()

    def checkhurt(self):
        for bullet in helper.bullets:
            if bullet.type != 'enemy' and abs(bullet.x-self.x) <= self.lx and abs(bullet.y-self.y) <= self.ly:
                self.health -= bullet.damage
                helper.endbullet(bullet)
        if self.health < 0:
            helper.removeenemy(self)
