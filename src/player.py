from src.render import pause

def movePlayer(gameData):
    newY = (gameData["player"]["y"] + gameData["player"]["stepSize"] if (gameData["player"]["yGoal"] > gameData["player"]["y"]) else gameData["player"]["y"] - gameData["player"]["stepSize"]) if ((gameData["player"]["yGoal"] - gameData["player"]["y"]) > gameData["player"]["stepSize"] or (gameData["player"]["y"] - gameData["player"]["yGoal"]) > gameData["player"]["stepSize"]) else gameData["player"]["y"]

    key = gameData["window"]["element"].checkKey()
    if key == "Up" and gameData["player"]["yGoal"] > 0:
        newY -= gameData["player"]["stepSize"]
        gameData["player"]["yGoal"] = gameData["player"]["y"]
    elif key == "Down" and gameData["player"]["yGoal"] < gameData["window"]["height"]:
        newY += gameData["player"]["stepSize"]
        gameData["player"]["yGoal"] = gameData["player"]["y"]
    elif key == "Escape":
        pause(gameData["window"]["element"], gameData["window"]["width"]/2, gameData["window"]["height"]/2)

    gameData["player"]["element"].move(gameData["player"]["x"] - gameData["player"]["x"], newY - gameData["player"]["y"])

    return newY