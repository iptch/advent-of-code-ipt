# aoc_template.py

import pathlib
import sys

def get_invalid_ids(ids, puzzle_part):
    invalid_ids = []

    for id in ids:
        max_reps = 2 if puzzle_part == 1 else len(id)

        for i in range(2, max_reps+1):
            quotient, remainder = divmod(len(id), i)

            if remainder == 0 and id[:quotient] * i == id:
                invalid_ids.append(int(id))
                break

    return invalid_ids

def parse(puzzle_input):
    """Parse input."""

    return [[str(num) for num in range(row[0], row[1]+1)] for row in [[int(id) for id in row.split("-")] for row in puzzle_input.split(",")]]

def part1(data):
    """Solve part 1."""

    return sum([sum(get_invalid_ids(row, 1)) for row in data])

def part2(data):
    """Solve part 2."""

    return sum([sum(get_invalid_ids(row, 2)) for row in data])

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