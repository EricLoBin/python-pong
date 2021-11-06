from graphics import *


def startMenu(window, x, y):
    window.setBackground("#444444")

    rectangle = Rectangle(Point(10, 10), Point(x-10, y-10))
    rectangle.setFill("#222222")
    rectangle.draw(window)
    
    text = Text(Point(x/2, y/2), "Play")
    text.setFill("#ffffff")
    text.setSize(30)
    text.draw(window)

    credits = Text(Point(x/2, (y/2)+90), '''Eric Loges Binsfeld
Lucca Oliari Peixoto
Lucca Resende da Costa Paiva
Thiago Rios da Silva
''')
    credits.setFill("#ffffff")
    credits.setSize(12)
    credits.draw(window)
    
    window.getMouse()

    rectangle.undraw()
    text.undraw()
    credits.undraw()


def createElements(window, gameData):
    window.setBackground("#444444")

    # Ball
    ball = Circle(Point(
        gameData["ball"]["x"],
        gameData["ball"]["y"]),
        gameData["ball"]["radius"])
    ball.setFill(gameData["ball"]["color"])
    ball.draw(window)

    # Player
    player = Point(gameData["player"]["x"], gameData["player"]["y"])
    player.setFill("Red")
    player.draw(window)

    return {
        "ball": ball,
        "player": player
    }
