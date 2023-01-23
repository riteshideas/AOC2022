# Please to the problem statement for more details of the question

with open("../input.txt", "r") as f: 
    calories = f.read()

elf_calories = []

for elf_calorie in calories.split("\n\n"): # Getting the total amount of calories for each elf
    elf_calories.append(sum(list(map(int, elf_calorie.split("\n")))))

print(max(elf_calories)) #Printing the maximum amount of calories