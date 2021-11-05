import math

def reflectBall(angle):
    newAngle = 0
    if (angle < 180):
        return (180 - angle)
    else:
        return (540 - angle)


def moveBall(x, y, angle, step):
    radians = 0.01745329 * (angle - 90) # PI/180 * angle
    return [
        x + step*math.cos(radians),
        y + step*math.sin(radians)
    ]
