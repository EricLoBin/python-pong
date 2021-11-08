from graphics import *

def settings():
    settingsWin = GraphWin("Settings", 200, 200)
    return

def startMenu(window, x, y):
    window.setBackground("#444444")

    rectangle = Rectangle(Point(10, 10), Point(x-10, y-10))
    rectangle.setFill("#222222")
    rectangle.draw(window)
    
    text = Text(Point(x/2, y/2), "Play")
    text.setFill("#ffffff")
    text.setSize(30)
    text.draw(window)

    settingsBtn = Text(Point(x/2, 30), "Settings")
    settingsBtn.setFill("#ffffff")
    settingsBtn.setSize(15)
    settingsBtn.draw(window)

    credits = Text(Point(x/2, (y/2)+90), '''Eric Loges Binsfeld
Lucca Oliari Peixoto
Lucca Resende da Costa Paiva
Thiago Rios da Silva
''')
    credits.setFill("#ffffff")
    credits.setSize(12)
    credits.draw(window)
    
    while True:
        click = window.getMouse()
        if (20 <= click.getY() <= 50 and (x/2)-50 <= click.getX() <= (x/2)+50):
            settings()
        else:
            break

    rectangle.undraw()
    text.undraw()
    settingsBtn.undraw()
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
