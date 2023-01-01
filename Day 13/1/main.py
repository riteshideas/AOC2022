with open("../input.txt", "r") as f:
    data = f.read().split("\n\n")

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

t = 0
for index, d in enumerate(data):
    left_str = d.split("\n")[0]
    right_str = d.split("\n")[1]

    left_lst = eval(left_str)
    right_lst = eval(right_str)

    left_len = len(left_lst)
    right_len = len(right_lst)

    if compare(left_lst, right_lst) < 0:
        t += index + 1

print(t)