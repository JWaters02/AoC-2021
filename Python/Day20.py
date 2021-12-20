import time
import fileinput

def get_neighbours(x, y):
    return [
        (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
        (x - 1, y    ), (x, y    ), (x + 1, y    ),
        (x - 1, y + 1), (x, y + 1), (x + 1, y + 1),
    ]

def get_bit(x, y, pixels, boundary, outside_on):
    if outside_on: return '1' if (x, y) in pixels or (x, y) not in boundary else '0'
    else: return '1' if (x, y) in pixels else '0'

def enhance(iea, pixels, outside_on):
    new_pixels = set()
    min_x = min([p[0] for p in pixels])
    min_y = min([p[1] for p in pixels])
    max_x = max([p[0] for p in pixels])
    max_y = max([p[1] for p in pixels])
    boundary = {(x, y) for x in range(min_x, max_x + 1) for y in range(min_y, max_y + 1)}
    for y in range(min_y - 1, max_y + 2):
        for x in range(min_x - 1, max_x + 2):
            s = ''.join([get_bit(x2, y2, pixels, boundary, outside_on) for (x2, y2) in get_neighbours(x, y)])
            b = int(s, 2)
            if iea[b] == '#': new_pixels.add((x, y))
    return new_pixels

def part1(iea, pixels):
    pixels = enhance(iea, pixels, False)
    pixels = enhance(iea, pixels, True)
    return len(pixels)

def part2(iea, pixels):
    for i in range(50):
        if i % 2 == 1: pixels = enhance(iea, pixels, True)
        else: pixels = enhance(iea, pixels, False)
    return len(pixels)

def main():
    lines = [line.strip() for line in fileinput.input("./Input/Day20.txt")]
    iea = lines[0]
    image = lines[2:]

    pixels = set()
    for y, row in enumerate(image):
        for x, cell in enumerate(row):
            if cell == '#': pixels.add((x, y))
    
    print("Part 1:", part1(iea, pixels))
    print("Part 2:", part2(iea, pixels))

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))