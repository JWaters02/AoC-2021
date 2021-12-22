import time
import fileinput
from functools import lru_cache

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

@lru_cache(maxsize=None)
def part2(r1, r2, p1, p2):
    if p1 >= 21: return [1, 0] 
    if p2 >= 21: return [0, 1]
    
    wins = [0, 0]
    for uni1 in range(1, 4):
        for uni2 in range(1, 4):
            for uni3 in range(1, 4):
                roll = (r1 + uni1 + uni2 + uni3 - 1) % 10 + 1
                p1_pos = p1 + roll
                next_uni = part2(r2, roll, p2, p1_pos)
                wins = [wins[0] + next_uni[1], wins[1] + next_uni[0]]
    return wins

def main():
    lines = [line for line in fileinput.input("./Input/Day21.txt")]
    p1 = lines[0].split(': ')[1].strip()
    p2 = lines[1].split(': ')[1].strip()
    print(part1(int(p1), int(p2)))
    print(max(part2(int(p1), int(p2), 0, 0)))

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))