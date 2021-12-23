import fileinput
import time
from collections import defaultdict

def get_matches(scanner_beacons, scanner):
    global known_beacons
    for rotation in range(24):
        translation = get_rotations(scanner_beacons, scanner, rotation)
        if translation: return rotation, translation
    return -1, -1

def get_rotations(scanner_beacons, scanner, rotation):
    global known_beacons
    matches = defaultdict(int)
    for beacon_0 in known_beacons:
        x0, y0, z0 = beacon_0
        for beacon_s in scanner_beacons[scanner]:
            xs, ys, zs = get_transform(beacon_s, rotation)
            dx, dy, dz = x0 - xs, y0 - ys, z0 - zs
            matches[dx, dy, dz] += 1
    best_match = max(matches.values())
    if best_match < 12: return
    for key, value in matches.items():
        if value == best_match: return key

def get_transform(coordinates, rotation, translation=(0,0,0)):
    x,  y,  z  = coordinates
    dx, dy, dz = translation
    
    # Face forward
    if   rotation == 0:  tx, ty, tz =  x,  y,  z
    elif rotation == 1:  tx, ty, tz = -y,  x,  z
    elif rotation == 2:  tx, ty, tz = -x, -y,  z
    elif rotation == 3:  tx, ty, tz =  y, -x,  z
    
    # Face left
    elif rotation == 4:  tx, ty, tz =  z,  y, -x
    elif rotation == 5:  tx, ty, tz =  z,  x,  y
    elif rotation == 6:  tx, ty, tz =  z, -y,  x
    elif rotation == 7:  tx, ty, tz =  z, -x, -y
    
    # Face back
    elif rotation == 8:  tx, ty, tz = -x,  y, -z
    elif rotation == 9:  tx, ty, tz = -y, -x, -z
    elif rotation == 10: tx, ty, tz =  x, -y, -z
    elif rotation == 11: tx, ty, tz =  y,  x, -z
    
    # Face right
    elif rotation == 12: tx, ty, tz = -z,  y,  x
    elif rotation == 13: tx, ty, tz = -z,  x, -y
    elif rotation == 14: tx, ty, tz = -z, -y, -x
    elif rotation == 15: tx, ty, tz = -z, -x,  y
    
    # Face up
    elif rotation == 16: tx, ty, tz =  x,  z, -y
    elif rotation == 17: tx, ty, tz = -y,  z, -x
    elif rotation == 18: tx, ty, tz = -x,  z,  y
    elif rotation == 19: tx, ty, tz =  y,  z,  x
    
    # Face down
    elif rotation == 20: tx, ty, tz =  x, -z,  y
    elif rotation == 21: tx, ty, tz =  y, -z, -x
    elif rotation == 22: tx, ty, tz = -x, -z, -y
    elif rotation == 23: tx, ty, tz = -y, -z,  x
    
    # apply translation
    tx, ty, tz = tx + dx, ty + dy, tz + dz
    return (tx, ty, tz)

def get_max_distance(scanner_coord):
    max_distance = 0
    for a in scanner_coord:
        for b in scanner_coord:
            if a >= b: continue
            max_distance = max(max_distance, manhattan_distance(a, b))
    return max_distance

def manhattan_distance(a, b):
    ax, ay, az = a
    bx, by, bz = b
    dx = abs(ax - bx)
    dy = abs(ay - by)
    dz = abs(az - bz)
    distance = dx + dy + dz
    return distance

def detect_scanners(scanner_beacons):
    global known_beacons
    known_beacons = set(scanner_beacons[0])
    scanners_to_find = set(range(1, len(scanner_beacons)))
    scanner_coord = [(0,0,0)] * (len(scanner_beacons) + 1)
    
    while len(scanners_to_find):
        scanners_this_pass = set(scanners_to_find)
        for scanner in scanners_this_pass:
            rotation, translation = get_matches(scanner_beacons, scanner)
            if rotation < 0: continue
            scanners_to_find.remove(scanner)
            for beacon in scanner_beacons[scanner]:
                known_beacons.add(get_transform(beacon, rotation, translation))
            scanner_coord[scanner] = translation
    return len(known_beacons), get_max_distance(scanner_coord)

def main():
    lines = [line.strip() for line in fileinput.input("./Input/Day19.txt")]
    scanners = []
    for line in lines:
        if line[0:3] == '---': scans = []
        elif len(line) == 0: scanners.append(scans)
        else:
            beacon = line.split(',')
            beacon = list(map(int,beacon))
            scans.append(tuple(beacon))
    scanners.append(scans)
    print(detect_scanners(scanners))

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))