import time
import fileinput
from collections import defaultdict

def part1(starting_ages):
    out = []
    iterations = 0
    for i in starting_ages:
        iterations += 1
        if i > 0:
            out.append(i - 1)
        else:
            out.extend([6, 8])
    print(iterations)
    return out

def part2(starting_ages):
    age_count = defaultdict(int)
    for fish in starting_ages:
        age_count[fish] += 1

    for _ in range(256):
        n = defaultdict(int)
        for age, count in age_count.items():
            if age > 0: n[age - 1] += count
            else: 
                n[6] += count 
                n[8] += count
        age_count = n
    return sum(age_count.values())

def count_fish(starting_ages, iterations):
    fish = []
    for i in range(9):
        fish.append(starting_ages.count(i))
    for _ in range(iterations):
        num = fish.pop(0)
        fish[6] += num
        fish.append(num)
    return sum(fish)

def main():
    lines = [line for line in fileinput.input("./Input/Day6.txt")]
    starting_ages = list(map(int, lines[0].split(",")))
    print(f"Part 1: {count_fish(starting_ages, 80)}")
    print(f"Part 2: {count_fish(starting_ages, 256)}")

if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    print("--- %s seconds ---" % (time.perf_counter() - start_time))