import time
import fileinput

def part1(template, pairs):
    polymerRules = {pair[:2]: pair[6] for pair in pairs}
    for _ in range(40):
        new_template = ""
        for i in range(len(template) - 1):
            new_template += template[i]
            new_template += polymerRules[template[i:i+2]]
        new_template += template[-1]
        template = new_template
        print(len(template))

    counts = {}
    for letter in template:
        if letter not in counts:
            counts[letter] = 0
        counts[letter] += 1
    print(counts[max(counts, key=counts.get)] - counts[min(counts, key=counts.get)])


def part2(lines):
    pass

def main():
    lines = [line.strip() for line in fileinput.input("./Input/Day14.txt")]
    template = lines[0]
    pairs = lines[2:]
    part1(template, pairs)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))