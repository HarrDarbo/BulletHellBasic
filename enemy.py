import helper
import random

from bullet import Bullet

class Enemy(object):
    x = 0
    y = 0
    dx = 2
    dy = 0

    bdx = 0
    bdy = 0

    lx = 10
    ly = 10

    shootctr = 0
    shoottimer = 5

    health = 100

    colour = 'blue'

    def __init__(self,x,y,dx=None,dy=None,bdx=None,bdy=None):
        self.x = x
        self.y = y
        if dx:
            self.dx = dx
        if dy:
            self.dy = dy
        if bdx:
            self.bdx = bdx
        if bdy:
            self.bdy = bdy

    def step(self):
        self.x += self.dx
        self.y += self.dy
        self.shootctr += 1
        if self.shootctr % self.shoottimer == 0:
            self.shootctr = 0
            helper.makebullet(Bullet(self.x,self.y,self.bdx,self.bdy, type='enemy'))
            #helper.makebullet(Bullet(self.x,self.y,random.random()*2 - random.random()*2,random.random()*-40, ddx=0, ddy=1, type='enemy'))
            #helper.makebullet(Bullet(self.x+self.lx/2,self.y+self.ly,random.random()-random.random(),5,type='enemy'))
        if self.x >= helper.clenx or self.x <= 0:
            self.dx *= -1
        if self.y >= helper.cleny or self.y <= 0:
            self.dy *= -1
        self.checkhurt()

    def checkhurt(self):
        for bullet in helper.playerbullets:
            if bullet.type != 'enemy' and abs(bullet.x-self.x) <= self.lx and abs(bullet.y-self.y) <= self.ly:
                self.health -= bullet.damage
                helper.endbullet(bullet)
        if self.health < 0:
            helper.removeenemy(self)
