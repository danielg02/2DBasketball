import pygame as pg
from settings import *


pg.init()
pg.mixer.init()
pg.font.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
bkgrd = pg.image.load("Images/start_menu_bkgd.jpg").convert()
start = pg.image.load("Images/button_start.png")
settings = pg.image.load("Images/button_settings.png")

font = pg.font.Font('Fonts/212 Sports.otf', 75)
name_1 = font.render('Basketball', False, BLACK)
name_2 = font.render('Frenzy', False, BLACK)


def events(pos):
    if pos[0] in range(515, 515 + start.get_width()) and pos[1] in range(150, 150 + start.get_height()):
        return 1
    elif pos[0] in range(WIDTH - settings.get_width() - 10, WIDTH - 10) and pos[1] in range(10, 10 + settings.get_height()):
        return 2


def run():
    while True:
        screen.fill(WHITE)
        screen.blit(bkgrd, (0, 0))
        screen.blit(start, (515, 150))
        screen.blit(settings, (WIDTH - settings.get_width() - 10, 10))
        screen.blit(name_1, (40, 380))
        screen.blit(name_2, (40, 380 + name_2.get_height()))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.MOUSEBUTTONUP:
                choice = events(pg.mouse.get_pos())
                if choice == 1:
                    return
                elif choice == 2:
                    print("SETTINGS")
        pg.display.flip()
