import random

from src.render import renderPowerup

def trySpawn(gameData):
    
    if len(gameData["powerup"]["elements"]) < gameData["powerup"]["max"]:
        if random.random() < 0.1:
            x = random.randrange(30, (gameData["window"]["width"] - 30))
            y = random.randrange(15, (gameData["window"]["height"] - 15))
            element = renderPowerup(x, y, gameData) 

            #TODO return elemento completo
            return element

