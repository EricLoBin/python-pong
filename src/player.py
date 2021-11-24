def movePlayer(gameData, thisTick, player):
    player.move(thisTick["player"]["x"] - gameData["player"]["x"], thisTick["player"]["y"] - gameData["player"]["y"])
    key = gameData["window"]["element"].checkKey()

    if key == "Up" and gameData["player"]["yGoal"] > 0:
        gameData["player"]["yGoal"] -= gameData["player"]["stepSize"]
    elif key == "Down" and gameData["player"]["yGoal"] < gameData["window"]["height"]:
        gameData["player"]["yGoal"] += gameData["player"]["stepSize"]