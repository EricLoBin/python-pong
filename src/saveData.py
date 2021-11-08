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

def updateLeaderboard(newScore):
    leaderboard = readLeaderboard()

    if (len(leaderboard) == 0 or leaderboard[0] == ""):
        leaderboard = [newScore]
    else:
        leaderboard.append(newScore)
        leaderboard.sort(key = lambda x: int(x[6:]), reverse=True)
    
    writeLeaderboard(leaderboard)
    return [] #TODO
