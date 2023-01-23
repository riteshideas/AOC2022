# Please to the problem statement for more details of the question

word_len = 14

with open("../input.txt", "r") as f:
    datastream = f.read()

for x in range(len(datastream)):
    char = datastream[x:x+word_len]

    if len(char) > word_len:
        print("Not enough char")
        break
    
    if word_len == len(set(char)):
        print(f"Buffer found at : {x + word_len}, {char}")
        break