# Please to the problem statement for more details of the question

with open("../input.txt", "r") as f:
    rucksack_data = f.read()

priority_sum = 0
rucksack_datas_ = rucksack_data.split("\n")

rucksack_datas = []
for i in range(0, len(rucksack_datas_), 3):
    rucksack_datas.append(rucksack_datas_[i] + "\n" + rucksack_datas_[i+1] + "\n" + rucksack_datas_[i+2])


for rucksack_data in rucksack_datas:
    sep = int((len(rucksack_data) + 1) / 2)
    rucksack_data_first , rucksack_data_second , rucksack_data_third = rucksack_data.split("\n")

    contents = list(set(rucksack_data_first)&set(rucksack_data_second)&set(rucksack_data_third))

    for content in contents:
        if content.islower():
            priority_sum += ord(content) - 96
        else:
            priority_sum += ord(content) - 38


print(priority_sum)