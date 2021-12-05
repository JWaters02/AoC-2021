import time
import fileinput
from collections import Counter

def part1(lines):
    gamma = ""
    epsilon = ""
    for i in range(5):
        counter_dict = Counter()
        for line in lines:
            counter_dict[line[i]] += 1
        if counter_dict["1"] > counter_dict["0"]:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    print(int(gamma, 2) * int(epsilon, 2))

def part2(lines):
    def get_rating(lines, type):
        bit_criteria = []
        if type == 0:
            bit_criteria = ["1", "0"]
        else:
            bit_criteria = ["0", "1"]
        for i in range(5):
            counter_dict = Counter()
            for line in lines:
                counter_dict[line[i]] += 1
            if counter_dict["1"] >= counter_dict["0"]:
                lines = [x for x in lines if x[i] == bit_criteria[0]]
            else:
                lines = [x for x in lines if x[i] == bit_criteria[1]]
            if len(lines) == 1:
                return lines[0]
        return lines[0]
    print(int(get_rating(lines, 0), 2) * int(get_rating(lines, 1), 2))

def main():
    lines = [line for line in fileinput.input("./Input/Day3.txt")]
    part1(lines)
    part2(lines)

if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    print("--- %s seconds ---" % (time.perf_counter() - start_time))