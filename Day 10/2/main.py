import time

with open("../input.txt", "r") as f:
    instructions = f.read().split("\n")

instruction_cycle = 0
cycle = 1
interrupts = [20, 60, 100, 140, 180, 220]
executing_instruction = ["", 0, ""]
signal_strength = []
xReg = 1
row = 0
xRegs = []
screen = []

while True:

    if instruction_cycle >= len(instructions):
        break


    if executing_instruction != ["", 0, ""]:
        executing_instruction[1] -= 1
    
    if 0 >= executing_instruction[1]:
        if "addx" == executing_instruction[0]:
            xReg += int(executing_instruction[2].split()[1])
        executing_instruction = ["", 0, ""]

    if cycle in interrupts:
        signal_strength.append(cycle * xReg)

    if executing_instruction[0] == "":
        instruction = instructions[instruction_cycle].split()
        
        if "addx" in instruction[0]:
            executing_instruction = ["addx", 2, " ".join(instruction)]
        elif "noop" in instruction[0]:
            executing_instruction = ["noop", 1, " ".join(instruction)]

        instruction_cycle += 1
    xRegs.append(abs(xReg - cycle))


    if xReg + 2 >= (cycle - (row * 40)) >= xReg:
        print(chr(9608), end="")
    else:
        print(" ", end="")

    if cycle % 40 == 0:
        row += 1
        print()


    cycle += 1

#print(xRegs)