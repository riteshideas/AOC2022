# Please to the problem statement for more details of the question

import math
from collections import deque


with open("../input.txt", "r") as f:
    data = f.read().split("\n")

data = list(map(lambda x: list(x), data))

DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


height = len(data)
width = len(data[0])
nodes = []
starting_nodes = deque()
shortest_path = math.inf

for y in range(height):
    for x in range(width):

        if data[y][x] == "S":
            data[y][x] = "a"
        
        if data[y][x] == "E":
            end = (y, x)
            data[y][x] = "z"

        if data[y][x] == "a":
            starting_nodes.append((y, x))
while starting_nodes:
    start = starting_nodes.popleft()

    queue = deque()
    visited_nodes = set()

    queue.append((0, start[0], start[1]))
    visited_nodes.add((start[0], start[1]))

    while queue:
        d, y, x = queue.popleft()

        for dir in DIRS:
            pos = (y + dir[0], x + dir[1])

            if 0 > pos[0] or 0 > pos[1] or pos[0] >= height or pos[1] >= width:
                continue

            if pos in visited_nodes:
                continue
            
            if ord(data[pos[0]][pos[1]]) - ord(data[y][x]) > 1:
                continue

            if pos == end:
                shortest_path = min(d + 1, shortest_path)
                break


            queue.append((d + 1, pos[0], pos[1]))
            visited_nodes.add(pos)

print(f"Current Shortest Path : {shortest_path}")