import time
import fileinput
from collections import Counter

def main():
    lines = [line for line in fileinput.input("./Input/Day3.txt")]
    print(part1(lines))
    print(part2(lines))

def part1(lines):
    gamma = ""
    epsilon = ""
    for i in range(12):
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
        type_order = []
        if type == 0:
            type_order = ["1", "0"]
        else:
            type_order = ["0", "1"]
        for i in range(12):
            counter_dict = Counter()
            for line in lines:
                counter_dict[line[i]] += 1
            if counter_dict["1"] >= counter_dict["0"]:
                lines = [x for x in lines if x[i] == type_order[0]]
            else:
                lines = [x for x in lines if x[i] == type_order[1]]
            if len(lines) == 1:
                return lines[0]
        return lines[0]
    print(int(get_rating(lines, 0), 2) * int(get_rating(lines, 1), 2))

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))