import pygame as pg
from ball import Ball
from net import Net
from settings import *
from start import Start
from obstacles import Obstacle
from network import Network
from wait import Wait

# TODO:
# Obstacle Collision
# Game Over Screen
# Reset game/server
# Wait for game


class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.bkgrd = pg.image.load("Images/bkgd.jpg").convert()
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.score1 = 0
        self.score2 = 0
        self.attempts = 0

    def new_game(self):
        self.all_sprites = pg.sprite.Group()
        self.net = Net(game)
        self.obstacle = Obstacle(game)
        self.ball = Ball(game)
        self.network = Network()
        self.all_sprites.add(self.ball, self.net, self.obstacle)
        self.start_ticks = pg.time.get_ticks()
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            elif event.type == pg.MOUSEBUTTONUP:
                self.ball.new_shot()
        self.score2 = str(self.network.send(str(self.score1)))

    def draw(self):
        font = pg.font.Font('Fonts/212 Sports.otf', 30)
        score1 = font.render('Score: {}'.format(self.score1), False, BLACK)
        score2 = font.render('Score: {}'.format(self.score2), False, BLACK)
        # attempts = font.render('Attempts: {}'.format(self.attempts), False, BLACK)
        total_seconds = TIME_LIMIT - int((pg.time.get_ticks() - self.start_ticks) / 1000)
        minutes = int(total_seconds / 60)
        seconds = total_seconds % 60
        if seconds < 10:
            time = font.render('{}:0{} Left'.format(minutes, seconds), False, BLACK)
        else:
            time = font.render('{}:{} Left'.format(minutes, seconds), False, BLACK)
        self.screen.fill(WHITE)
        self.screen.blit(self.bkgrd, (0, 0))
        self.screen.blit(score1, (5, 10))
        self.screen.blit(score2, (5, 40))
        self.screen.blit(time, (500, 10))
        self.all_sprites.draw(self.screen)
        pg.draw.line(self.screen, LINE_COLOUR,
                     self.ball.line[0], self.ball.line[1])
        pg.display.flip()

        if total_seconds <= 0:
            self.playing = False
            self.show_over_screen()
            self.show_start_screen()

    def show_start_screen(self):
        self.start = Start()
        self.start.run()
        # self.show_waiting()

    def show_over_screen(self):
        pass

    def show_waiting(self):
        self.wait = Wait()
        self.wait.run()


def main():
    global game
    game = Game()
    game.show_start_screen()
    while game.running:
        game.new_game()
        game.show_over_screen()
    pg.quit()


if __name__ == '__main__':
    main()
