import time
import fileinput

def part1(lines):
    pass

def part2(lines):
    pass

def main():
    lines = [line for line in fileinput.input("./Input/Day8.txt")]
    part1(lines)
    part2(lines)

if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    print("--- %s seconds ---" % (time.perf_counter() - start_time))