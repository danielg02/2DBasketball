import math
import pygame as pg
from settings import *
from random import randrange

class Net(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pg.image.load('Images/net.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH
        self.rect.bottom = randrange(HEIGHT - 345, HEIGHT - GROUND_HEIGHT - 30)
        self.center_hoop = self.rect.right - 55

    def change(self):
        self.rect.bottom = randrange(HEIGHT - 345, HEIGHT - GROUND_HEIGHT - 30)
        return HEIGHT - self.rect.top - GROUND_HEIGHT