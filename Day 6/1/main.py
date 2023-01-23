# Please to the problem statement for more details of the question

with open("../input.txt", "r") as f:
    datastream = f.read()

for x in range(len(datastream)):
    char = datastream[x:x+4]

    if len(char) > 4:
        print("Not enough char")
        break
    
    if 4 == len(set(char)):
        print(f"Buffer found at : {x + 4}, {char}")
        break