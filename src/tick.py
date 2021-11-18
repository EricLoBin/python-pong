from random import randrange

# Import Files
import src.ball as ball
import src.powerup as powerup

def tick(gameData):

    # Ball
    ballData = gameData["ball"]
    for i, ballElement in enumerate(ballData["balls"]):
        if (ballElement["y"]-ballData["radius"] <= 0 or ballElement["y"]+ballData["radius"] >= gameData["window"]["height"]):
            ballElement["angle"] = ball.reflectBall(ballElement["angle"])

        ballElement["x"], ballElement["y"] = ball.moveBall(
            ballElement["x"],
            ballElement["y"],
            ballElement["angle"],
            ballData["step"],
            ballElement["element"]
        )

        ballData["balls"][i] = ballElement

        if (gameData["gamemode"] == "normal" and ("twoSides" not in gameData["powerup"]["active"])):
            if (ballElement["x"] - ballData["radius"] < 0):
                ballElement["x"] = ballData["radius"]
                ballElement["angle"] = randrange(20, 160)

        if (ballElement["x"]< 0 - ballData["radius"] or ballElement["x"] > gameData["window"]["width"] + ballData["radius"]):
            ballElement["element"].undraw()
            ballData["balls"].pop(i)

        #playerCollision
        if (ballElement["x"] - ballData["radius"] <= gameData["player"]["x"] - (gameData["player"]["width"]/2) <= ballElement["x"] + ballData["radius"]):
            if (gameData["player"]["y"] - (gameData["player"]["height"]/2) <= ballElement["y"] <= gameData["player"]["y"] + (gameData["player"]["height"]/2)):
                ballElement["angle"] = randrange(190, 350)
                gameData["score"] += 1
                print(gameData["score"])

    if (len(ballData["balls"]) == 0 and gameData["player"]["lifes"] > 0):
        gameData["player"]["lifes"] -= 1
        ballData["balls"].append(ball.createBall(gameData))
    elif (len(ballData["balls"]) == 0 and gameData["player"]["lifes"] <= 0):
        print("gameOver")
        #TODO Game Over
    
    #Powerup
    powerupData = gameData["powerup"]
    if (gameData["score"] % 5 == 0 and gameData["score"] != 0):
        powerupData["max"] += 1
    
    pUp = powerup.trySpawn(gameData)
    if (pUp):
        powerupData["elements"].append(pUp)
    
    return {
        "player": {
            "x": gameData["player"]["x"],
            "y": gameData["player"]["y"] + gameData["player"]["stepSize"] if (gameData["player"]["yGoal"] > gameData["player"]["y"]) else gameData["player"]["y"] - gameData["player"]["stepSize"],

            "yGoal": gameData["player"]["yGoal"]
        },
        "ball": ballData
    }


