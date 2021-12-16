import time
import fileinput

matches = ["()", "{}", "[]", "<>"]
matches2 = {')': '(', ']': '[', '}': '{', '>': '<'}
points1 = {']': 57, ')': 3, '}': 1197, '>': 25137}
points2 = {'(': 1, '[': 2, '{': 3, '<': 4}

def part1(lines):
    score = 0
    for line in lines:
        stack = []
        for char in line:
            if char in '([{<':
                stack.append(char)
            elif char in ')]}>':
                last = stack[-1]
                if (last + char) in matches:
                    stack = stack[:-1]
                else:
                    score += points1[char]
                    break
    print(score)

def part2(lines):
    score = []
    for line in lines:
        stack = []
        corrupt = False
        for char in list(line.strip()):
            if char in '([{<':
                stack.append(char)
            elif stack.pop() not in matches2[char]:
                corrupt = True
                break
        if not corrupt:
            count = 0
            for char in stack[::-1]:
                count = 5 * count + points2[char]
            score.append(count)
    score = sorted(score)
    print(score[len(score) // 2])

def main():
    lines = [line for line in fileinput.input("./Input/Day10.txt")]
    part1(lines)
    part2(lines)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))