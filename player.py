import random
import math

import helper
from bullet import Bullet

class Player(object):
    x = 0
    y = 0
    dx = 0
    dy = 0

    movespeed = 2
    turnspeed = 0.1

    N = False
    fN = 0
    S = False
    fS = 0
    E = False
    fE = 0
    W = False
    fW = 0

    # Radians
    angle = 0.5*math.pi
    Tr = False
    Tl = False

    shooting = False

    colour = 'green'
    lx = 3
    ly = 3

    advcontrol = False

    health = 100

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def step(self):
        self.dx = 0
        self.dy = 0

        self.move()

        # Wall checking
        if self.x < 0:
            self.dx -= self.x
            self.x = 0
        elif self.x > helper.clenx:
            self.dx -= (self.x-helper.clenx)
            self.x = helper.clenx
        if self.y < 0:
            self.dy -= self.y
            self.y = 0
        elif self.y > helper.cleny:
            self.dy -= (self.y-helper.cleny)
            self.y = helper.cleny

        self.checkhurt()
        if self.shooting:
            self.bullets()

    def move(self):
        if self.Tl:
            self.angle = (self.angle + self.turnspeed) % (2*math.pi)
        if self.Tr:
            self.angle = (self.angle - self.turnspeed) % (2*math.pi)
        if not self.advcontrol:
            if self.N:
                if self.fN < 10:
                    self.fN += 1
                    ymove = 0.1*self.fN*self.movespeed
                    self.y -= ymove
                    self.dy -= ymove
                else:
                    ymove = self.movespeed
                    self.y -= ymove
                    self.dy -= ymove
            else:
                self.fN = 0
            if self.S:
                if self.fS < 10:
                    self.fS += 1
                    ymove = 0.1*self.fS*self.movespeed
                    self.y += ymove
                    self.dy += ymove
                else:
                    ymove = self.movespeed
                    self.y += ymove
                    self.dy += ymove
            else:
                self.fS = 0
            if self.E:
                if self.fE < 10:
                    self.fE += 1
                    xmove = 0.1*self.fE*self.movespeed
                    self.x += xmove
                    self.dx += xmove
                else:
                    xmove = self.movespeed
                    self.x += xmove
                    self.dx += xmove
            else:
                self.fE = 0
            if self.W:
                if self.fW < 10:
                    self.fW += 1
                    xmove = 0.1*self.fW*self.movespeed
                    self.x -= xmove
                    self.dx -= xmove
                else:
                    xmove = self.movespeed
                    self.x -= xmove
                    self.dx -= xmove
            else:
                self.fW = 0
        else:
            if self.N:
                if self.fN < 10:
                    self.fN += 1
                    ymove = 0.1*self.fN*self.movespeed*math.sin(self.angle)
                    self.y -= ymove
                    self.dy -= ymove
                    xmove = 0.1*self.fN*self.movespeed*math.cos(self.angle)
                    self.x -= xmove
                    self.dx -= xmove
                else:
                    ymove = self.movespeed*math.sin(self.angle)
                    self.y -= ymove
                    self.dy -= ymove
                    xmove = self.movespeed*math.cos(self.angle)
                    self.x -= xmove
                    self.dx -= xmove
            else:
                self.fN = 0
            if self.S:
                if self.fS < 10:
                    self.fS += 1
                    ymove = 0.1*self.fS*self.movespeed*math.sin(self.angle)
                    self.y += ymove
                    self.dy += ymove
                    xmove = 0.1*self.fS*self.movespeed*math.cos(self.angle)
                    self.x += xmove
                    self.dx += xmove
                else:
                    ymove = self.movespeed*math.sin(self.angle)
                    self.y += ymove
                    self.dy += ymove
                    xmove = self.movespeed*math.cos(self.angle)
                    self.x += xmove
                    self.dx += xmove
            else:
                self.fS = 0
            if self.E:
                if self.fE < 10:
                    self.fE += 1
                    ymove = 0.1*self.fE*self.movespeed*math.sin(self.angle-0.5*math.pi)
                    self.y += ymove
                    self.dy += ymove
                    xmove = 0.1*self.fE*self.movespeed*math.cos(self.angle-0.5*math.pi)
                    self.x += xmove
                    self.dx += xmove
                else:
                    ymove = self.movespeed*math.sin(self.angle-0.5*math.pi)
                    self.y += ymove
                    self.dy += ymove
                    xmove = self.movespeed*math.cos(self.angle-0.5*math.pi)
                    self.x += xmove
                    self.dx += xmove
            else:
                self.fE = 0
            if self.W:
                if self.fW < 10:
                    self.fW += 1
                    ymove = 0.1*self.fW*self.movespeed*math.sin(self.angle-0.5*math.pi)
                    self.y -= ymove
                    self.dy -= ymove
                    xmove = 0.1*self.fW*self.movespeed*math.cos(self.angle-0.5*math.pi)
                    self.x -= xmove
                    self.dx -= xmove
                else:
                    ymove = self.movespeed*math.sin(self.angle-0.5*math.pi)
                    self.y -= ymove
                    self.dy -= ymove
                    xmove = self.movespeed*math.cos(self.angle-0.5*math.pi)
                    self.x -= xmove
                    self.dx -= xmove
            else:
                self.fW = 0

    def bomb(self):
        for x in range(3):
            x += 6
            for a in range(180):
                xchg = ((math.pi)/360)*a*4
                helper.makebullet(Bullet(self.x,self.y,-x/3*math.cos(self.angle+xchg),-x/3*math.sin(self.angle+xchg), type='player', damage=100))

    def bullets(self):
        for a in range(3):
            xchg = ((math.pi)/180)*a*2-0.1
            helper.makebullet(Bullet(self.x,self.y,-5*math.cos(self.angle+xchg),-5*math.sin(self.angle+xchg), type='player'))

    def checkhurt(self):
        for bullet in helper.enemybullets:
            if abs(bullet.x-self.x) <= self.lx and abs(bullet.y-self.y) <= self.ly:
                self.health -= bullet.damage
                helper.endbullet(bullet)

    def movew(self):
        self.W = True
    def stopw(self):
        self.W = False
    def movee(self):
        self.E = True
    def stope(self):
        self.E = False
    def moven(self):
        self.N = True
    def stopn(self):
        self.N = False
    def moves(self):
        self.S = True
    def stops(self):
        self.S = False
    def turnleft(self):
        self.Tr = True
    def stopturnl(self):
        self.Tr = False
    def turnright(self):
        self.Tl = True
    def stopturnr(self):
        self.Tl = False

    def moveinc(self):
        self.movespeed /= 2
        self.turnspeed /= 2
    def stopinc(self):
        self.movespeed *= 2
        self.turnspeed *= 2

    def shoot(self):
        self.shooting = True
    def stopshoot(self):
        self.shooting = False

    def align(self):
        self.angle = 0.5*math.pi

    def dropbomb(self):
        self.bomb()
