import pygame as pg
from Network import Network
from Player import *
import Config
from Ball import Ball

width = Config.WindowWidth
height = Config.WindowHeight

win = pg.display.set_mode((width,height))
pg.display.set_caption("Client")


PlayerID=-1

def redrawWindow(win,players,ball):

    win.fill((255,255,255))
    for p in players:
        if p.isActive:
            p.draw(win)
    ball.draw(win)
    pg.display.update()


def main():
    run=True
    n=Network()
    p=n.getP()
    global PlayerID
    PlayerID=p.id
    clock=pg.time.Clock()
    while run:
        clock.tick(Config.FPS)
        data=n.send(p)
        for event in pg.event.get():
            if event.type ==pg.QUIT:
                run =False
                pg.quit()
        
        p.move()
        redrawWindow(win,data[0],data[1])

main()