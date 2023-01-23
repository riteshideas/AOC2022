# Please to the problem statement for more details of the question

import json

dirs = {}
dir_complexities = {}
current_dir = ""
listing = False
size = []


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
                    "parent dirs" : [],
                    "parent dir" : parent_dir,
                    "files" : {},
                    "dirs" : [],
                    "total size" : 0,
                    "dir complexity" : dir_complexity,
                }

                if parent_dir != "":
                    parent_dirs = dirs[parent_dir]["parent dirs"]
                    parent_dirs.append(parent_dir)
                    dirs[current_dir]["parent dirs"] = parent_dirs
                    dirs[current_dir]["parent dirs"] = list(set(dirs[current_dir]["parent dirs"]))

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
                    "parent dirs" : [],
                    "files" : {},
                    "dirs" : [],
                    "total size" : 0,
                    "dir complexity" : dirs[current_dir]["dir complexity"] + 1
                }

                
                parent_dirs = dirs[current_dir]["parent dirs"]
                parent_dirs.append(current_dir)
                dirs[current_dir + "," + listed_files[-1]]["parent dirs"] = parent_dirs
                dirs[current_dir + "," + listed_files[-1]]["parent dirs"] = list(set(dirs[current_dir + "," + listed_files[-1]]["parent dirs"]))

                if dirs[current_dir]["dir complexity"] in dir_complexities:
                    dir_complexities[dirs[current_dir]["dir complexity"]].append(current_dir)
                    dir_complexities[dirs[current_dir]["dir complexity"]] = list(set(dir_complexities[dirs[current_dir]["dir complexity"]]))
                else:
                    dir_complexities[dirs[current_dir]["dir complexity"]] = [current_dir]

            else:
                dirs[current_dir]["files"][listed_files[1]] = int(listed_files[0])

for dir in dirs:
    if dirs[dir]["parent dir"] == "":
        dirs[dir]["parent dirs"] = []

    parent_dirs = dirs[dir]["parent dirs"]
    parent_dirs = list(set(parent_dirs))
    if dir in parent_dirs:
        parent_dirs.remove(dir)

    dirs[dir]["parent dirs"] = parent_dirs

for dir in dirs:
    dirs[dir]["total size"] = sum(dirs[dir]["files"].values())
    for x in dirs[dir]["parent dirs"]:
        dirs[x]["total size"] += dirs[dir]["total size"]


size_required = 30000000 - (70000000 - dirs[",/"]["total size"])

for dir in dirs:
    if size_required <= dirs[dir]["total size"]:
        size.append(dirs[dir]["total size"])

for x in sorted(size):
    print(x)