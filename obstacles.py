import pygame as pg
from settings import *


class Obstacle(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pg.Surface((50, 300))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.left = int(WIDTH * (3/4))
        self.rect.bottom = HEIGHT - GROUND_HEIGHT

    def change(self, height):
        self.image = pg.Surface((50, height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.left = int(WIDTH * (3/4))
        self.rect.bottom = HEIGHT - GROUND_HEIGHT
