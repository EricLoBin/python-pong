from random import random
import math

# Import Files
from src.render import renderBall

def createBall(gameData):
    x, y = gameData["window"]["width"]/2, gameData["window"]["height"]/2
    while True:
        angle = int(random()*360)
        if (15 < angle < 165 or 195 < angle < 345):
            break

    return {
        "x": x,
        "y": y,
        "angle": angle,
        "element": renderBall(x, y, gameData)
    }

def reflectBall(angle):
    newAngle = 0
    if (angle < 180):
        return (180 - angle)
    elif (angle > 180):
        return (540 - angle)
    else:
        return 320


def moveBall(x, y, angle, step, ball):
    radians = 0.01745329 * (angle - 90) # PI/180 * angle
    newPosition = [
        int(step*math.cos(radians)),
        int(step*math.sin(radians))
    ]

    ball.move(
        newPosition[0],
        newPosition[1]
    )
    return [
        x + newPosition[0],
        y + newPosition[1]
    ]
