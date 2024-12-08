import re
from string import punctuation
from tqdm import tqdm
import numpy as np

def part1(data):
    ans = 0
    i = data[0].index("|")
    
    for card in data:
        n = 0
        for x in card[i+1:]:
            if x in card[2:i]:
                n +=1

        if n>0:
            ans += np.power(2,n-1)

    return ans

def part2(data):
    n_cards = np.ones(len(data))
    print(n_cards.shape)
    ans = 0
    i = data[0].index("|")
    
    for id, card in enumerate(data):
        n = 0
        for x in card[i+1:]:
            if x in card[2:i]:
                n +=1
        if n>0:
            for j in range(1,n+1):
                n_cards[id+j]+=n_cards[id]

    ans = sum(n_cards)
    return ans


def main():
    file_name = "data/day4.txt"

    with open(file_name) as f:
        data = f.readlines()
    
    refined_data =[line.replace(":","").replace("\n","").split() for line in data]
    print(f"Part 1 answer: {part1(refined_data)}")

    print(f"Part 2 answer: {part2(refined_data)}")

if __name__ == "__main__":
    main()