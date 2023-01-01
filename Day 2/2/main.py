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

def losing(inp):
    out = None
    if inp == "rock":
        out = "paper"
    elif inp == "paper":
        out = "scissor"
    else:
        out = "rock"

    return out

def winning(inp):
    out = None
    if inp == "rock":
        out = "scissor"
    elif inp == "paper":
        out = "rock"
    else:
        out = "paper"

    return out

with open("../input.txt", "r") as f:
    rps = f.read()

for game in rps.split("\n"):
    player = game[2]
    player_out = None
    opp = convert(game[0])

    if player == "X":
        player_out = winning(opp)
    elif player == "Y":
        player_out = opp
    else:
        player_out = losing(opp)

    out = rps_outcome(opp, player_out)
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

    score += points(player_out)

    print(score - init_score)
    print(f"Player : {player_out}, Opp : {opp}")
    print()

print("Total : " , score)
