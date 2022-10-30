import time
from random import randint

from src.window import Window
from src.player import Player
from src.ball import Ball
from src.powerup import Powerup


class Game:
    def __init__(self):
        # Options
        self.tps = 80
        self.max_lives = 3

        # Game data
        self.score = 0
        self.lives = self.max_lives
        self.balls = []
        self.max_powerups = 2
        self.powerups = []

        # Window
        self.window = Window(self)
        self.window.start_menu()

        # Player
        self.player = Player(self.window.window)

    def tick(self):
        self.player.tick()
        for ball in self.balls:
            ball.tick(self)
        # powerup spawn
        if (len(self.powerups) < self.max_powerups):
            self.powerups.append(Powerup(self, randint(30, self.window.width - 60), randint(30, self.window.height - 30)))


def main():
    game = Game()

    # Ball
    game.balls.append(Ball(game.window))

    tps_wait_time = 1/game.tps
    while True:
        start = time.time() # Tick Start time

        # Tick
        game.tick()

        # Window is closed
        if (game.window.window.isClosed()):
            break

        # TPS
        wait = (tps_wait_time - (time.time() - start))
        if (wait > 0):
            time.sleep(wait)


if (__name__ == "__main__"):
    main()
