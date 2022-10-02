import pygame
import random2

WINDOW = 1000
TILE_SIZE = 50
RANGE =(TILE_SIZE // 2, WINDOW - TILE_SIZE //2, TILE_SIZE)
get_random_position = Lambda: [randrange(*RANGE), randrange(*RANGE)]
snake = pg.Rect([0,0, TILE_SIZE -2], TILE_SIZE -2] )
screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    screen.fill('black')
    #draw snakey
    pg.display.flip()
    clock.tick (60)







