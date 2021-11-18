import random

from src.render import renderPowerup

powerups = {
    "good": [
        "moreBalls",    # mais bolas
        "bigBalls",     # bolas grandes
        "bigPlayer",    # barra grande
        "slowBall",     # bola lenta
        "extraLife",    # vida extra
        "doublePoints"  # dobro de pontos
    ],
    "bad": [
        "smallBalls",   # bolas pequenas
        "twoSides",     # player (barra) dos dois lados
        "smallPlayer",  # barra pequena    
        "fastBall",     # bola rápida
    ]
}

def trySpawn(gameData):
    
    if len(gameData["powerup"]["elements"]) < gameData["powerup"]["max"]:
        if random.random() < 0.025:
            x = random.randrange(30, (gameData["window"]["width"] - 30))
            y = random.randrange(15, (gameData["window"]["height"] - 15))
            element = renderPowerup(x, y, gameData) 

            #TODO return elemento completo
            return element

