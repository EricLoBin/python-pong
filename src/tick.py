import time
import sched

def tick(gameData):
    
    return {
        "player": {
            "x": gameData["player"]["x"],
            "y": gameData["player"]["y"] + gameData["player"]["stepSize"] if (gameData["player"]["yGoal"] > gameData["player"]["y"]) else gameData["player"]["y"] - gameData["player"]["stepSize"],

            "yGoal": gameData["player"]["yGoal"]
        },
        "ball": {
            "x": 1,
            "y": 1,
            "step": 5,
            "angle": 180,
            "radius": 1,
            "color": "#ff0000"
        }
    }