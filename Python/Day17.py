import time

x1, x2, y1, y2 = 281, 311, -74, -54

def is_in_target(x, y):
    return (x1 <= x <= x2) and (y1 <= y <= y2)

def part2(dx, dy):
    x, y = 0, 0
    while x <= x2 and y >= y1:
        if is_in_target(x, y): return True
        x += dx
        y += dy
        if dx > 0: dx -= 1
        dy -= 1
    return False

def part1(n):
    return n * (n + 1) // 2

def main():
    print("Part 1: {}".format(part1(y1)))
    print("Part 2: {}".format(sum(part2(dx,dy)
                        for dx in range(x2+1) for dy in range(y1,-y1+1))))

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))