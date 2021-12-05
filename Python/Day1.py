import time
import fileinput

def part1(nums):
    count = 0
    for i, num in enumerate(nums):
        if num > nums[i - 1]:
            count += 1
    return count

def part2(nums):
    count = 0
    for i, num in enumerate(nums):
        if num > nums[i - 3]:
            count += 1
    return count

def main():
    lines = [line for line in fileinput.input("./Input/Day1.txt")]
    nums = [int(line.strip()) for line in lines]
    print(f"Part 1: {part1(nums)}") 
    print(f"Part 2: {part2(nums)}")

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))