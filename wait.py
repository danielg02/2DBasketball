import pygame as pg
from settings import *

pg.init()
pg.mixer.init()
pg.font.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))

font = pg.font.Font('Fonts/212 Sports.otf', 40)
waiting = font.render('Waiting For Opponent', False, BLACK)
found = font.render('Opponent Found', False, BLACK)


class Wait:
    def __init__(self):
        pass

    def run(self):
        screen.fill(WHITE)
        screen.blit(waiting, (WIDTH/2-(waiting.get_width()/2), HEIGHT/2-waiting.get_height()))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        pg.display.flip()
