import pygame as pg
from random import randint


pg.init()
pg.init()
RES = WIDTH, HEIGHT = 64, 64
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2
FPS = 60
screen = pg.display.set_mode(RES)
clock = pg.time.Clock()
color = (255,0, 0)
while True:
    [exit() for i in pg.event.get() if i.type == pg.QUIT]
    color = (randint(0,255), randint(0,255), randint(0,255))
    # screen.fill(color)
    pg.draw.rect(screen, (0, 0, 255), [40, 30, 40, 10], 2)
    
    pg.display.update()

print("Done")