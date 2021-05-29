import pygame as pg
import Config

class Player():
    def __init__(self,x,y,width,height,i,a,colour):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.colour=colour
        self.rect=(x,y,width,height)
        self.id=i
        self.isActive=a
        self.vel=Config.PlayerSpeed


    def draw(self,win):
        pg.draw.rect(win,self.colour,self.rect)

    def move(self):
        keys=pg.key.get_pressed()

        if self.height>self.width:
            if keys[pg.K_UP]:
                self.y-=self.vel

            if keys[pg.K_DOWN]:
                self.y+=self.vel
        else:
            if keys[pg.K_LEFT]:
                self.x-=self.vel

            if keys[pg.K_RIGHT]:
                self.x+=self.vel

        
        self.update()

    def update(self):
        self.rect=(self.x,self.y,self.width,self.height)
