score = 0

def rps_outcome(player1, player2):
    out = None

    if player1 == player2:
        out = 0
    elif player1 == "rock" and player2 == "scissor":
        out = 1
    elif player1 == "paper" and player2 == "rock":
        out = 1
    elif player1 == "scissor" and player2 == "paper":
        out = 1
    else:
        out = 2

    # 0 == draw, 1 == player1 won, 2 == player2 won
    return out

def points(attack):
    out = None
    if attack == "rock":
        out = 1
    elif attack == "paper":
        out = 2
    else:
        out = 3

    return out

def convert(inp):

    out = ""

    if inp == "A" or inp == "X":
        out = "rock"
    elif inp == "B" or inp == "Y":
        out = "paper"
    elif inp == "C" or inp == "Z":
        out = "scissor"

    return out


with open("../input.txt", "r") as f:
    rps = f.read()

for game in rps.split("\n"):
    player = convert(game[2])
    opp = convert(game[0])

    out = rps_outcome(opp, player)
    init_score = score

    if out == 0:
        print("Draw")
        score += 3
    elif out == 2:
        print("Won")
        score += 6
    elif out == 1:
        print("Lost")
        score += 0

    score += points(player)

    print(score - init_score)

print("Total : " , score)
