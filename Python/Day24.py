import time
import fileinput

def solve(blocks):
    max, min = [None] * 14, [None] * 14
    stack = []
    for i, block in enumerate(blocks):
        if block[3] == 'div z 1': stack.append((i, int(block[14].split(' ')[-1])))
        elif block[3] == 'div z 26':
            w, x = stack.pop()
            difference = x + int(block[4].split(' ')[-1])
            if difference < 0: i, w, difference = w, i, -difference
            max[i], min[i], max[w], min[w] = 9, 1 + difference, 9 - difference, 1
    print(''.join(map(str, max)))
    print(''.join(map(str, min)))

def main():
    lines = [line.strip() for line in fileinput.input("./Input/Day24.txt")]
    blocks = []
    for i, line in enumerate(lines):
        if line.startswith("inp w"): blocks.append(lines[i+1:i+18])
    solve(blocks)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))