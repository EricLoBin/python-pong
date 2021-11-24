# Import
from graphics import *
import time


# Import Files
from src.render import startMenu, renderPlayer, status, gameOver
from src.tick import tick
import src.ball as ball

# Main
def main():
    game()

def game():
    # Window size
    width, height = 800, 600

    # Game data
    gameData = {
        "tps": 60,# ticks/second
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

    gameData["player"]["element"] = renderPlayer(
        gameData["player"]["x"],
        gameData["player"]["y"],
        gameData)


    # gameData["ball"]["balls"].append(ball.createBall(gameData))
    gameData["ball"]["balls"].append(ball.createBall(gameData))


    while True:
        time.sleep(1/gameData["tps"])

        end = tick(gameData)

        # print(src.powerup.randomPowerup(gameData))

        if (window.isClosed() or end):
            break
    # GameOver
    gameOver(window, gameData["window"]["element"])
    window.getMouse()
    window.close()
    #
    game()

if (__name__ == "__main__"):
    main()