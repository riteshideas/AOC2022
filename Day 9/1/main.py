# Please to the problem statement for more details of the question

import numpy as np

with open("../input.txt", "r") as f:
    data = f.read().split("\n")

S = np.array([0, 0])
H = np.array([0, 0])
T = np.array([0, 0])

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

        adjacent_to_h = 2 > np.linalg.norm(H-T)

        if not adjacent_to_h:
            moves = np.array([[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]])
            dist_btwn = np.linalg.norm(H-(T+moves), axis=1)
            closest_move = moves[np.argmin(dist_btwn)]
            T += closest_move

        if T.tolist() not in T_moves:
            T_moves.append(T.tolist())

print(len(T_moves))