import pygame as pg
from random import randint


pg.init()
pg.init()
RES = WIDTH, HEIGHT = 640, 640
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2
FPS = 1
screen = pg.display.set_mode(RES)
clock = pg.time.Clock()
clock.tick(FPS)
color = (255,0, 0)
c = 0
ru = True
while ru:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            ru = False
    color = (randint(0,255), randint(0,255), randint(0,255))
    
    # pg.draw.rect(screen, (0, 0, 255), [randint(10,600), randint(0,600), 40, 10], 2)
    pg.draw.circle(screen, color, (randint(0,640), randint(0,640)), 1, 1)
    
    pg.display.update()
    if c > 100:
        screen.fill((0,0,0))
        c = 0
    c += 1

print("Done")