with open("../input.txt", "r") as f:
    rucksack_data = f.read()

priority_sum = 0
rucksack_datas = rucksack_data.split("\n")

for rucksack_data in rucksack_datas:
    sep = int((len(rucksack_data) + 1) / 2)
    rucksack_data_first = rucksack_data[:sep]
    rucksack_data_second = rucksack_data[sep:]

    contents = list(set(rucksack_data_first)&set(rucksack_data_second))

    for content in contents:
        if content.islower():
            priority_sum += ord(content) - 96
        else:
            priority_sum += ord(content) - 38

print(priority_sum)