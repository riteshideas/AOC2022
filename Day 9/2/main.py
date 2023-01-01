import numpy as np


with open("../input.txt", "r") as f:
    data = f.read().split("\n")

no_tails = 9
tails = {}
space = 50
S = np.array([0, 0])
H = np.array([0, 0])
for x in range(1, no_tails + 1):
    tails[x] = {
        "pos" : np.array([0, 0]),
        "previous" : x - 1 if x != 1 else "H",
    }

T_moves = []

turns = list(map(lambda x: x.split(" ")[0], data))
steps = list(map(lambda x: x.split(" ")[1], data))

for turn, step in zip(turns, steps):
    for _ in range(int(step)):
        if turn == "U":
            H += [0, 1]
        elif turn == "D":
            H += [0, -1]
        elif turn == "R":
            H += [1, 0]
        elif turn == "L":
            H += [-1, 0]

        for tail in tails:
            current_pos = tails[tail]["pos"]
            following_tail_pos = H if tail == 1 else tails[tails[tail]["previous"]]["pos"]
            adjacent_to_tail = 2 > np.linalg.norm(following_tail_pos-current_pos)

            if not adjacent_to_tail:
                moves = np.array([[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]])
                dist_btwn = np.linalg.norm(following_tail_pos-(current_pos+moves), axis=1)
                closest_move = moves[np.argmin(dist_btwn)]
                tails[tail]["pos"] += closest_move

            if tail == 9 and tails[tail]["pos"].tolist() not in T_moves:
                T_moves.append(tails[tail]["pos"].tolist())


print(len(T_moves))

