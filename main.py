# Import
from graphics import *
import threading

# Import Files
from src.render import startMenu, render

# Window
width, height = 800, 600

# Player
playerY = height/2
playerYGoal = height/2

# Main
def main():
    # Create window
    window = GraphWin("python-pong", width, height)

    # Start Menu
    startMenu(window, width, height)
    

    # Get mouse Y
    def motion(event):
        playerYGoal = event.y
        point = Point(300, playerYGoal)
        point.setFill("Red")
        point.draw(window)
    window.bind('<Motion>', motion)

    # render_thread = threading.Thread(target=render)
    # render_thread.start()
    
    render(window)
    print(window.mouseY)
    
    window.getMouse()
    window.close()

if (__name__ == "__main__"):
    main()