from graphics import *
import random 

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

    credits = Text(Point(x/2, (y/2)+90), '''Antonio Pedro de Mattos Vieira Quezado
Eric Loges Binsfeld
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


# def createElements(window, gameData):
#     window.setBackground("#444444")

# Player
def renderPlayer(x, y, gameData):
    player = Rectangle(
        Point(x-(gameData["player"]["width"]/2),y-(gameData["player"]["height"]/2)),
        Point(x+(gameData["player"]["width"]/2),y+(gameData["player"]["height"]/2)))

    player.setFill("#ff0000")
    player.draw(gameData["window"]["element"])
    return player

#player = Point(gameData["player"]["x"], gameData["player"]["y"])
#player.setFill("Red")
#player.draw(window)




def renderBall(x, y, gameData):
    ball = Circle(Point(x, y), gameData["ball"]["radius"])
    ball.setFill(gameData["ball"]["color"])
    ball.draw(gameData["window"]["element"])
    return ball

def renderPowerup(x, y, gameData):
    powUp = Rectangle(Point(x, y), Point(x + gameData["powerup"]["size"], y + gameData["powerup"]["size"]))
    powUp.setFill(color_rgb(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
    powUp.draw(gameData["window"]["element"])
    return powUp