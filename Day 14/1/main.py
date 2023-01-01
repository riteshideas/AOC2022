import math
from os import system
import time

with open("../input.txt", "r") as f:
    data = list(map(lambda x: x.split(" -> "), f.read().split("\n")))

walls = set()
sand = set()
max_x = -math.inf
max_y = -math.inf

min_x = math.inf
min_y = math.inf

lowest_wall = math.inf

for path in data:
    start = path[0]

    for pos in path:
        
        start_x, start_y = start.split(",")
        start_x, start_y = int(start_x), int(start_y)


        x, y = pos.split(",")
        x, y = int(x), int(y)

        max_x = max(x, max_x)
        max_y = max(y, max_y)

        min_x = min(x, min_x)
        min_y = min(y, min_y)

        lowest_wall = min(y, lowest_wall)

        if start_y - y == 0:
            if start_x > x:
                for x_pos in range(x, start_x + 1):
                    walls.add((x_pos, y))
            else:
                for x_pos in reversed(range(start_x, x + 1)):
                    walls.add((x_pos, y))

        elif start_x - x == 0:
            if start_y > y:
                for y_pos in range(y, start_y + 1):
                    print(x, y_pos)
                    walls.add((x, y_pos))
            else:
                for y_pos in reversed(range(start_y, y + 1)):
                    walls.add((x, y_pos))
        
        start = pos


max_x = max(500, max_x)
max_y = max(0, max_y)

min_x = min(500, min_x)
min_y = min(0, min_y)




sand_no = 0
is_void = False
while not is_void:
    sand_loc = (500, 0)
    falling = True
    while falling:
        possible_dirs = []
        for dir in [(0, 1), (-1, 1), ( 1, 1)]:
            land_pos = (sand_loc[0] + dir[0], sand_loc[1] + dir[1])
            if land_pos not in sand and land_pos not in walls:
                possible_dirs.append(land_pos)
        
        if sand_loc[1] > max_y:
            falling = False
            is_void = True

        if len(possible_dirs) == 0:
            falling = False
            sand_no += 1
            sand.add(sand_loc)
        else:
            sand_loc = possible_dirs[0]

        

print(sand_no)
for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):

        if (x, y) == (500, 0):
            print("+", end="")
        elif (x, y) in sand:
            print("o", end="")
        elif (x, y) in walls:
            print("#", end="")
        else:
            print(" ", end="")

    print()