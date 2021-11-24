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
        if random.random() < gameData["powerup"]["spawnChance"]:
            x = random.randrange(gameData["powerup"]["marginX"], (gameData["window"]["width"] - gameData["powerup"]["marginX"]))
            y = random.randrange(gameData["powerup"]["marginY"], (gameData["window"]["height"] - gameData["powerup"]["marginY"]))
            element = renderPowerup(x, y, gameData) 

            #TODO return elemento completo
            return element

def randomPowerup(gameData):
    probBad = 1.2 ** gameData["score"] - 1
    result = None
    if (probBad > random.randrange(0, 100)):
        result = powerups["bad"][random.randrange(0, len(powerups["bad"])- 1)]
    else:
        result = powerups["good"][random.randrange(0, len(powerups["good"])- 1)]
    gameData["powerup"]["active"][result] = gameData["powerup"]["duration"]
    return result
