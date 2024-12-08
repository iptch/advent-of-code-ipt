# aoc_template.py

import pathlib
import sys

def calc(puzzle_part, numbers, test_value, value):
    if len(numbers) == 0:
        return value == test_value
    else:
        has_solution_sum = None
        has_solution_product = None
        has_solution_concat = None

        sum = value + numbers[0]
        if sum <= test_value:
            has_solution_sum = calc(puzzle_part, numbers[1:], test_value, sum)

        product = value * numbers[0]
        if product <= test_value:
            has_solution_product = calc(puzzle_part, numbers[1:], test_value, product)

        if puzzle_part == 2:
            concat = int(str(value) + str(numbers[0]))
            if product <= test_value:
                has_solution_concat = calc(puzzle_part, numbers[1:], test_value, concat)

        if has_solution_sum or has_solution_product or has_solution_concat:
            return True

def parse(puzzle_input):
    """Parse input."""
    return [
        [int(part[0]), [int(y) for y in part[1].split()]]
        for part in (row.split(": ") for row in puzzle_input.splitlines())
    ]

def part1(data):
    """Solve part 1."""
    sum = 0

    for row in data:
        if calc(1, row[1][1:], row[0], row[1][0]):
            sum += row[0]

    return sum

def part2(data):
    """Solve part 2."""
    sum = 0

    for row in data:
        if calc(2, row[1][1:], row[0], row[1][0]):
            sum += row[0]

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