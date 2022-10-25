from graphics import Rectangle, Point

from src.render import pause

class Player:
    def __init__(self, x, y, width, height, step_size, color, window):
        self.x = x
        self.y = y
        self.y_goal = y
        self.width = width
        self.height = height
        self.step_size = step_size
        self.color = color
        self.player = Rectangle(
            Point(x - (self.width/2), y - (self.height/2)),
            Point(x + (self.width/2), y + (self.height/2))
        )
        self.window = window

        self.player.setFill(self.color)
        self.player.draw(self.window)

    def move(self, gameData):
        new_y = (self.y + self.step_size if (self.y_goal > self.y) else self.y - self.step_size) if ((self.y_goal - self.y) > self.step_size or (self.y - self.y_goal) > self.step_size) else self.y
        key = self.window.checkKey()
        if key == "Up" and self.y_goal > 0:
            new_y -= self.step_size
            self.y_goal = self.y
        elif key == "Down" and self.y_goal < gameData["window"]["height"]:
            new_y += self.step_size
            self.y_goal = self.y
        elif key == "Escape":
            pause(self.window, gameData["window"]["width"]/2, gameData["window"]["height"]/2)

        self.player.move(0, gameData["player"]["y"] - self.player.getCenter().getY())

        gameData["player"]["y_goal"] = self.y_goal

        return new_y

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