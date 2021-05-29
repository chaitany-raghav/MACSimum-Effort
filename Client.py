import pygame as pg
from Network import Network
from Player import *
import Config

width = Config.WindowWidth
height = Config.WindowHeight

win = pg.display.set_mode((width,height))
pg.display.set_caption("Client")


PlayerID=-1

def redrawWindow(win,players):

    win.fill((255,255,255))
    for p in players:
        p.draw(win)
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
        redrawWindow(win,data)

main()