# Please to the problem statement for more details of the question

import numpy as np

visible_trees = 0

with open("../input.txt", "r") as f:
    tree_height = f.read()

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

        if all(tree > up) or all(tree > down) or all(tree > right) or all(tree > left):
            visible_trees += 1

print(visible_trees)