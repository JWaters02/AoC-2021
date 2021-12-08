import time
import fileinput

def middle(pos):
    return pos[len(pos) // 2]

def fuel_cost(move):
    return move * (move + 1) // 2

def fuel_usage(pos, middle, part):
    if part == 1:
        return sum(abs(x - middle) for x in pos)
    else:
        return sum(fuel_cost(abs(x - middle)) for x in pos)

def part1(pos):
    print(fuel_usage(pos, middle(pos), 1))

def part2(pos):
    fuel_usages = fuel_usage(pos, middle(pos), 2)
    for middles in range(min(pos), max(pos) + 1):
        fuel_usages = min(fuel_usages, fuel_usage(pos, middles, 2))
    print(fuel_usages)

def main():
    lines = [line for line in fileinput.input("./Input/Day7.txt")]
    pos = list(map(int, lines[0].split(",")))
    pos.sort()
    part1(pos)
    part2(pos)

if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    print("--- %s seconds ---" % (time.perf_counter() - start_time))