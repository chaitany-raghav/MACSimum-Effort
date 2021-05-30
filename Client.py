import pygame as pg

from _thread import *

from Network import Network
from Player import *
import Config
from Ball import Ball

width = Config.WindowWidth
height = Config.WindowHeight

pg.font.init()

win = pg.display.set_mode((width,height))
pg.display.set_caption("Client")
image = pg.image.load(r'images\bg.jpg')
#image = pg.transform.scale(pg.image.load(r'images\bg.jpg'), (width,height))
#soundObj = pg.mixer.Sound('sounds\mixkit-retro-game-notification-212.wav')
#soundObj2 = pg.mixer.Sound('sounds\mixkit-arcade-retro-game-over-213.wav')
sounds=[pg.mixer.Sound('sounds\mixkit-retro-game-notification-212.wav'),pg.mixer.Sound('sounds\mixkit-arcade-retro-game-over-213.wav')]

PlayerID=-1

font = pg.font.Font('font\Creamy Coconut.ttf', 32)

def show_score(win,score_value,x, y):
    if x==100 and y==500:
        score = font.render("Score : " + str(score_value), True, (255, 0, 0))
    if x==300 and y==500:
        score = font.render("Score : " + str(score_value), True, (0, 255, 0))
    if x==100 and y==550:
        score = font.render("Score : " + str(score_value), True, (0, 0, 250))
    if x==300 and y==550:
        score = font.render("Score : " + str(score_value), True, (128, 128, 0))
    win.blit(score, (x, y))

def redrawWindow(win,players,ball,scores):

    win.fill((255,255,255))
    win.blit(image, (0, 0))
    for p in players:
        if p.isActive:
            p.draw(win)
            if p.id==0:
                show_score(win,scores[p.id],100,500)
            if p.id==1:
                show_score(win,scores[p.id],300,500)
            if p.id==2:
                show_score(win,scores[p.id],100,550)
            if p.id==3:
                show_score(win,scores[p.id],300,550)
    
    ball.draw(win)
    pg.display.update()



def main():
    run=True
    n=Network()
    p=n.getP()
    global PlayerID
    PlayerID=p.id
    pg.display.set_caption("Player "+str(PlayerID+1))
    clock=pg.time.Clock()
    pg.mixer.music.load(r'sounds\mixkit-mystwrious-bass-pulse-2298.wav')
    pg.mixer.music.play(-1)
    while run:
        clock.tick(Config.FPS)
        data=n.send(p)
        for event in pg.event.get():
            if event.type ==pg.QUIT:
                run =False
                pg.quit()
        music=data[3]
        for m in music:
            sounds[m].play()
        #print(data)
        p.move()
        redrawWindow(win,data[0],data[1],data[2])

main()
