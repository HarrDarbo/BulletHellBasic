import helper

class Bullet(object):
    x = 0
    y = 0
    dx = 1
    dy = 1
    ddx = 0
    ddy = 0

    lx = 3
    ly = 3
    colour = 'white'

    damage = 1
    type = 'none'

    def __init__(self,x,y,dx,dy,ddx=None,ddy=None,lx=None,ly=None,type=None):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        if ddx:
            self.ddx = ddx
        if ddy:
            self.ddy = ddy
        if lx:
            self.lx = lx
        if ly:
            self.ly = ly
        if type:
            self.type = type

    def step(self):
        self.x += self.dx
        self.y += self.dy
        self.dx += self.ddx
        self.dy += self.ddy
        if self.x > 1.25*helper.clenx or self.x < -0.25*helper.clenx:
            helper.endbullet(self)
        elif self.y > 1.25*helper.cleny or self.y < -0.25*helper.cleny:
            helper.endbullet(self)
