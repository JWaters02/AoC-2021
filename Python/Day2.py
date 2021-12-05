import time
import fileinput

def part1(lines):
    horizontalD, depth = 0, 0
    for line in lines:
        line.strip("\n")
        instruction, distance = line.split()
        distance = int(distance)
        if instruction == "forward":
            horizontalD = horizontalD + distance
        elif instruction == "down":
            depth = depth + distance
        elif instruction == "up":
            depth = depth - distance
    print(f"Part 1: {horizontalD * depth}")

def part2(lines):
    horizontalD, depth, aim = 0, 0, 0
    for line in lines:
        line.strip("\n")
        instruction, distance = line.split()
        distance = int(distance)
        if instruction == "forward":
            horizontalD = horizontalD + distance
            depth = depth + (aim * distance)
        elif instruction == "down":
            aim = aim + distance
        elif instruction == "up":
            aim = aim - distance
    print(f"Part 2: {horizontalD * depth}")

def main():
    lines = [line for line in fileinput.input("./Input/Day2.txt")]
    part1(lines)
    part2(lines)

if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    print("--- %s seconds ---" % (time.perf_counter() - start_time))