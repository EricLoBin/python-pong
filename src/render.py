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


# Pause
def pause(window, x, y):
    text = Text(Point(x, y), "PAUSE")
    text.setFill("#ffffff")
    text.setSize(15)
    text.draw(window)
    resume = Text(Point(x, y + 30), "CLIQUE NA TELA PARA CONTINUAR")
    resume.setFill("#f0f0f0")
    resume.setSize(10)
    resume.draw(window)

    window.getMouse()

    resume.undraw()
    text.undraw()

# Game Over
def gameOver(gameData):
    window = gameData["window"]["element"]
    width, height = gameData["window"]["width"], gameData["window"]["height"]
    for item in window.items:
        item.undraw()
    
    bg = Rectangle(Point(0, 0), Point(width, height))
    bg.setFill("#444444")
    bg.draw(window)

    # text = Text(Point(width/2, (height/2) - 20))
    # text.score

    input_box = Entry(Point(width/2, height/2), 20)
    input_box.setSize(20)
    input_box.draw(window)

    while True:
        input_box.setText(input_box.getText()[:10].upper())
        key = gameData["window"]["element"].checkKey()
        if (key == "Return"):
            break
    nickname = input_box.getText()
    #TODO
    window.close()

# Player
def renderPlayer(x, y, gameData):
    player = Rectangle(
        Point(x - (gameData["player"]["width"]/2), y - (gameData["player"]["height"]/2)),
        Point(x + (gameData["player"]["width"]/2), y + (gameData["player"]["height"]/2)))

    player.setFill("#ff0000")
    player.draw(gameData["window"]["element"])
    return player

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

def status(gameData):
    textlife = Text(Point(gameData["window"]["width"]/2, 15),f"Vidas restantes: {gameData['player']['lifes']}")
    textlife.setFill('#ffffff')
    textlife.draw(gameData["window"]["element"])
    textscore = Text(Point(gameData["window"]["width"]/ 2, 35), f"Score: {gameData['score']}")
    textscore.setFill('#ffffff')
    textscore.draw(gameData["window"]["element"])
    return textlife, textscore