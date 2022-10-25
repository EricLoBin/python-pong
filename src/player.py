from graphics import Rectangle, Point

from src.render import pause

class Player:
    def __init__(self, x, y, width, height, color, window):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.player = Rectangle(
            Point(x - (self.width/2), y - (self.height/2)),
            Point(x + (self.width/2), y + (self.height/2))
        )

        self.player.setFill(self.color)
        self.player.draw(window)

    def move(self, gameData):
        if (gameData["player"]["y"] > gameData["player"]["yGoal"]):
            gameData["player"]["y"] -= gameData["player"]["stepSize"]
        elif (gameData["player"]["y"] < gameData["player"]["yGoal"]):
            gameData["player"]["y"] += gameData["player"]["stepSize"]
        
        self.player.move(0, gameData["player"]["y"] - self.player.getCenter().getY())

def movePlayer(gameData):
    newY = (gameData["player"]["y"] + gameData["player"]["stepSize"] if (gameData["player"]["yGoal"] > gameData["player"]["y"]) else gameData["player"]["y"] - gameData["player"]["stepSize"]) if ((gameData["player"]["yGoal"] - gameData["player"]["y"]) > gameData["player"]["stepSize"] or (gameData["player"]["y"] - gameData["player"]["yGoal"]) > gameData["player"]["stepSize"]) else gameData["player"]["y"]

    key = gameData["window"]["element"].checkKey()
    if key == "Up" and gameData["player"]["yGoal"] > 0:
        newY -= gameData["player"]["stepSize"]
        gameData["player"]["yGoal"] = gameData["player"]["y"]
    elif key == "Down" and gameData["player"]["yGoal"] < gameData["window"]["height"]:
        newY += gameData["player"]["stepSize"]
        gameData["player"]["yGoal"] = gameData["player"]["y"]
    elif key == "Escape":
        pause(gameData["window"]["element"], gameData["window"]["width"]/2, gameData["window"]["height"]/2)

    gameData["player"]["element"].player.move(gameData["player"]["x"] - gameData["player"]["x"], newY - gameData["player"]["y"])

    return newY