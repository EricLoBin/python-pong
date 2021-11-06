# Import
from graphics import *
import time
# import threading

# Import Files
from src.render import startMenu, render
from src.tick import tick



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

        "yGoal": height/2,
        "stepSize": 5
    },
    "ball": {
        "x": width/2,
        "y": height/2,
        "step": 5,
        "angle": 170,
        "radius": 10,
        "color": "#ff0000"
    }
}



# Main
def main():
    # Create window
    window = GraphWin(
        gameData["window"]["title"],
        gameData["window"]["width"],
        gameData["window"]["height"]
    )

    # Start Menu
    startMenu(window, width, height)
    

    # Get mouse Y
    def motion(event):
        gameData["player"]["yGoal"] = event.y
    window.bind('<Motion>', motion)

    # render_thread = threading.Thread(target=render)
    # render_thread.start()

    # Create Elements

    # Player
    point = Point(gameData["player"]["x"], gameData["player"]["y"])
    point.setFill("Red")
    point.draw(window)

    # Ball
    ball = Circle(Point(
        gameData["ball"]["x"],
        gameData["ball"]["y"]),
        gameData["ball"]["radius"])
    ball.setFill(gameData["ball"]["color"])
    ball.draw(window)

    gameData["ball"]["element"] = ball

    running = True
    while running:
        thisTick = tick(gameData)
        
        time.sleep(1/gameData["tps"])

        point.move(thisTick["player"]["x"]-gameData["player"]["x"], thisTick["player"]["y"]-gameData["player"]["y"])

        render(window, gameData)
        gameData["player"]["y"] = thisTick["player"]["y"]
        gameData["ball"]["x"] = thisTick["ball"]["x"]
        gameData["ball"]["y"] = thisTick["ball"]["y"]
        gameData["ball"]["angle"] = thisTick["ball"]["angle"]
        
        # print(window.items)
    
    window.getMouse()
    window.close()

if (__name__ == "__main__"):
    main()