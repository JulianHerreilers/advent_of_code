import re
from string import punctuation
from tqdm import tqdm
import numpy as np
from collections import deque

def graph_maker(file_name):
    graph = {}
    with open(file_name) as file:
        data  = file.readlines()
    data = [list(line.replace("\n","")) for line in data]

    N = len(data)
    M = len(data[0])
    for r in range(N):
        for c in range(M):
            if data[r][c] == "S":
                sr = r
                sc = c
                data[r][c] = "a"
            elif data[r][c] == "E":
                er = r
                ec = c
                data[r][c] = "z"
    sps = [(sr, sc)]
    for r in range(N):
        for c in range(M):
            valid = []
            curr = ord(data[r][c])
            if data[r][c] == "a": sps.append((r,c))
            if r-1>=0:
                if ord(data[r-1][c]) - curr <=1: valid.append(f"{r-1}_{c}")

            if c-1>= 0 and ord(data[r][c-1]) - curr<=1: valid.append(f"{r}_{c-1}")
            if c+1<M and ord(data[r][c+1]) - curr<=1: valid.append(f"{r}_{c+1}")

            if r+1<N:
                if ord(data[r+1][c]) - curr <=1: valid.append(f"{r+1}_{c}")
            graph[f"{r}_{c}"] = valid

    return graph, sr, sc, er, ec, data, sps

# Credits https://onestepcode.com/graph-shortest-path-python/

def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0
    next_node = node1
    # To keep track of previously visited nodes
    previous_nodes = {node1}
    if node1 == node2:
        
        return path_list[0]
        
    while path_index < len(path_list):
    # while next_node != node2:
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)

        # Continue to next path in list
        path_index += 1
    # No path is found
    return []

def part1(graph, sr, sc, er, ec, data):
    
    start = f"{sr}_{sc}"
    end = f"{er}_{ec}"

    return len(shortest_path(graph, start, end))-1


def part2(graph, er, ec, sps):
    
    end = f"{er}_{ec}"
    ans = []
    for sr, sc in tqdm(sps):
        start = f"{sr}_{sc}"
        a = len(shortest_path(graph, start, end))-1
        print(f"Anser for {start} is {a}")
        ans.append(a)

        

    
    ans = [a for a in ans if a!=-1]
    return min(ans)
    
def main():
    file_name = "data/day12.txt"
    graph, sr, sc, er, ec, data, sps = graph_maker(file_name)
    with open("data/temp.txt", "w") as file:

        file.write(str(graph))

    print(graph)
    print(f"Need to traverse from {sr}_{sc} to {er}_{ec}")


    print(f"Part 1 answer: {part1(graph, sr, sc, er, ec, data)}")
    print(f"Part 2 answer: {part2(graph, er, ec, sps)}")


if __name__ == "__main__":
    main()