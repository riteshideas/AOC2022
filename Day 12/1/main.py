import numpy as np
import math
from collections import deque
import sys
from os import system
import time


np.set_printoptions(threshold=sys.maxsize)


with open("../input.txt", "r") as f:
    data = f.read().split("\n")

data = list(map(lambda x: list(x), data))

DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


height = len(data)
width = len(data[0])
nodes = []

for y in range(height):
    for x in range(width):

        if data[y][x] == "S":
            start = (y, x)
            data[y][x] = "a"
        
        if data[y][x] == "E":
            end = (y, x)
            data[y][x] = "z"


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
            print(d + 1)
            exit(0)

            
        queue.append((d + 1, pos[0], pos[1]))
        visited_nodes.add(pos)
