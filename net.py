import math
import pygame as pg
from settings import *


class Net(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pg.image.load('Images/net.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH
        self.rect.bottom = HEIGHT - 300
        self.center_hoop = self.rect.right - 55
