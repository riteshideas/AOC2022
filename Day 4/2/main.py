# Please to the problem statement for more details of the question

with open("../input.txt", "r") as f:
    elf_pairs = f.read().split("\n")

overwork = 0
for pair in elf_pairs:
    pairs = pair.split(",")
    first_pair = pairs[0].split("-")
    second_pair = pairs[1].split("-")
    first_elf = list(range(int(first_pair[0]), int(first_pair[-1]) + 1))
    second_elf = list(range(int(second_pair[0]), int(second_pair[-1]) + 1))

    if any(item in first_elf for item in second_elf) or any(item in second_elf for item in first_elf):
        overwork += 1

print(overwork)