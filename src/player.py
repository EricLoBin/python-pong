def movePlayer(gameData):
    newY = (gameData["player"]["y"] + gameData["player"]["stepSize"] if (gameData["player"]["yGoal"] > gameData["player"]["y"]) else gameData["player"]["y"] - gameData["player"]["stepSize"]) if ((gameData["player"]["yGoal"] - gameData["player"]["y"]) > gameData["player"]["stepSize"] or (gameData["player"]["y"] - gameData["player"]["yGoal"]) > gameData["player"]["stepSize"]) else gameData["player"]["y"]

    gameData["player"]["element"].move(gameData["player"]["x"] - gameData["player"]["x"], newY - gameData["player"]["y"])
    key = gameData["window"]["element"].checkKey()

    if key == "Up" and gameData["player"]["yGoal"] > 0:
        gameData["player"]["yGoal"] -= gameData["player"]["stepSize"]
    elif key == "Down" and gameData["player"]["yGoal"] < gameData["window"]["height"]:
        gameData["player"]["yGoal"] += gameData["player"]["stepSize"]
    
    return newY