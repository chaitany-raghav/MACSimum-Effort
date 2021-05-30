import pygame as pg

import math
import random

import Config

pg.mixer.init()

#soundObj = pg.mixer.Sound('sounds\mixkit-retro-game-notification-212.wav')  ##will be representeb by 0
#soundObj2 = pg.mixer.Sound('sounds\mixkit-arcade-retro-game-over-213.wav')  ##eill be represented by 1

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
        self.lastTouch=-1
    
    def draw(self,win):
        pg.draw.circle(win,self.colour,self.circle,self.radius)
    
    def update(self):
        self.circle=(self.x,self.y)

    def move(self,players,score,music):
        self.checkCollision(players,score,music)
        self.x+=self.vx
        self.y+=self.vy

        self.update()
    
    def reset(self):
        self.x=Config.WindowWidth/2
        self.y=Config.WindowHeight/2
        temp=random.randint(0,10)
        self.vx=self.s*math.cos(temp)
        self.vy=self.s*math.sin(temp)
        self.lastTouch=-1

    def checkCollision(self,players,score,music):
        relaxation=5
        d=self.x-Config.PlayerOffSet-self.radius
        if d<0:#collision with left wall
            if players[0].isActive:#player for the left wall is active
                range=(players[0].y-relaxation,players[0].y+Config.PlayerLength+relaxation)
                if self.y<range[0] or self.y>range[1]:#the ball has been missed
                    if players[self.lastTouch]:
                        if not self.lastTouch==-1:
                            score[self.lastTouch]+=1
                    score[0]-=1
                    music.append(1)
                    #soundObj2.play()
                    self.reset()
                else: #the ball was hit
                    self.lastTouch=0
                    score[0]+=1
                    self.vx=-1*self.vx
                    music.append(0)
                    #soundObj.play()
            else:#just act as a wall
                self.vx=-1*self.vx

        d=self.y-Config.PlayerOffSet-self.radius
        if d<0:#collision with top wall
            if players[2].isActive:
                range=(players[2].x-relaxation,players[2].x+Config.PlayerLength+relaxation)
                if self.x<range[0] or self.x>range[1]:
                    if players[self.lastTouch]:
                        if not self.lastTouch==-1:
                            score[self.lastTouch]+=1
                    score[2]-=1
                    music.append(1)
                    #soundObj2.play()
                    self.reset()
                else:
                    self.lastTouch=2
                    score[2]+=1
                    self.vy=-1*self.vy
                    music.append(0)
                    #soundObj.play()
            else:
                self.vy=-1*self.vy

        d=Config.WindowWidth-Config.PlayerOffSet-self.x-self.radius
        if d<0:#collision with right wall
            if players[1].isActive:
                range=(players[1].y-relaxation,players[1].y+Config.PlayerLength+relaxation)
                if self.y<range[0] or self.y>range[1]:
                    if players[self.lastTouch]:
                        if not self.lastTouch==-1:
                            score[self.lastTouch]+=1
                    score[1]-=1
                    music.append(1)
                    #soundObj2.play()
                    self.reset()
                else: 
                    score[1]+=1
                    self.lastTouch=1
                    self.vx=-1*self.vx
                    music.append(0)
                    #soundObj.play()
            else:
                self.vx=-1*self.vx


        d=Config.WindowHeight-Config.PlayerOffSet-self.y-self.radius
        if d<0:#collision with bottom wall
            if players[3].isActive:
                range=(players[3].x-relaxation,players[3].x+Config.PlayerLength+relaxation)
                if self.x<range[0] or self.x>range[1]:
                    if players[self.lastTouch]:
                        if not self.lastTouch==-1:
                            score[self.lastTouch]+=1
                    score[3]-=1
                    music.append(1)
                    #soundObj2.play()
                    self.reset()
                else:
                    score[3]+=1
                    self.lastTouch=3
                    self.vy=-1*self.vy
                    music.append(0)
                    #soundObj.play()
            else:
                self.vy=-1*self.vy
        