from graphics import Point, Circle
from random import random, randrange
import math

class Ball:
    def __init__(self, window):
        self.x = window.width/2
        self.y = window.height/2
        self.radius = 7
        self.color = "#ff0000"
        self.step = 4
        self.window = window.window
        self.previous_move = (0, [0, 0]) # (angle, [x, y]) save last move to avoid recalculation

        while True:
            self.angle = int(random()*360)
            if (15 < self.angle < 165 or 195 < self.angle < 345):
                break
        self.ball = Circle(Point(self.x, self.y), self.radius)
        self.ball.setFill(self.color)
        self.ball.draw(self.window)

    def __reflectBall(self):
        if (self.angle < 180):
            return (180 - self.angle)
        elif (self.angle > 180):
            return (540 - self.angle)
        else:
            return 320

    def __move(self):
        if (self.previous_move[0] == self.angle):
            new_position = self.previous_move[1]
        else:
            radians = 0.01745329 * (self.angle - 90) # PI/180 * angle
            new_position = [
                int(self.step*math.cos(radians)),
                int(self.step*math.sin(radians))
            ]

        self.ball.move(
            new_position[0],
            new_position[1]
        )

        self.x += new_position[0]
        self.y += new_position[1]

    def resize(self, radius):
        self.radius = radius
        self.ball.undraw()
        self.ball = Circle(Point(self.x, self.y), self.radius)
        self.ball.setFill(self.color)
        self.ball.draw(self.window)

    def tick(self, game):
        if (self.y-self.radius <= 0 or self.y+self.radius >= self.window.getHeight()):
            self.angle = self.__reflectBall()

        self.__move()

        # Left wall collision
        # if (gameData["gamemode"] == "normal" and ("twoSides" not in gameData["powerup"]["active"])):
        if (True):
            if (self.x - self.radius < 0):
                self.x = self.radius
                self.angle = randrange(30, 150)
        
        # Delete ball
        if (self.x < 0 - self.radius or self.x > self.window.getWidth() + self.radius):
            self.ball.undraw()
            game.balls.remove(self)

            # Update score
            game.score -= 1
            game.window.textscore.setText(f"Score: {game.score}")

            if (len(game.balls) == 0):
                if (game.lives > 0):
                    # Remove life and respawn ball
                    game.lives -= 1
                    game.window.textlife.setText(f"Vidas restantes: {game.lives}")
                    game.balls.append(Ball(game.window))
                else:
                    # Game over
                    game.window.game_over()
            return

        # playerCollision
        player_position = game.player.get_position()
        if (self.x - self.radius <= player_position["x"] - (game.player.width/2) <= self.x + self.radius):
            if (player_position["y"] - (game.player.height/2) <= self.y <= player_position["y"] + (game.player.height/2)):
                self.angle = randrange(210, 330)
                self.x = self.ball.getCenter().x # Sync ball position

                # Update score
                game.score += 1
                game.window.textscore.setText(f"Score: {game.score}")

                # Update Powerup Max Ammount
                if (game.score % 5 == 0):
                    game.max_powerups += 1

        # powerup and ball collision
        x, y = (self.x - self.radius), (self.y - self.radius)
        for powerup in game.powerups:
            if (
                (
                    powerup.x < x
                    and
                    powerup.x + powerup.size > x
                ) or (
                    powerup.x < x + self.radius * 2
                    and
                    powerup.x + powerup.size > x + self.radius * 2
                )
            ):
                if (
                    (
                        powerup.y < y
                        and
                        powerup.y + powerup.size > y
                    ) or (
                        powerup.y < y + self.radius * 2
                        and
                        powerup.y + powerup.size > y + self.radius * 2
                    )
                ):
                    powerup.activate_powerup(game)

