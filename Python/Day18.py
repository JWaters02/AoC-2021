import time
import fileinput
from functools import reduce
from itertools import permutations
from math import floor, ceil

def explode_reduction(snailfish_num):
    for i, ((left, dleft), (right, dright)) in enumerate(zip(snailfish_num, snailfish_num[1:])):
        if dleft < 5 or dleft != dright: continue
        if i > 0: snailfish_num[i-1][0] += left
        if i < len(snailfish_num) - 2: snailfish_num[i+2][0] += right
        return True, snailfish_num[:i] + [[0, dleft-1]] + snailfish_num[i+2:]
    return False, snailfish_num

def split_reduction(snailfish_num):
    for i, (num, depth) in enumerate(snailfish_num):
        if num < 10: continue
        return True, snailfish_num[:i] + [[floor(num / 2.0), depth+1], [ceil(num / 2.0), depth+1]] + snailfish_num[i+1:]
    return False, snailfish_num

def add_snailfish_nums(left, right):
    new_num = [[num, depth+1] for num, depth in left+right]
    while True:
        reduction, new_num = explode_reduction(new_num)
        if reduction: continue
        reduction, new_num = split_reduction(new_num)
        if not reduction: break
    return new_num

def calculate_magnitude(snailfish_num):
    if len(snailfish_num) > 1:
        for i, ((left, dleft), (right, dright)) in enumerate(zip(snailfish_num, snailfish_num[1:])):
            if dleft != dright: continue
            inner_magnitude = left * 3 + right * 2
            snailfish_num = snailfish_num[:i] + [[inner_magnitude, dleft-1]] + snailfish_num[i+2:]
            return calculate_magnitude(snailfish_num)
    return snailfish_num[0][0]

def remove_brackets(lines):
    final_list = []
    for line in lines:
        this_line, depth = [], 0
        for character in line:
            if character == '[': depth += 1
            elif character == ']': depth -= 1
            elif character.isdigit(): this_line.append([int(character), depth])
        final_list.append(this_line)
    return final_list

def part1(lines):
    return calculate_magnitude(reduce(add_snailfish_nums, lines))

def part2(lines):
    return max(calculate_magnitude(add_snailfish_nums(left, right)) for left, right in permutations(lines, 2))

def main():
    lines = [line for line in fileinput.input("./Input/Day18.txt")]
    lines = remove_brackets(lines)
    print("Part 1: {}".format(part1(lines)))
    print("Part 2: {}".format(part2(lines)))

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))