import time
import fileinput
from collections import defaultdict

def part1(starting_ages):
    out = []
    for i in starting_ages:
        if i > 0:
            out.append(i - 1)
        else:
            out.extend([6, 8])
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

def main():
    lines = [line for line in fileinput.input("./Input/Day6.txt")]
    starting_ages = list(map(int, lines[0].split(",")))
    for _ in range(80):
        starting_ages = part1(starting_ages)
    print(len(starting_ages))
    print(part2(starting_ages))

if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    print("--- %s seconds ---" % (time.perf_counter() - start_time))