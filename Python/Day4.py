import time

def check_grid(grid, current_draw):
    for row in range(len(grid)):
        if all(grid[row][col] in current_draw for col in range(len(grid))):
            return True
        if all(grid[col][row] in current_draw for col in range(len(grid))):
            return True
    return False

def check_last_win(grids, drawn):
    winning = None
    winning_draws = None
    wins = []
    for i in range(1, len(drawn)):
        current_draw = set(drawn[:i])
        for check, grid in enumerate(grids):
            if check in wins:
                continue
            if check_grid(grid, current_draw):
                wins.append(check)
                winning = grid
                winning_draws = drawn[:i]
                if len(wins) == len(grids):
                    return winning, winning_draws

def check_winning(grids, drawn):
    winning = None
    winning_draws = None
    for i in range(1, len(drawn)):
        current_draw = set(drawn[:i])
        for grid in grids:
            if check_grid(grid, current_draw):
                winning = grid
                winning_draws = drawn[:i]
                return winning, winning_draws

def get_not_called(winning, winning_draws):
    not_called = 0
    for i in range(5):
        for j in range(5):
            if winning[i][j] not in winning_draws:
                not_called += winning[i][j]
    return not_called

def part1(lines):
    drawn, grids = lines[0], lines[1:]
    drawn = [int(x) for x in drawn.split(",")]
    grids = [[[int(item) for item in row.split()] for row in grid.strip().split("\n")] for grid in grids]
    winning, winning_draws = check_winning(grids, drawn)
    print(get_not_called(winning, winning_draws) * winning_draws[-1])

def part2(lines):
    drawn, grids = lines[0], lines[1:]
    drawn = [int(x) for x in drawn.split(",")]
    grids = [[[int(item) for item in row.split()] for row in grid.strip().split("\n")] for grid in grids]
    winning, winning_draws = check_last_win(grids, drawn)
    print(get_not_called(winning, winning_draws) * winning_draws[-1])

def main():
    lines = open("./Input/Day4.txt").read().split("\n\n")
    part1(lines)
    part2(lines)

if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    print("--- %s seconds ---" % (time.perf_counter() - start_time))