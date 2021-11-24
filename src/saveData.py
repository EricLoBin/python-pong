import os

def writeLeaderboard(data):
    leaderboard = open("data/leaderboard.csv", "w")
    leaderboard.write(",".join(data))

def readLeaderboard():
    try:
        leaderboard = open("data/leaderboard.csv", "r")
        return leaderboard.read().split(",")
    except:
        os.makedirs("data")
        open("data/leaderboard.csv", "x")
        return []

def updateLeaderboard(name, score):
    insert = f"{((10 - len(name)) * ' ')}{name}: {score}"
    leaderboard = readLeaderboard()

    if (len(leaderboard) == 0 or leaderboard[0] == ""):
        leaderboard = [insert]
    else:
        leaderboard.append(insert)
        leaderboard.sort(key = lambda x: int(x[12:]), reverse=True)
    
    writeLeaderboard(leaderboard)
    return [] #TODO
