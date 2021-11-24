# Import
from graphics import *
import time


# Import Files
from src.render import startMenu, renderPlayer, status
from src.tick import tick
import src.ball as ball
from src.player import movePlayer
import src.powerup

# Main
def main():

    # Window size
    width, height = 800, 600

    # Game data
    gameData = {
        "tps": 30,# ticks/second
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
            "stepSize": 5
        },
        "ball": {
            "balls": [],
            "x": width/2,
            "y": height/2,
            "step": 5,
            "radius": 7,
            "color": "#ff0000"
        },
        "powerup": {
            "elements": [],
            "size": 8,
            "max": 2,
            "marginX": 70,
            "marginY": 25,
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

    player = renderPlayer(
        gameData["player"]["x"],
        gameData["player"]["y"],
        gameData)


    # gameData["ball"]["balls"].append(ball.createBall(gameData))
    gameData["ball"]["balls"].append(ball.createBall(gameData))


    while True:
        thisTick = tick(gameData)
        
        print(src.powerup.randomPowerup(gameData))
        
        time.sleep(1/gameData["tps"])

        movePlayer(gameData, thisTick, player)
        gameData["player"]["y"] = thisTick["player"]["y"]


        gameData["ball"] = thisTick["ball"]
        
        if (window.isClosed()):
            break
    
    window.getMouse()
    window.close()

if (__name__ == "__main__"):
    main()