import time

def part1(grid):
    risk = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if i == 0 and j == 0:
                continue
            elif i > 0 and grid[i][j] >= grid[i-1][j]:
                continue
            elif i < len(grid) - 1 and grid[i][j] >= grid[i+1][j]:
                continue
            elif j > 0 and grid[i][j] >= grid[i][j-1]:
                continue
            elif j < len(grid[0]) - 1 and grid[i][j] >= grid[i][j+1]:
                continue
            else:
                risk += grid[i][j] + 1
    print(risk)

def depth_first_search(grid, visited, i, j):
    node = (i, j)
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return
    if node in visited or grid[i][j] == 9:
        return
    visited.add(node)
    depth_first_search(grid, visited, i-1, j)
    depth_first_search(grid, visited, i+1, j)
    depth_first_search(grid, visited, i, j-1)
    depth_first_search(grid, visited, i, j+1)

def part2(grid):
    visited = set()
    basins = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if (i, j) not in visited and grid[i][j] != 9:
                previous_node = len(visited)
                depth_first_search(grid, visited, i, j)
                basins.append(len(visited) - previous_node)
    basins.sort()
    print(basins[-1] * basins[-2] * basins[-3])

def main():
    grid = [[int(y) for y in x] for x in open('./Input/Day9.txt').read().strip().split('\n')]
    part1(grid)
    part2(grid)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))