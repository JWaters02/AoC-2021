import time
import fileinput

def middle(pos):
    return pos[len(pos) // 2]

def fuel_usage(pos, middle):
    # fuel_usage = 0
    # for x in pos:
    #     fuel_usage += sum(abs(x - middle))
    return sum(abs(x - middle) for x in pos)

def part1(pos):
    print(fuel_usage(pos, middle(pos)))

def part2(pos):
    def fuel_cost(move):
        return move * (move + 1) // 2
    
    middle = pos[len(pos) // 2] 
    fuel_usage = sum(fuel_cost(abs(x - middle)) for x in pos)

    for middle in range(min(pos), max(pos) + 1):
        fuel_usage = min(fuel_usage, sum(fuel_cost(abs(x - middle)) for x in pos))
    print(fuel_usage)

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