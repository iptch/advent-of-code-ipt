# aoc_template.py

import pathlib
import sys

def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

def multiply(numbers):
    prod = 1

    for number in numbers:
        prod *= number

    return prod

def parse(puzzle_input):
    """Parse input."""

    return puzzle_input.splitlines()

def part1(data):
    """Solve part 1."""
    problems = transpose([[x for x in row.split()] for row in data])
    problems = [(problem[:-1], problem[-1]) for problem in problems]
    
    res = 0

    for numbers, operation in problems:
        numbers = [int(number) for number in numbers]
        res += sum(numbers) if operation == "+" else multiply(numbers)
    
    return res

def part2(data):
    """Solve part 2."""
    cols = ["".join(symbol) for symbol in transpose([list(row[::-1]) for row in data])]
    cols = [col for col in cols if col.strip()] # Remove empty columns

    res = 0
    numbers = []

    for col in cols:
        numbers.append(int(col[:-1]))
        
        if col[-1] == "+":
            res += sum(numbers)
            numbers = []

        if col[-1] == "*":
            res += multiply(numbers)
            numbers = []
    
    return res

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))