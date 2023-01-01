import json

dirs = {}
dir_complexities = {}
current_dir = ""
listing = False
size = 0


with open("../input.txt", "r") as f:
    filesystem = f.read()

commands = filesystem.split("\n")

for command in commands:
    if "$" in command:  # Usr sent command
        listing = False
        cmd = command.replace(" ", "").replace("$", "")
        if "cd" in cmd:
            if ".." in cmd:
                current_dir = dirs[current_dir]["parent dir"]
            else:
                parent_dir = current_dir
                current_dir = str(parent_dir) + "," + cmd.replace("cd", "")
                dir_complexity = 0 if current_dir == ",/" else dirs[parent_dir]["dir complexity"] + 1
                dirs[current_dir] = {
                    "parent dir" : parent_dir,
                    "files" : {},
                    "dirs" : [],
                    "total size" : 0,
                    "dir complexity" : dir_complexity,
                }
                if dir_complexity in dir_complexities:
                    dir_complexities[dir_complexity].append(current_dir)
                    dir_complexities[dir_complexity] = list(set(dir_complexities[dir_complexity]))
                else:
                    dir_complexities[dir_complexity] = [current_dir]
        elif "ls" in cmd:
            listing = True
    else:  # Output
        if listing:
            listed_files = command.split(" ")
            if "dir" in listed_files:
                dirs[current_dir]["dirs"].append(current_dir + "," + listed_files[-1])
                dirs[current_dir + "," + listed_files[-1]] = {
                    "parent dir" : current_dir,
                    "files" : {},
                    "dirs" : [],
                    "total size" : 0,
                    "dir complexity" : dirs[current_dir]["dir complexity"] + 1
                }

                if dirs[current_dir]["dir complexity"] in dir_complexities:
                    dir_complexities[dirs[current_dir]["dir complexity"]].append(current_dir)
                    dir_complexities[dirs[current_dir]["dir complexity"]] = list(set(dir_complexities[dirs[current_dir]["dir complexity"]]))
                else:
                    dir_complexities[dirs[current_dir]["dir complexity"]] = [current_dir]

            else:
                dirs[current_dir]["files"][listed_files[1]] = int(listed_files[0])



for complexities in reversed(sorted(dir_complexities.keys())):
    for complexity in dir_complexities[complexities]:
        dirs[complexity]["total size"] = sum(dirs[complexity]["files"].values()) + sum([dirs[x]["total size"] for x in dirs[complexity]["dirs"]])

for dir in dirs:
    if 100000 >= dirs[dir]["total size"]:
        size += dirs[dir]["total size"]

print(size)