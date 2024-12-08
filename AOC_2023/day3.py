import re
from string import punctuation
from tqdm import tqdm
def concat_num(string,x, row):

    num = ""
    i = x
    if i == -1: i = 0
    j = x
    while i-1>=0: 
       if  string[i-1].isdigit(): i-=1 
       else: break
    while j+1<len(string): 
        if string[j+1].isdigit(): j+=1 
        else: break
    num=int(string[i:j+1], 10)
    
    return [num, i, j, row]

def part1(data, characters):
    used_nums = []
    ans = 0
    for row in tqdm(range(len(data))):
        for column in range(len(data[row])):
            if data[row][column] in characters:
                if row - 1 >= 0:
                    if column - 1 >= 0 and data[row - 1][column-1].isdigit():
                        entry = concat_num(data[row - 1], column-1, row - 1)
                        if entry not in used_nums:
                            used_nums.append(entry)

                    if data[row - 1][column].isdigit():
                        entry = concat_num(data[row - 1], column, row - 1)
                        if entry not in used_nums:
                            used_nums.append(entry)

                    if column + 1 <= len(data[row - 1]) and data[row - 1][column+1].isdigit():
                        entry = concat_num(data[row - 1], column+1, row - 1)   
                        if entry not in used_nums:
                            used_nums.append(entry)

                # Check same row
                if column - 1 >= 0 and data[row][column-1].isdigit():
                    entry = concat_num(data[row], column-1, row)
                    if entry not in used_nums:
                            used_nums.append(entry)

                if column + 1 <= len(data[row]) and data[row][column+1].isdigit():
                    entry = concat_num(data[row], column+1, row)   
                    if entry not in used_nums:
                            used_nums.append(entry)

                # Check lower row
                if row +1 <= len(data)-1: 
                    if column - 1 >= 0 and data[row + 1][column-1].isdigit():
                        entry = concat_num(data[row + 1], column-1, row + 1)
                        if entry not in used_nums:
                            used_nums.append(entry)

                    if data[row + 1][column].isdigit():
                        entry = concat_num(data[row + 1], column, row + 1)
                        if entry not in used_nums:
                            used_nums.append(entry)

                    if column + 1 <= len(data[row + 1]) and data[row + 1][column+1].isdigit():
                        entry = concat_num(data[row + 1], column+1, row + 1)   
                        if entry not in used_nums:
                            used_nums.append(entry)

    valid_nums = [num[0] for num in used_nums]

    ans = sum(valid_nums)

    return ans

def part2(data, characters):
    used_nums = []
    ans = 0

    for row in tqdm(range(len(data))):
        for column in range(len(data[row])):
            if data[row][column] in characters:
                adj_nums = []
                if row - 1 >= 0:
                    if column - 1 >= 0 and data[row - 1][column-1].isdigit():
                        entry = concat_num(data[row - 1], column-1, row - 1)
                        if entry not in used_nums:
                            used_nums.append(entry)
                            adj_nums.append(entry[0])

                    if data[row - 1][column].isdigit():
                        entry = concat_num(data[row - 1], column, row - 1)
                        if entry not in used_nums:
                            used_nums.append(entry)
                            adj_nums.append(entry[0])

                    if column + 1 <= len(data[row - 1]) and data[row - 1][column+1].isdigit():
                        entry = concat_num(data[row - 1], column+1, row - 1)   
                        if entry not in used_nums:
                            used_nums.append(entry)
                            adj_nums.append(entry[0])

                # Check same row
                if column - 1 >= 0 and data[row][column-1].isdigit():
                    entry = concat_num(data[row], column-1, row)
                    if entry not in used_nums:
                            used_nums.append(entry)
                            adj_nums.append(entry[0])

                if column + 1 <= len(data[row]) and data[row][column+1].isdigit():
                    entry = concat_num(data[row], column+1, row)   
                    if entry not in used_nums:
                            used_nums.append(entry)
                            adj_nums.append(entry[0])

                # Check lower row
                if row +1 <= len(data)-1: 
                    if column - 1 >= 0 and data[row + 1][column-1].isdigit():
                        entry = concat_num(data[row + 1], column-1, row + 1)
                        if entry not in used_nums:
                            used_nums.append(entry)
                            adj_nums.append(entry[0])

                    if data[row + 1][column].isdigit():
                        entry = concat_num(data[row + 1], column, row + 1)
                        if entry not in used_nums:
                            used_nums.append(entry)
                            adj_nums.append(entry[0])

                    if column + 1 <= len(data[row + 1]) and data[row + 1][column+1].isdigit():
                        entry = concat_num(data[row + 1], column+1, row + 1)   
                        if entry not in used_nums:
                            used_nums.append(entry)
                            adj_nums.append(entry[0])
                
                if len(adj_nums) == 2: ans += (adj_nums[0]*adj_nums[1])
            

    # valid_nums = [num[0] for num in used_nums]

    # ans = sum(valid_nums)

    return ans
    

    return ans


def main():
    file_name = "data/day4.txt"
    characters = list(r"""`~!@#$%^&*()_-+={[}}|\:;"'<,>?/""") # From strings.punctuation

    with open(file_name) as f:
        data = f.readlines()
    
    refined_data =[line.replace("\n","") for line in data]
    print(f"Part 1 answer: {part1(refined_data, characters)}")
    # characters = list(r"""*""")
    # print(f"Part 2 answer: {part2(refined_data, characters)}")

if __name__ == "__main__":
    main()