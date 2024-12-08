file_name = "AOC/2022/data/aoc_7.txt"

from collections import defaultdict

#Credits to https://git.arul.io/arul/advent_of_code_2022/src/branch/main/07/sol.py as I was completely lost

with open(file_name) as file:
    data = [line.strip().split() for line in file]



def get_size(data):
    sizes = defaultdict(list)
    path = ""
    for i in data:
        if i[0] == "$":
            if i[1] == "cd":
                if i[-1]=="..":
                    path = path[:path[:-1].rfind("/")+1]
                    exit_directory = 1
                else: 
                    if i[-1] == "/": path = "/"
                    else: path += (i[-1]+"/")
        else:
            if i[0] =="dir": sizes[path].append(f"{path}{i[-1]}/")
            else: sizes[path].append(i[0])
    return sizes

def get_directory_size(sizes, directory):
    total = 0
    for size in sizes[directory]:
        if size.isnumeric():
            total += int(size)
        else:
            total += get_directory_size(sizes,size)
    return total

def get_all_directory_sizes(sizes):
    return [get_directory_size(sizes, directory) for directory in sizes.keys()]

def find_directory_to_delete(sizes):
    total_space = 70000000
    required_space = 30000000
    used_space = get_directory_size(sizes, "/")

    available_space = total_space - used_space
    smallest = total_space
    amount_to_free = required_space - available_space
    for i in get_all_directory_sizes(sizes):
        if i >= amount_to_free and i < smallest:
            smallest = i


    return smallest


print("Part 1")
sizes = get_size(data)
print(sum((size for size in get_all_directory_sizes(sizes) if size<=100000)))


print("Part 2")
print(find_directory_to_delete(sizes))

