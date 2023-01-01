with open("../input.txt", "r") as f:
    data = f.read().split("\n\n")

monkeys = {}
monkey_divisibility = 1

data = [data[x].replace(" ", "").split("\n") for x in range(len(data))]


for monkey in data:
    name = monkey[0].replace(":", "").lower()
    starting_items = list(map(int, monkey[1].replace("Startingitems:", "").split(",")))
    operation = monkey[2].replace("Operation:new=old", "")
    divisiblity = int(monkey[3].replace("Test:divisibleby", ""))
    iftrue = monkey[4].replace("Iftrue:throwto", "")
    iffalse = monkey[5].replace("Iffalse:throwto", "")

    monkey_divisibility *= divisiblity
    monkeys[name] = {
        "Starting Items" : starting_items,
        "Operation" : operation,
        "Divisibility" : divisiblity,
        "True" : iftrue,
        "False" : iffalse,
        "Inspection" : 0,
    }


for operation in range(1, 10000 + 1):
    for monkey_name in monkeys:
        monkey_data = monkeys[monkey_name]

        for item in monkey_data["Starting Items"]:
            worry_level = item

            if "old" in monkey_data["Operation"]:
                if "*" in monkey_data["Operation"]:
                    worry_level *= worry_level 
                else:
                    worry_level += worry_level
            elif "*" in monkey_data["Operation"]:
                worry_level *= int(monkey_data["Operation"].replace("*", ""))
            else:
                worry_level += int(monkey_data["Operation"].replace("+", ""))

            worry_level = worry_level % monkey_divisibility

            if worry_level % monkey_data["Divisibility"] == 0:
                monkeys[monkey_data["True"]]["Starting Items"].append(worry_level)
            else:
                monkeys[monkey_data["False"]]["Starting Items"].append(worry_level)

            monkey_data["Inspection"] += 1

        monkey_data["Starting Items"] = []

    #if operation in [1, 20, 1000, 2000, 5000]:
    print(f"{operation}\r", end="")



most_inspection = sorted([monkeys[monkey]["Inspection"] for monkey in monkeys])[-2:]
print(most_inspection[0] * most_inspection[1])