import time
import fileinput

def part1(p1, p2):
    dice = 0
    players = [p1, p2]
    scores = [0, 0]
    while scores[0] < 1000 and scores[1] < 1000:
        for i in range(2):
            dice += 3
            players[i] = (players[i] + (3 * dice - 3) - 1) % 10 + 1
            scores[i] += players[i]
    return (scores[0] if scores[0] < scores[1] else scores[1] - players[1]) * (dice - 3)

def part2(lines):
    pass

def main():
    lines = [line for line in fileinput.input("./Input/Day21.txt")]
    p1 = lines[0].split(': ')[1].strip()
    p2 = lines[1].split(': ')[1].strip()
    print(part1(int(p1), int(p2)))

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))