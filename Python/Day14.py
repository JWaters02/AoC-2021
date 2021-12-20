import time
import fileinput
from collections import defaultdict

def part1():
    lines = [line.strip() for line in fileinput.input("./Input/Day14.txt")]
    template = lines[0]
    pairs = lines[2:]
    polymerRules = {pair[:2]: pair[6] for pair in pairs}

    for _ in range(10):
        new_template = ""
        for i in range(len(template) - 1):
            new_template += template[i]
            new_template += polymerRules[template[i:i+2]]
        new_template += template[-1]
        template = new_template

    counts = {}
    for letter in template:
        if letter not in counts:
            counts[letter] = 0
        counts[letter] += 1
    return counts[max(counts, key=counts.get)] - counts[min(counts, key=counts.get)]


def part2():
    template, pairs = open("./Input/Day14.txt").read().split('\n\n')
    template = {''.join(pair): 1 for pair in zip(template[:-1], template[1:])}
    pairs = dict(pair.split(' -> ') for pair in pairs.splitlines())
    pairs = {key: [key[0] + value, value + key[1]] for key, value in pairs.items()}

    for _ in range(40):
        new_template = defaultdict(int)
        for polymer, count in template.items():
            for pair in pairs[polymer]:
                new_template[pair] += count
        template = new_template
    count = defaultdict(int)
    for key, value in template.items():
        for char in key:
            count[char] += value
    quantities = sorted((item + 1) // 2 for item in count.values())
    return quantities[-1] - quantities[0]

def main():
    print("Part 1:", part1()) # Old, slow method
    print("Part 2:", part2()) # New, fast method

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))