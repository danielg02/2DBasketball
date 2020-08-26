import pygame as pg
import pygame_menu as pg_menu

# DISPLAY SETTINGS
TITLE = "Basketball Frenzy"
WIDTH = 800
HEIGHT = 600

# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

GRAVITY = 5.5
GROUND_HEIGHT = 37
TIME_CHANGE = 0.09
LINE_COLOUR = RED
TIME_LIMIT = 120
# VALUES = []
#
# for i in range(1, 101):
#     VALUES.append((str(i), i))
#
#
# class Settings:
#     def __init__(self, screen):
#         self.screen = screen
#
#         # GAMEPLAY SETTINGS
#         self.time_change = 0.02
#         self.gravity = 5.5
#         self.line_colour = RED
#
#         # SETTINGS MENU FEATURES
#         self.menu = pg_menu.Menu(600, 800, 'Settings',
#                                  theme=pg_menu.themes.THEME_ORANGE, onclose=pg_menu.events.CLOSE)
#         self.menu.add_text_input('NAME: ', default='ENTER HERE', maxchar=20)
#         self.menu.add_selector('AIM LINE: ', [('RED', 1), ('GREEN', 2),
#                                               ('BLUE', 3), ('YELLOW', 4),
#                                               ('WHITE', 5), ('BLACK', 6)],
#                                onchange=self.set_line_colour)
#         self.menu.add_selector('GAME SPEED: ', VALUES,
#                                default=int(self.time_change*100-1),
#                                onchange=self.set_speed)
#         self.menu.add_selector('GRAVITY: ', VALUES,
#                                default=int(self.gravity*10-1),
#                                onchange=self.set_gravity)
#         self.menu.add_button('CLOSE', pg_menu.events.CLOSE)
#
#     def show(self):
#         self.menu.mainloop(self.screen)
#
#     def set_line_colour(self, selection, index):
#         if selection[0] == 'WHITE':
#             self.line_colour = WHITE
#         elif selection[0] == 'BLACK':
#             self.line_colour = BLACK
#         elif selection[0] == 'RED':
#             self.line_colour = RED
#         elif selection[0] == 'GREEN':
#             self.line_colour = GREEN
#         elif selection[0] == 'BLUE':
#             self.line_colour = BLUE
#         elif selection[0] == 'YELLOW':
#             self.line_colour = YELLOW
#
#     def set_gravity(self, selection, index):
#         self.gravity = float(selection[0]) / 10
#
#     def set_speed(self, selection, index):
#         self.time_change = float(selection[0]) / 100
