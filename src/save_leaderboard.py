import os

def write_leaderboard(data):
    leaderboard = open("data/leaderboard.txt", "w")
    leaderboard.write("\n".join(data))

def read_leaderboard():
    try:
        leaderboard = open("data/leaderboard.txt", "r")
        return leaderboard.read().split("\n")
    except:
        os.makedirs("data")
        open("data/leaderboard.txt", "x")
        return []

def update_leaderboard(name, score):
    insert = f"{name}: {score}"
    leaderboard = read_leaderboard()

    leaderboard.append(insert)
    leaderboard.sort(key = lambda x: int(x.split(": ")[-1]), reverse=True)

    write_leaderboard(leaderboard)
