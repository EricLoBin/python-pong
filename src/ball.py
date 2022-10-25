from graphics import Point, Circle
from random import random, randrange
import math

class Ball:
    def __init__(self, gameData):
        self.x = gameData["window"]["width"]/2
        self.y = gameData["window"]["height"]/2
        self.radius = gameData["ball"]["radius"]
        self.color = gameData["ball"]["color"]
        self.step = gameData["ball"]["step"]
        self.window = gameData["window"]["element"]

        while True:
            self.angle = int(random()*360)
            if (15 < self.angle < 165 or 195 < self.angle < 345):
                break
        self.ball = Circle(Point(self.x, self.y), self.radius)
        self.ball.setFill(self.color)
        self.ball.draw(self.window)

    def __reflectBall(self):
        newAngle = 0
        if (self.angle < 180):
            return (180 - self.angle)
        elif (self.angle > 180):
            return (540 - self.angle)
        else:
            return 320

    def __move(self):
        radians = 0.01745329 * (self.angle - 90) # PI/180 * angle
        newPosition = [
            int(self.step*math.cos(radians)),
            int(self.step*math.sin(radians))
        ]

        self.ball.move(
            newPosition[0],
            newPosition[1]
        )

        self.x += newPosition[0]
        self.y += newPosition[1]

    def tick(self, gameData):
        if (self.y-self.radius <= 0 or self.y+self.radius >= self.window.getHeight()):
            self.angle = self.__reflectBall()

        self.__move()

        # Left wall collision
        if (gameData["gamemode"] == "normal" and ("twoSides" not in gameData["powerup"]["active"])):
            if (self.x - self.radius < 0):
                self.x = self.radius
                self.angle = randrange(30, 150)
        
        # Delete ball
        if (self.x< 0 - self.radius or self.x > self.window.getWidth() + self.radius):
            self.ball.undraw()
            # TODO Delete ball from gameData["ball"]["balls"]
        
        # playerCollision
        if (self.x - self.radius <= gameData["player"]["x"] - (gameData["player"]["width"]/2) <= self.x + self.radius):
            if (gameData["player"]["y"] - (gameData["player"]["height"]/2) <= self.y <= gameData["player"]["y"] + (gameData["player"]["height"]/2)):
                self.angle = randrange(210, 330)
                self.x = self.ball.getCenter().x # Sync ball position

                # Update score
                gameData["score"] += 1 #! Redo score system
                gameData["textscore"].setText(f"Score: {gameData['score']}") #! Redo score system

                # Update Powerup Max Ammount #! not for every ball
                # if (gameData["score"] % 5 == 0):
                #     gameData["powerup"]["max"] += 2

        #TODO powerupCollision



# b = Ball({"window": {"width": 800, "height": 600, "element": None}, "ball": {"radius": 10, "color": "#ffffff"}})


# def createBall(gameData):
#     x, y = gameData["window"]["width"]/2, gameData["window"]["height"]/2
#     while True:
#         angle = int(random()*360)
#         if (15 < angle < 165 or 195 < angle < 345):
#             break

#     return {
#         "x": x,
#         "y": y,
#         "angle": angle,
#         "element": renderBall(x, y, gameData)
#     }

# def reflectBall(angle):
#     newAngle = 0
#     if (angle < 180):
#         return (180 - angle)
#     elif (angle > 180):
#         return (540 - angle)
#     else:
#         return 320


# def moveBall(x, y, angle, step, ball):
#     radians = 0.01745329 * (angle - 90) # PI/180 * angle
#     newPosition = [
#         int(step*math.cos(radians)),
#         int(step*math.sin(radians))
#     ]

#     ball.move(
#         newPosition[0],
#         newPosition[1]
#     )
#     return [
#         x + newPosition[0],
#         y + newPosition[1]
#     ]
