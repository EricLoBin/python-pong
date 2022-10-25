# Import
from graphics import *
import time


# Import Files
from src.render import startMenu, status, gameOver
from src.tick import tick
from src.ball import Ball
from src.player import Player


class Game:
    def __init__(self):
        # Window
        self.windowWidth = 800
        self.windowHeight = 600
        self.window = GraphWin("Pong", self.windowWidth, self.windowHeight)
        self.window.setBackground("black")
        self.window.setCoords(0, 0, self.windowWidth, self.windowHeight)

        # Player
        # self.playerX = 10
        # self.playerY = self.windowHeight/2
        # self.playerYGoal = self.playerY
        # self.playerStepSize = 10
        # self.playerWidth = 10
        # self.playerHeight = 100

        # Ball
        self.balls = []

        self.gameData = {
            "window": {
                "element": self.window,
                "width": 800,
                "height": 600
            },
            "player": None,
            "ball": {
                "x": 400,
                "y": 300,
                "radius": 10,
                "color": "white",
                "step": 5,
                "angle": 0,
                "element": None
            },
            "gamemode": "normal",
            "powerup": {
                "active": [],
                "cooldown": 0
            }
        }

# Main
def main():
    game()

def game():
    # Window size
    width, height = 800, 600

    # Game data
    gameData = {
        "tps": 120,# ticks/second
        "window": {
            "title": "python-pong",
            "width": width,
            "height": height
        },
        "gamemode": "normal",
        "score": 0,
        "player": {
            "x": width - 40,
            "y": height/2,
            "width": 10,
            "height": 40,

            "lifes": 3,
            "yGoal": height/2,
            "stepSize": 4
        },
        "ball": {
            "balls": [],
            "x": width/2,
            "y": height/2,
            "step": 4,
            "radius": 7,
            "color": "#ff0000"
        },
        "powerup": {
            "elements": [],
            "size": 20,
            "max": 2,
            "spawnChance": 0.002, # 1 = 100%
            "duration": 600, #Ticks
            "marginX": 70,
            "marginY": 35,
            "active": {}
        } 
    }

    # Create window
    window = GraphWin(
        gameData["window"]["title"],
        gameData["window"]["width"],
        gameData["window"]["height"]
    )

    gameData["window"]["element"] = window


    # Start Menu
    startMenu(window, width, height)


    # Get mouse Y
    def motion(event):
        gameData["player"]["yGoal"] = event.y
    window.bind('<Motion>', motion)


    # Create Elements
    gameData["textlife"], gameData["textscore"] = status(gameData)

    gameData["player"]["element"] = Player(
        width - 40,
        height/2,
        10,
        40,
        "#ff0000",
        gameData["window"]["element"]
    )


    # gameData["ball"]["balls"].append(ball.createBall(gameData))
    gameData["ball"]["balls"].append(Ball(gameData))


    while True:
        time.sleep(1/gameData["tps"])

        end = tick(gameData)

        # print(src.powerup.randomPowerup(gameData))

        if (window.isClosed() or end):
            break
    # GameOver
    gameOver(gameData)
    #
    game()

if (__name__ == "__main__"):
    main()