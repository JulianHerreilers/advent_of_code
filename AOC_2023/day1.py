import re

def part1(file_name):
    ans = []
    with open(file_name, "r") as f:
        data = f.readlines()

    for line in data:
        nums = (re.findall(r'\d+', line))
        if len(nums)>0:
            ans.append(int(2*nums[0][0])) if len(nums) == 1 else ans.append(int(nums[0][0]+nums[-1][-1]))

    return sum(ans)

def part2(file_name):
    ans = []
    with open(file_name, "r") as f:
        data = f.readlines()
        
    list_nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for line in data:
        nums = []
        for i in range(0,len(line)):
            for num in list_nums:
                if num in line[i:i+len(num)]:
                    nums.append(str(list_nums.index(num)+1)) if list_nums.index(num)<9 else nums.append(num)
                    i += len(nums)
                    
        ans.append(int(2*nums[0])) if len(nums) == 0 else ans.append(int(nums[0]+nums[-1]))


    return sum(ans)

def main():
    data_file = "data_day1.txt"
    ans = part1(data_file)
    print(f"Part one: {ans}")
    ans = part2(data_file)
    print(f"Part Two: {ans}")

if __name__ == "__main__":
    main()
