import time
import fileinput
from collections import defaultdict

def count_cells(grid):
    cell_count = 0
    for _, value in grid.items():
        if value > 1:
            cell_count += 1
    return cell_count

def part1(lists):
    grid = defaultdict(int)
    for line in lists:
        x1, y1 = line[0][0], line[0][1]
        x2, y2 = line[1][0], line[1][1]
        if x1 == x2:
            if y1 < y2:
                for y in range(y1, y2 + 1):
                    grid[(x1, y)] += 1
            else:
                for y in range(y2, y1 + 1):
                    grid[(x1, y)] += 1
        elif y1 == y2:
            if x1 < x2:
                for x in range(x1, x2 + 1):
                    grid[(x, y1)] += 1
            else:
                for x in range(x2, x1 + 1):
                    grid[(x, y1)] += 1
    print(count_cells(grid))

def part2(lists):
    grid = defaultdict(int)
    for line in lists:
        x1, y1 = line[0][0], line[0][1]
        x2, y2 = line[1][0], line[1][1]
        dx = 1 if x2 > x1 else -1
        dy = 1 if y2 > y1 else -1
        if x1 == x2:
            dx = 0
        elif y1 == y2:
            dy = 0
        grid[(x1, y1)] += 1
        while x1 != x2 or y1 != y2:
            x1 += dx
            y1 += dy
            grid[(x1, y1)] += 1
    print(count_cells(grid))

def main():
    lines = [line for line in fileinput.input("./Input/Day5.txt")]
    lists = []
    for line in lines:
        line = line.strip()
        line = line.split(" -> ")
        line = [(int(line[0].split(",")[0]), int(line[0].split(",")[1])), (int(line[1].split(",")[0]), int(line[1].split(",")[1]))]
        lists.append(line)
    part1(lists)
    part2(lists)

if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    print("--- %s seconds ---" % (time.perf_counter() - start_time))