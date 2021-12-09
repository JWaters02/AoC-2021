import time
import fileinput

def part1(lines):
    count = 0
    for line in lines:
        line = line.strip()
        line = line.split(" | ")[1]
        count += sum(1 for word in line.split() if len(word) in [2, 3, 4, 7])
    print(count)

def part2(lines):
    count = 0
    for line in lines:
        key, digits = [[set(x) for x in string.split()] for string in line.split(' | ')]
        numbers = {}
        numbers[4] = next(x for x in key if len(x) == 4)
        key.remove(numbers[4])
        numbers[8] = next(x for x in key if len(x) == 7)
        key.remove(numbers[8])
        numbers[1] = next(x for x in key if len(x) == 2)
        key.remove(numbers[1])
        numbers[7] = next(x for x in key if len(x) == 3)
        key.remove(numbers[7])
        numbers[9] = next(x for x in key if len(x ^ (numbers[7] | numbers[4])) == 1)
        key.remove(numbers[9])
        numbers[0] = next(x for x in key if numbers[1] < x and len(x) == 6)
        key.remove(numbers[0])
        numbers[6] = next(x for x in key if len(x) == 6)
        key.remove(numbers[6])
        numbers[3] = next(x for x in key if numbers[1] < x and len(x) == 5)
        key.remove(numbers[3])
        numbers[5] = next(x for x in key if len(numbers[9] - x) == 1)
        key.remove(numbers[5])
        numbers[2] = key.pop()
        count += int(''.join(str(next(key for key, value in numbers.items() if number == value)) for number in digits))
    print(count)

def main():
    lines = [line for line in fileinput.input("./Input/Day8.txt")]
    part1(lines)
    part2(lines)

if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    print("--- %s seconds ---" % (time.perf_counter() - start_time))