# aoc_template.py

import pathlib
import sys

def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

def has_smudge(row1, row2):
    counter = 0

    for x1, x2 in zip(row1, row2):
        if x1 != x2:
            if counter > 0: return False
            counter += 1

    if counter == 1:
        return True
    
    return False

def has_reflection(i, pattern, puzzle_part):
    counter = 0

    for row1, row2 in zip(reversed(pattern[:i+1]), pattern[i+1:]):
        if puzzle_part == 2 and has_smudge(row1, row2):
            if counter > 0: return False
            counter += 1
        elif row1 != row2:
            return False

    if puzzle_part == 2 and counter != 1:
        return False
       
    return True

def get_reflection(pattern, puzzle_part):
    for i in range(len(pattern)-1):
        if has_reflection(i, pattern, puzzle_part):
            return i + 1

    return 0

def parse(puzzle_input):
    """Parse input."""
    return [[row for row in pattern.splitlines()] for pattern in puzzle_input.split("\n\n")]

def part1(data):
    """Solve part 1."""
    sum = 0

    for pattern in data:
        h_reflection = get_reflection(pattern, 1)
        v_reflection = get_reflection(transpose(pattern), 1)

        sum += v_reflection + 100 * h_reflection

    return sum

def part2(data):
    """Solve part 2."""
    sum = 0

    for pattern in data:
        h_reflection = get_reflection(pattern, 2)
        v_reflection = get_reflection(transpose(pattern), 2)

        sum += v_reflection + 100 * h_reflection

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