import math
import pygame as pg
from settings import *


class Ball(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pg.image.load('ball.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = (100, HEIGHT - 40)
        self.shoot = False
        self.bounds_check = True

    def update(self):
        pos = pg.mouse.get_pos()
        self.line = [(self.rect.midtop[0], self.rect.midtop[1]), pos]
        if not self.bounds_check:
            if self.rect.bottom >= HEIGHT - 40 and self.rect.left != 0 and self.rect.right != WIDTH:
                self.rect.bottom = HEIGHT - 40
                self.bounds_check = True
                self.shoot = False
                self.bounce_direction = 0
            else:
                self.wall_bounce()
        elif self.shoot:
            if self.rect.bottom - 1 < HEIGHT - 40:
                if not self.wall_check():
                    self.time += TIME_CHANGE
                    po = self.ballPath(self.startX, self.startY, self.power, self.angle, self.time)
                    self.rect.centerx = po[0]
                    self.rect.bottom = po[1]
            else:
                self.shoot = False
                self.rect.bottom = HEIGHT - 40
        elif not self.shoot and self.bounds_check:
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH - 1

    def new_shot(self):
        if not self.shoot:
            self.shoot = True
            self.time = 0
            self.power = math.sqrt(pow(self.line[1][1]-self.line[0][1], 2) +
                                   pow(self.line[1][0]-self.line[0][0], 2))/8
            self.angle = self.findAngle()
            self.startX = self.rect.centerx
            self.startY = self.rect.bottom

    def wall_check(self):
        if self.rect.left <= 0:
            self.bounce_direction = 1
            self.bounds_check = False
            self.reset_var_bounce(290, self.rect.left)
            return True
        elif self.rect.right >= WIDTH:
            self.bounce_direction = -1
            self.bounds_check = False
            self.reset_var_bounce(250, self.rect.right)
            return True
        return False

    def reset_var_bounce(self, degrees, startX):
        self.time = 0
        self.power /= 2
        self.angle = math.radians(degrees)
        self.startX = startX
        self.startY = self.rect.bottom

    def wall_bounce(self):
        # self.game.clock.tick(1000)
        if self.bounce_direction == 1:
            self.time += TIME_CHANGE
            po = self.ballPath(self.startX, self.startY, self.power, self.angle, self.time)
            self.rect.left = po[0]
            self.rect.bottom = po[1]
        elif self.bounce_direction == -1:
            self.time += TIME_CHANGE
            po = self.ballPath(self.startX, self.startY, self.power, self.angle, self.time)
            self.rect.right = po[0]
            self.rect.bottom = po[1]

    def findAngle(self):
        delta_x = self.line[1][0] - self.line[0][0]
        delta_y = self.line[0][1] - self.line[1][1]
        return math.atan2(delta_y, delta_x)

    @staticmethod
    def ballPath(startx, starty, power, angle, time):
        velx = math.cos(angle) * power
        vely = math.sin(angle) * power

        distX = velx * time
        distY = (vely * time) + ((-GRAVITY * pow(time, 2))/2)

        newX = round(distX + startx)
        newY = round(starty - distY)
        return (newX, newY)
