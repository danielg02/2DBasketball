import pygame as pg
from sprites import *
from settings import *

# TODO:
# 1. Rotate ball depending on the situation
# 2. Add Net and Collision with new_shot
# 3. Start and Over Screens
# 4. Settings Screen


class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.bkgrd = pg.image.load("bkgd.jpg").convert()
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new_game(self):
        self.all_sprites = pg.sprite.Group()
        self.ball = Ball(game)
        self.all_sprites.add(self.ball)
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

    def draw(self):
        self.screen.fill(WHITE)
        self.screen.blit(self.bkgrd, (0, 0))
        self.all_sprites.draw(self.screen)
        pg.draw.line(self.screen, WHITE, self.ball.line[0], self.ball.line[1])
        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_over_screen(self):
        pass


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
