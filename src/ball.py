def reflectBall(angle):
    newAngle = 0
    if (angle < 180):
        return (180 - angle)
    else:
        return (540 - angle)
