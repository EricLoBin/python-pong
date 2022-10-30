from graphics import Rectangle, Point
from random import randint

from src.ball import Ball

# Powerup effects
def more_balls(game):
    game.balls.append(Ball(game.window))

def bigger_balls(game):
    for ball in game.balls:
        if (ball.radius > 14):
            continue
        ball.resize(ball.radius + 3)

def smaller_balls(game):
    for ball in game.balls:
        if (ball.radius < 5):
            continue
        ball.resize(ball.radius - 3)

def slower_balls(game):
    for ball in game.balls:
        if (ball.step < 3):
            continue
        ball.step -= 1

def faster_balls(game):
    for ball in game.balls:
        if (ball.step > 4):
            continue
        ball.step += 1

powerup_list = [
    more_balls,
    bigger_balls,
    smaller_balls,
    slower_balls,
    faster_balls
]

powerup_list_size = len(powerup_list)-1

# Powerup class
class Powerup:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.size = 20
        self.powerup = Rectangle(
            Point(x, y),
            Point((x + self.size), (y + self.size))
        )
        color = "#%06x" % randint(0, 0xFFFFFF) # random color
        self.powerup.setFill(color)
        self.powerup.draw(game.window.window)

    def activate_powerup(self, game):
        powerup_list[randint(0, powerup_list_size)](game)
        self.powerup.undraw()
        game.powerups.remove(self)
