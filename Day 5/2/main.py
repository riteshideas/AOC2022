# Please to the problem statement for more details of the question

import numpy as np


with open("../input.txt", "r") as f:
    crates = f.read()

crate_start_loc, crate_move = crates.split("\n\n")
crate_loc = []

# Get the starting position of the crate at first
crate_no = crate_start_loc.split("\n")[-1].split(" ")
crate_no = list(map(int, list(filter(None, crate_no))))

# Doing the moving action
crate_move = crate_move.replace("move ", "")
crate_move = crate_move.replace("from ", "")
crate_move = crate_move.replace("to ", "")

crate_move = crate_move.split("\n")

crate_move = list(map(lambda x : list(map(int , x.split())), crate_move))

qnts = [x[-1] for x in crate_move]



crate_start_loc = crate_start_loc.replace("[", "")
crate_start_loc = crate_start_loc.replace("]", "")

crate_start_loc = crate_start_loc.replace("    ", "-")
crate_start_loc = crate_start_loc.replace(" ", "")

crate_start_loc = crate_start_loc.split("\n")

crate_start_loc = crate_start_loc[:-1]

crate_start_loc = [list(x) for x in crate_start_loc]



crate_loc = []
crate_starting_loc = []

for _ in range(50):
    crate_starting_loc.append(["-"] * max(crate_no))


crate_loc = crate_starting_loc + crate_start_loc

crate_loc = np.array(crate_loc)

crate_loc = crate_loc.T

for move in crate_move:
    qnt = move[0]
    from_crate = move[1]
    to_crate = move[2]

    carrying_crates = []

    for _ in range(qnt):
        for i, y in enumerate(crate_loc[from_crate - 1]):
            if y != "-":
                carrying_crates.append(y)
                crate_loc[from_crate - 1][i] = "-"
                break
    
    for z in reversed(carrying_crates):
        for i, y in enumerate(crate_loc[to_crate - 1]):
            if i + 1 >= len(crate_loc[to_crate - 1]):
                crate_loc[to_crate - 1][i] = z

            elif y == "-" and crate_loc[to_crate - 1][i + 1] != "-":
                crate_loc[to_crate - 1][i] = z
                break

for y in crate_loc.T:
    for x in y:
        print(x, end=" ")
    print("")

print("\n\n")