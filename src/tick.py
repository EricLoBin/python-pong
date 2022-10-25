from random import randrange

# Import Files
import src.powerup as powerup
from src.player import movePlayer

def tick(gameData):
    powerupData = gameData["powerup"]

    # Player
    # gameData["player"]["y"] = gameData["player"]["element"].move(gameData)
    gameData["player"]["y"] = movePlayer(gameData)
    

    # Ball
    for ball in gameData["ball"]["balls"]:
        ball.tick(gameData)
    # ballData = gameData["ball"]
    # for i, ballElement in enumerate(ballData["balls"]):
    #     if (ballElement["y"]-ballData["radius"] <= 0 or ballElement["y"]+ballData["radius"] >= gameData["window"]["height"]):
    #         ballElement["angle"] = ball.reflectBall(ballElement["angle"])

    #     ballElement["x"], ballElement["y"] = ball.moveBall(
    #         ballElement["x"],
    #         ballElement["y"],
    #         ballElement["angle"],
    #         ballData["step"],
    #         ballElement["element"]
    #     )

    #     # Left wall collision
    #     if (gameData["gamemode"] == "normal" and ("twoSides" not in gameData["powerup"]["active"])):
    #         if (ballElement["x"] - ballData["radius"] < 0):
    #             ballElement["x"] = ballData["radius"]
    #             ballElement["angle"] = randrange(30, 150)

    #     # Delete ball
    #     if (ballElement["x"]< 0 - ballData["radius"] or ballElement["x"] > gameData["window"]["width"] + ballData["radius"]):
    #         ballElement["element"].undraw()
    #         ballData["balls"].pop(i)

    #     #playerCollision
    #     if (ballElement["x"] - ballData["radius"] <= gameData["player"]["x"] - (gameData["player"]["width"]/2) <= ballElement["x"] + ballData["radius"]):
    #         if (gameData["player"]["y"] - (gameData["player"]["height"]/2) <= ballElement["y"] <= gameData["player"]["y"] + (gameData["player"]["height"]/2)):
    #             ballElement["angle"] = randrange(210, 330)
    #             ballElement["x"] = ballElement["element"].getCenter().x # Sync ball
    #             gameData["score"] += 1
    #             gameData["textscore"].setText(f"Score: {gameData['score']}")

    #             # powerupAmmount
    #             if (gameData["score"] % 5 == 0):
    #                 gameData["powerup"]["max"] += 2
        
    #     # powerupCollision
    #     ballXInitialPoint = ballElement["x"] - ballData["radius"]
    #     ballXEndPoint = ballElement["x"] + ballData["radius"]
    #     for i, p in enumerate(gameData["powerup"]["elements"]):
    #         powerupXInitialPoint = p.p1.x
    #         powerupXEndPoint = p.p2.x
    #         if (
    #             (powerupXInitialPoint < ballXInitialPoint < powerupXEndPoint) or
    #             (powerupXInitialPoint < ballXEndPoint < powerupXEndPoint)
    #             ):
    #             powerupYInitialPoint = p.p1.y
    #             powerupYEndPoint = p.p2.y
    #             ballYInitialPoint = ballElement["y"] - ballData["radius"]
    #             ballYEndPoint = ballElement["y"] + ballData["radius"]
    #             if (
    #                 (powerupYInitialPoint < ballYInitialPoint < powerupYEndPoint) or
    #                 (powerupYInitialPoint < ballYEndPoint < powerupYEndPoint)
    #                 ):
    #                 powerup.randomPowerup(gameData)
    #                 # print(gameData["powerup"]["active"])
    #                 p.undraw()
    #                 gameData["powerup"]["elements"].pop(i)
    #                 break


    if (len(gameData["ball"]["balls"]) == 0 and gameData["player"]["lifes"] > 0):
        gameData["player"]["lifes"] -= 1
        gameData["textlife"].setText(f"Vidas restantes: {gameData['player']['lifes']}")
        gameData["ball"]["balls"].append(ball.createBall(gameData))
    elif (len(gameData["ball"]["balls"]) == 0 and gameData["player"]["lifes"] <= 0):
        return True
        #TODO Game Over
    
    #Powerup
    ppup = None
    for pwup in powerupData["active"]:
        powerupData["active"][pwup] -= 1
        if powerupData["active"][pwup] == 0:
            ppup = pwup
    if ppup:
        del powerupData["active"][ppup]
        
            
    pUp = powerup.trySpawn(gameData)
    if (pUp):
        powerupData["elements"].append(pUp)

    
    return False
