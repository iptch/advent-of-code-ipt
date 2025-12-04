# aoc_template.py

import pathlib
import sys

def can_access(x, y, map):
    n = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if (not (i == 0 and j == 0) and
                 x + i >= 0 and x + i < len(map) and
                 y + j >= 0 and y + j < len(map[0]) and
                 map[x+i][y+j] == "@"):
                    n += 1

                    if n >= 4:
                        return False
                    
    return True

def parse(puzzle_input):
    """Parse input."""

    return puzzle_input.splitlines()

def part1(data):
    """Solve part 1."""
    sum = 0
    map = [[cell for cell in row] for row in data]

    for x, row in enumerate(data):
        for y, cell in enumerate(row):
            if cell == "@" and can_access(x, y, data):
                map[x][y] = "x"
                sum += 1

    return sum

def part2(data):
    """Solve part 2."""
    sum = 0
    map = [[cell for cell in row] for row in data]

    for _ in range(1000):
        sum_prev = sum

        for x, row in enumerate(map):
            for y, cell in enumerate(row):
                if cell == "@" and can_access(x, y, map):
                    map[x][y] = "x"
                    sum += 1

        if sum == sum_prev:
            break

    return sum

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))