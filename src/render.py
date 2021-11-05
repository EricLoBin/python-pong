from graphics import *

def startMenu(window, x, y):
    window.setBackground("#444444")

    rectangle = Rectangle(Point(10, 10), Point(x-10, y-10))
    rectangle.setFill("#222222")
    rectangle.draw(window)
    
    text = Text(Point(x/2, y/2), "Play")
    text.setSize(30)
    text.draw(window)
    
    window.getMouse()
    
    rectangle.undraw()
    text.undraw()

def render(window):
    window.setBackground("#444444")
