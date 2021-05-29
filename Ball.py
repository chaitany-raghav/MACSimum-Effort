import Config
import pygame as pg
import math
import random

class Ball:
    def __init__(self,x,y,r,s,colour):
        self.x=x
        self.y=y
        self.s=s
        temp=random.randint(0,10)
        self.vx=s*math.cos(temp)
        self.vy=s*math.sin(temp)
        self.radius=r
        self.circle=(x,y)
        self.colour=colour
    
    def draw(self,win):
        pg.draw.circle(win,self.colour,self.circle,self.radius)
    
    def update(self):
        self.circle=(self.x,self.y)

    def move(self,players):
        self.checkCollision(players)
        self.x+=self.vx
        self.y+=self.vy

        self.update()
    
    def reset(self):
        self.x=Config.WindowWidth/2
        self.y=Config.WindowHeight/2
        temp=random.randint(0,10)
        self.vx=self.s*math.cos(temp)
        self.vy=self.s*math.sin(temp)

    def checkCollision(self,players):

        d=self.x-Config.PlayerOffSet-self.radius
        if d<0:#collision with left wall
            if players[0].isActive:#player for the left wall is active
                range=(players[0].y,players[0].y+Config.PlayerLength)
                if self.y<range[0] or self.y>range[1]:#the ball has been missed
                    self.reset()
                else: #the ball was hit
                    self.vx=-1*self.vx
            else:#just act as a wall
                self.vx=-1*self.vx

        d=self.y-Config.PlayerOffSet-self.radius
        if d<0:#collision with top wall
            if players[2].isActive:
                range=(players[2].x,players[2].x+Config.PlayerLength)
                if self.x<range[0] or self.x>range[1]:
                    self.reset()
                else:
                    self.vy=-1*self.vy
            else:
                self.vy=-1*self.vy

        d=Config.WindowWidth-Config.PlayerOffSet-self.x-self.radius
        if d<0:#collision with right wall
            if players[1].isActive:
                range=(players[1].y,players[1].y+Config.PlayerLength)
                if self.y<range[0] or self.y>range[1]:
                    self.reset()
                else: 
                    self.vx=-1*self.vx
            else:
                self.vx=-1*self.vx


        d=Config.WindowHeight-Config.PlayerOffSet-self.y-self.radius
        if d<0:#collision with bottom wall
            if players[3].isActive:
                range=(players[3].x,players[3].x+Config.PlayerLength)
                if self.x<range[0] or self.x>range[1]:
                    self.reset()
                else:
                    self.vy=-1*self.vy
            else:
                self.vy=-1*self.vy
        