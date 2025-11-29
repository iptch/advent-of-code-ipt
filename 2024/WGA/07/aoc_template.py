# aoc_template.py

import pathlib
import sys

def calc(puzzle_part, test_value, numbers, result):
    if len(numbers) == 0:
        return result == test_value
    
    has_solution_sum = None
    has_solution_product = None
    has_solution_concat = None

    sum = result + numbers[0]
    if sum <= test_value:
        has_solution_sum = calc(puzzle_part, test_value, numbers[1:], sum)

    product = result * numbers[0]
    if product <= test_value:
        has_solution_product = calc(puzzle_part, test_value, numbers[1:], product)

    if puzzle_part == 2:
        concat = int(str(result) + str(numbers[0]))
        if product <= test_value:
            has_solution_concat = calc(puzzle_part, test_value, numbers[1:], concat)

    if has_solution_sum or has_solution_product or has_solution_concat:
        return True

def parse(puzzle_input):
    """Parse input."""
    return [(int(test_value), [int(i) for i in numbers.split()]) for test_value, numbers in [row.split(": ") for row in puzzle_input.splitlines()]]

def part1(data):
    """Solve part 1."""
    return sum([test_value for test_value, numbers in data if calc(1, test_value, numbers[1:], numbers[0])])

def part2(data):
    """Solve part 2."""
    return sum([test_value for test_value, numbers in data if calc(2, test_value, numbers[1:], numbers[0])])

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