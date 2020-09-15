import time
import random
import os
import math

from tkinter import *
from PIL import Image, ImageTk

import helper

class HCanvas(object):
    # General nessecities
    canvas = None
    root = None
    tkobjects = dict()
    scale = 2.8

    # Art Assets
    player = None
    indic = None
    background = None
    tksprites = dict()

    def __init__(self):
        self.root = Tk()
        self.root.title("2Hou")
        geo = str(int(self.scale*helper.clenx+5)) + 'x' + str(int(self.scale*helper.cleny+5))
        self.root.geometry(geo)
        self.root.configure(bg='white')
        self.canvas = Canvas(self.root, height=self.scale*(helper.cleny+5), width=self.scale*(helper.clenx+5), bg='black')
        # background image
        bg = Image.open('Assets/touhou6background.png')
        bg = bg.resize((int(self.scale*(helper.clenx+2)), int(self.scale*(helper.cleny+2))), Image.ANTIALIAS)
        self.tksprites['background'] = ImageTk.PhotoImage(bg)
        self.background = self.canvas.create_image(0,0, image=self.tksprites['background'], anchor=NW)
        self.canvas.tag_lower(self.background)


        self.canvas.bind("<1>", lambda event: self.canvas.focus_set())
        self.canvas.bind("<KeyPress>", self.move)
        self.canvas.bind("<KeyRelease>", self.stop)
        self.canvas.grid(row=0,column=0,rowspan=200)

        # players gotta exist
        self.tksprites['player'] = PhotoImage(file='Assets/arwing.png')
        self.player = self.canvas.create_image(self.scale*helper.player.x, self.scale*helper.player.y, image=self.tksprites['player'])
        self.indic = self.canvas.create_rectangle(self.scale*helper.player.x-2.5, self.scale*helper.player.y-20, self.scale*helper.player.x+2.5, self.scale*helper.player.y-15)

    def move(self, event):
        if event.char == 'a':
            helper.player.movew()
        elif event.char == 'd':
            helper.player.movee()
        elif event.char == 'w':
            helper.player.moven()
        elif event.char == 's':
            helper.player.moves()
        elif event.char == 'i':
            helper.player.moveinc()
        elif event.keycode == 65:
            helper.player.shoot()
        elif event.char == 'j':
            helper.player.turnleft()
        elif event.char == 'l':
            helper.player.turnright()
        elif event.char == 'k':
            helper.player.align()
        elif event.char == 'o':
            helper.player.dropbomb()

    def stop(self, event):
        if event.keycode == 38: # w
            helper.player.stopw()
        elif event.keycode == 40: # d
            helper.player.stope()
        elif event.keycode == 25: # s
            helper.player.stopn()
        elif event.keycode == 39: # a
            helper.player.stops()
        elif event.keycode == 31: # i
            helper.player.stopinc()
        elif event.keycode == 65:
            helper.player.stopshoot()
        elif event.keycode == 44:
            helper.player.stopturnl()
        elif event.keycode == 46:
            helper.player.stopturnr()

    def step(self):
        # objects
        objects = helper.enemybullets + helper.playerbullets + helper.enemies
        for object in objects:
            if object in self.tkobjects.keys():
                coords = self.canvas.coords(self.tkobjects[object])
                coorddiffx = self.scale*object.x - coords[0]
                coorddiffy = self.scale*object.y - coords[1]
                self.canvas.move(self.tkobjects[object], coorddiffx, coorddiffy)
            else:
                colour = object.colour
                self.tkobjects[object] = self.canvas.create_oval(self.scale*object.x, self.scale*object.y, self.scale*(object.x + object.lx), self.scale*(object.y+object.ly), fill=colour, outline=colour)
        for object in list(set(self.tkobjects.keys()) - set(helper.enemybullets) - set(helper.playerbullets) - set(helper.enemies)):
            self.canvas.delete(self.tkobjects[object])
            self.tkobjects.pop(object)

        # players special or somethin
        coords = self.canvas.coords(self.player)
        coorddiffx = self.scale*helper.player.x - coords[0]
        coorddiffy = self.scale*helper.player.y - coords[1]
        self.canvas.move(self.player, coorddiffx, coorddiffy)
        self.canvas.delete(self.indic)
        xang = -20*math.cos(helper.player.angle)
        yang = -20*math.sin(helper.player.angle)
        self.indic = self.canvas.create_rectangle(self.scale*helper.player.x+xang-2.5, self.scale*helper.player.y+yang, self.scale*helper.player.x+xang+2.5, self.scale*helper.player.y+yang+5, fill='blue', outline='blue')
        self.canvas.tag_raise(self.player)

        self.root.update()
        #self.root.after(100, self.step)
        helper.progressflag = False
