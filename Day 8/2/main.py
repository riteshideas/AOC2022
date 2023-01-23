# Please to the problem statement for more details of the question

import numpy as np

score = 0

with open("../input.txt", "r") as f:
    tree_height = f.read()

def dist_btw(x, y):
    f = 0
    for z in range(len(y)):
        f = z + 1
        if x <= y[z]:
            break
    return f

# Formatting the tree height
tree_height = tree_height.split("\n")
for tree in range(len(tree_height)):
    tree_height[tree] = list(map(int, list(tree_height[tree])))

x = len(tree_height)

for j in range(len(tree_height)):
    for k in range(len(tree_height[j])):
        tree = tree_height[k][j]

        up_down = np.array(tree_height).T[j]
        right_left = np.array(tree_height[k])
        
        up = up_down[0:k]
        down = up_down[k + 1:]
        left = right_left[0:j]
        right = right_left[j + 1:]

        s_up = dist_btw(tree, list(reversed(up)))
        s_down = dist_btw(tree, down)
        s_right = dist_btw(tree, right)
        s_left = dist_btw(tree, list(reversed(left)))

        s = s_up * s_down * s_left * s_right

        if s > score:
            print(s_up, s_down, s_left, s_right,"  ", j, k, tree)
            score = s


print(score)