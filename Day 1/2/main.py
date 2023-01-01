with open("../input.txt", "r") as f:
    calories = f.read()

elf_calories = []

for elf_calorie in calories.split("\n\n"):
    elf_calories.append(sum(list(map(int, elf_calorie.split("\n")))))

elf_calories.sort()

print(sum(elf_calories[-3:]))