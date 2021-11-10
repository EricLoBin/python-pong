# Import
from graphics import *
import time


# Import Files
from src.render import startMenu
from src.tick import tick
import src.ball as ball



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
        "player": {
            "x": width - 40,
            "y": height/2,

            "lifes": 3,
            "yGoal": height/2,
            "stepSize": 5
        },
        "ball": {
            "balls": [],
            "x": width/2,
            "y": height/2,
            "step": 5,
            "radius": 5,
            "color": "#ff0000"
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
    player = Point(gameData["player"]["x"], gameData["player"]["y"])
    player.setFill("Red")
    player.draw(window)

    # gameData["ball"]["balls"].append(ball.createBall(gameData))
    gameData["ball"]["balls"].append(ball.createBall(gameData))


    while True:
        thisTick = tick(gameData)
        
        time.sleep(1/gameData["tps"])

        player.move(thisTick["player"]["x"]-gameData["player"]["x"], thisTick["player"]["y"]-gameData["player"]["y"])
        gameData["player"]["y"] = thisTick["player"]["y"]


        gameData["ball"] = thisTick["ball"]
        
        if (window.isClosed()):
            break
    
    window.getMouse()
    window.close()

if (__name__ == "__main__"):
    main()