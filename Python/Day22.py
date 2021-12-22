import time
import fileinput
import re

def execute(grid, cuboid):
    if cuboid[0] == 'on':
        for x in cuboid[1][0]:
            for y in cuboid[1][1]:
                for z in cuboid[1][2]:
                    grid.add((x, y, z))
    elif cuboid[0] == 'off':
        for x in cuboid[1][0]:
            for y in cuboid[1][1]:
                for z in cuboid[1][2]:
                    grid.discard((x, y, z))

def volume(cube):
    volume = 1
    for range in cube: volume *= len(range)
    return volume

def overlaps(range1, range2):
    if range1.start <= range2.start < range1.stop or range2.start <= range1.start < range2.stop or range1.start < range2.stop <= range1.stop or range2.start < range1.stop <= range2.stop:
        overlapping = sorted([range1.start, range1.stop - 1, range2.start, range2.stop - 1])
        return range(overlapping[1], overlapping[2] + 1)
    return range(0, 0)

def intersection(cube1, cube2):
    intersections = []
    for range1, range2 in zip(cube1, cube2):
        if not overlaps(range1, range2): return []
        intersections.append(overlaps(range1, range2))
    return intersections

def part1(cuboids):
    grid = set()
    for step in cuboids:
        if step[1][0].start in range(-50, 51): execute(grid, step)
    return len(grid)

def part2(cuboids):
    ons, offs, onsv = [], [], 0
    for state, cube in cuboids:
        on, off = len(ons), len(offs)
        if state == 'on':
            onsv += volume(cube)
            ons.append(cube)
        for i in range(on):
            intersecting = intersection(cube, ons[i])
            if intersecting:
                offs.append(intersecting)
                onsv -= volume(intersecting)
        for i in range(off):
            intersecting = intersection(cube, offs[i])
            if intersecting:
                onsv += volume(intersecting)
                ons.append(intersecting)
    return onsv

def main():
    lines = [line.strip() for line in fileinput.input("./Input/Day22.txt")]
    exp = re.compile(r'(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)')
    cuboids = []
    for line in lines:
        state = exp.findall(line)[0][0]
        coords = exp.findall(line)[0][1:]
        coords = [range(int(coords[i]), int(coords[i+1])+1) for i in range(0, len(coords), 2)]
        cuboids.append((state, coords))
    
    # print(part1(cuboids))
    print(part2(cuboids))

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))