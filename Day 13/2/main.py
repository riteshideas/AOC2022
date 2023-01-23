# Please to the problem statement for more details of the question

with open("../input.txt", "r") as f:
    data = list(map(eval, f.read().split()))

def compare(x, y):
    if type(x) == int:
        if type(y) == int:
            return x - y
        else:
            return compare([x], y)
    else:
        if type(y) == int:
            return compare(x, [y])

    for j, k in zip(x, y):
        v = compare(j, k)
        if v:
            return v

    return len(x) - len(y)


i_2 = 1
i_6 = 2

for z in data:
    if compare(z, [[2]]) < 0:
        i_2 += 1
        i_6 += 1
    elif compare(z, [[6]]) < 0:
        i_6 += 1

print(i_2 * i_6)