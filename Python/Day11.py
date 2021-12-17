import time

def get_adjacent_tiles(grid, x, y):
    tiles = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                if 0 <= x + i < len(grid) and 0 <= y + j < len(grid[x + i]):
                    tiles.append([x + i, y + j])
    return tiles

def step_1(grid):
    flashed = False
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            grid[x][y] += 1
            if grid[x][y] > 9:
                flashed = True
    return grid, flashed 

def step_2(grid, flashed):
    flash_count = []
    while flashed:
        flashed = False
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] > 9:
                    if [x, y] not in flash_count:
                        grid[x][y] = 0
                        flashed = True
                        flash_count.append([x, y])
                        for adjacent in get_adjacent_tiles(grid, x, y):
                            grid[adjacent[0]][adjacent[1]] += 1
    return flash_count

def step_3(grid, flashed, flashes):
    for cell in step_2(grid, flashed):
        grid[cell[0]][cell[1]] = 0
        flashes += 1
    return flashes

def part1(grid):
    flashes = 0
    for _ in range(100):
        grid, flashed = step_1(grid)
        flashes = step_3(grid, flashed, flashes)
    return flashes

def part2(grid):
    step = 0
    for _ in range(10000000000):
        step += 1
        flashes = 0
        grid, flashed = step_1(grid)
        flashes = step_3(grid, flashed, flashes)
        if flashes == 100:
            return step + 100

def main():
    grid = [[int(y) for y in x] for x in open('./Input/Day11.txt').read().strip().split('\n')]
    print(part1(grid))
    print(part2(grid))

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))