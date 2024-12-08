import numpy as np
import re
import random

print_conditions = {}
print_order = []
pages_already_entered = []

def check_update(print_order, print_conditions):
    valid = True
    for q_idx in range(0, len(print_order)):
        query_page = print_order[q_idx]
        other_conditions = []
        for i in range(q_idx+1, len(print_order)):
            if print_order[i] in print_conditions.keys():
                other_conditions+=print_conditions[print_order[i]]
        if query_page in other_conditions:
            return False
        
    return True

def correct_order_p1(print_order, print_conditions):
    corrected_order = print_order
    while not check_update(corrected_order, print_conditions):
        for q_idx in range(0, len(corrected_order)):
            query_page = corrected_order[q_idx]
            for i in range(q_idx+1, len(corrected_order)):
                if corrected_order[i] in print_conditions.keys():
                    if corrected_order[q_idx] in print_conditions[corrected_order[i]]:
                        corrected_order[q_idx] = corrected_order[i]
                        corrected_order[i] = query_page
                        break

    return corrected_order

with open('AOC_2024/day5.txt', 'r') as f:
    for line in f.readlines():
        if '|' in line:
            a, b = line.strip().split("|")
            if a not in pages_already_entered:
                pages_already_entered.append(a)
                print_conditions[a] = [b]
            else: print_conditions[a].append(b)
        elif len(line)>1:
            print_order.append([i.strip() for i in line.split(',')])

part1_correct = 0
part2_correct = 0

for i, order in enumerate(print_order):
    if check_update(order, print_conditions):
        part1_correct += int(order[len(order)//2])
    else: 
        corrected_order = correct_order_p1(print_order[i], print_conditions)
        part2_correct += int(corrected_order[len(corrected_order)//2])

print('Part 1:',part1_correct)
print('Part 2:',part2_correct)
