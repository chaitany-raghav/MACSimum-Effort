import pygame as pg
from pygame.constants import K_UP

width = 800
height = 600

win = pg.display.set_mode((width,height))
pg.display.set_caption("Client")

FPS=60

clientNumber = 0

class Player():
    def __init__(self,x,y,width,height,colour):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.colour=colour
        self.rect=(x,y,width,height)
        self.vel=3

    def draw(self,win):
        pg.draw.rect(win,self.colour,self.rect)

    def move(self):
        keys=pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.x-=self.vel

        if keys[pg.K_RIGHT]:
            self.x+=self.vel

        if keys[pg.K_UP]:
            self.y-=self.vel

        if keys[pg.K_DOWN]:
            self.y+=self.vel

        self.rect=(self.x,self.y,self.width,self.height)


def redrawWindow(win,player):

    win.fill((255,255,255))
    player.draw(win)
    pg.display.update()


def main():
    run=True
    p=Player(50,50,100,100,(0,0,255))
    clock=pg.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type ==pg.QUIT:
                run =False
                pg.quit()
        
        p.move()
        redrawWindow(win,p)

main()