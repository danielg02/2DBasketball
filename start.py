import pygame as pg
from settings import *

pg.init()
pg.mixer.init()
pg.font.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
bkgrd = pg.image.load("Images/start_menu_bkgd.jpg").convert()
multiplayer = pg.image.load("Images/button_multiplayer.png")

font = pg.font.Font('Fonts/212 Sports.otf', 75)
name_1 = font.render('Basketball', False, BLACK)
name_2 = font.render('Frenzy', False, BLACK)


class Start:
    def __init__(self):
        pass

    def events(self, pos):
        if pos[0] in range(515, 515 + multiplayer.get_width()) and pos[1] in range(150, 150 + multiplayer.get_height()):
            return 1

    def run(self):
        while True:
            screen.fill(WHITE)
            screen.blit(bkgrd, (0, 0))
            screen.blit(multiplayer, (515, 150))
            screen.blit(name_1, (40, HEIGHT - 40 - name_1.get_height() - name_1.get_height()))
            screen.blit(name_2, (40, HEIGHT - 40 - name_2.get_height()))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                elif event.type == pg.MOUSEBUTTONUP:
                    choice = self.events(pg.mouse.get_pos())
                    if choice == 1:
                        return

            pg.display.flip()
