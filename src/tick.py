
# Import Files
import src.ball as ball

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
    
    
    return {
        "player": {
            "x": gameData["player"]["x"],
            "y": gameData["player"]["y"] + gameData["player"]["stepSize"] if (gameData["player"]["yGoal"] > gameData["player"]["y"]) else gameData["player"]["y"] - gameData["player"]["stepSize"],

            "yGoal": gameData["player"]["yGoal"]
        },
        "ball": ballData
    }