import time
import sched

# Import Files
import src.ball as ball

def tick(gameData):

    # Ball
    ballData = gameData["ball"]
    if (ballData["y"]-ballData["radius"] <= 0 or ballData["y"]+ballData["radius"] >= gameData["window"]["height"]):
        ballData["angle"] = ball.reflectBall(ballData["angle"])

    ballData["x"], ballData["y"] = ball.moveBall(
        ballData["x"],
        ballData["y"],
        ballData["angle"],
        ballData["step"],
        ballData["element"]
    )
    
    return {
        "player": {
            "x": gameData["player"]["x"],
            "y": gameData["player"]["y"] + gameData["player"]["stepSize"] if (gameData["player"]["yGoal"] > gameData["player"]["y"]) else gameData["player"]["y"] - gameData["player"]["stepSize"],

            "yGoal": gameData["player"]["yGoal"]
        },
        "ball": {
            "x": ballData["x"],
            "y": ballData["y"],
            "step": 5,
            "angle": ballData["angle"],
            "radius": 1,
            "color": "#ff0000"
        }
    }