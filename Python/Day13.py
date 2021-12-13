import time
import fileinput

def part1(folds, coords):
    for i, fold in enumerate(folds):
        direction, location = fold[0], fold[2:]
        location = int(location)
        points = set()
        for (x, y) in coords:
            if direction == "x":
                if x < location: points.add((x, y))
                else: points.add((location - (x - location), y))
            elif direction == "y":
                if y < location: points.add((x, y))
                else: points.add((x, location - (y - location)))
        coords = points
        if i == 0:
            print(len(coords))
    part2(coords)

def part2(coords):
    grid = []
    for _ in range(6):
        grid.append(list("." * 39))
    for (x, y) in coords:
        grid[y][x] = "#"
    print("\n".join(["".join(x) for x in grid]))

def main():
    lines = [line.strip() for line in fileinput.input("./Input/Day13.txt")]
    fold_instructions = lines[-12:]
    folds = [instructions.split()[2] for instructions in fold_instructions]
    dots = lines[:-14]
    coords = [[int(x) for x in dots[y].split(",")] for y in range(len(dots))]
    part1(folds, coords)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))