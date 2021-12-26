import time

def step(grid):
    new_grid = list([y.copy() for y in grid])
    moved = False
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == '>':
                if y < len(grid[0]) - 1: loc = y + 1
                else: loc = 0
                if grid[x][loc] == '.':
                    new_grid[x][y] = '.'
                    new_grid[x][loc] = '>'
                    moved = True
    new_grid2 = list([y.copy() for y in new_grid])
    for x in range(len(new_grid)):
        for y in range(len(new_grid[0])):
            if new_grid[x][y] == 'v':
                if x < len(new_grid) - 1: loc = x + 1
                else: loc = 0
                if new_grid[loc][y] == '.':
                    new_grid2[x][y] = '.'
                    new_grid2[loc][y] = 'v'
                    moved = True
    return new_grid2, moved

def part1(grid):
    count = 0
    new = grid
    while True:
        new, moved = step(new)
        count += 1
        if not moved: break
    return count

def main():
    grid = [[y for y in x] for x in open('./Input/Day25.txt').read().strip().split('\n')]
    print(part1(grid))

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))