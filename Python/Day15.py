import time

def dijkstra(grid):
    queue = [(0, 0, 0)]
    visited = {}
    while True:
        current_node, x, y = queue[0]
        if x == len(grid) - 1 and y == len(grid[0]) - 1: 
            return current_node
        queue.pop(0)
        for dx, dy in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
            if 0 <= dx < len(grid) and 0 <= dy < len(grid[0]):
                if (dx, dy) not in visited or visited[(dx, dy)] > current_node + grid[dx][dy]:
                    visited[(dx, dy)] = current_node + grid[dx][dy]
                    queue.append((visited[(dx, dy)], dx, dy))
        queue = sorted(queue)

def part1(grid):
    return dijkstra(grid)

def part2(grid):
    thicc_grid = [[0 for _ in range(5 * len(grid[0]))] for _ in range(5 * len(grid))]
    for x in range(len(thicc_grid)):
        for y in range(len(thicc_grid[0])):
            distance = x // len(grid) + y // len(grid[0])
            new_cell = grid[x % len(grid)][y % len(grid[0])]
            for _ in range(distance):
                new_cell += 1
                if new_cell > 9: new_cell = 1
            thicc_grid[x][y] = new_cell
    return dijkstra(thicc_grid)

def main():
    grid = [[int(y) for y in x] for x in open('./Input/Day15.txt').read().strip().split('\n')]
    print(part1(grid))
    print(part2(grid))

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))