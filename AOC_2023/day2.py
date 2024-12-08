import re
import numpy as np

def part1(file_name):
    valid = {"red":12, "green":13, "blue": 14}
    all_games = {}
    ans = []
    with open(file_name, "r") as f:
        data = f.readlines()

    for line in data:
        id = line[5: line.index(":")]
        all_games[id] = 1
        game = line[line.index(":")+2: ]
        sets = game.split(";")
        for s in sets:
            entries = s.split(" ")
            entries = [entry for entry in entries if entry != '']
            for i in range(len(entries)//2):
                for color in list(valid.keys()):
                    if color in entries[i*2+1]  and int(entries[i*2]) > valid[color]: 
                        all_games[id] = 0
                    

        ans = [int(id) for id in all_games.keys() if all_games[id] != 0]
    return sum(ans)

def part2(file_name):
    
    all_games = {}
    ans = []
    with open(file_name, "r") as f:
        data = f.readlines()

    for line in data:
        valid = {"red": 0, "green": 0, "blue": 0}
        id = line[5: line.index(":")]
        all_games[id] = 1
        game = line[line.index(":")+2: ]
        sets = game.split(";")
        for s in sets:
            entries = s.split(" ")
            entries = [entry for entry in entries if entry != '']
            for i in range(len(entries)//2):
                for color in list(valid.keys()):

                    if color in entries[i*2+1]  and int(entries[i*2]) > valid[color]: 
                        valid[color] = int(entries[i*2])
                        
        values = list(valid.values())
        a = values[0] * values[1] * values[2]
                    
        ans.append(a)


    return sum(ans)

def main():
    data_file = "data_day2.txt"
    ans = part1(data_file)
    print(f"Part one: {ans}")
    ans = part2(data_file)
    print(f"Part Two: {ans}")

if __name__ == "__main__":
    main()
