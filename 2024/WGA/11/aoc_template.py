# aoc_template.py

import pathlib
import sys

def blink(numbers):
    res = []

    for number in numbers:
        string = str(number)
        no_of_digits = len(string)

        if number == 0:
            res.append(1)
        elif no_of_digits % 2 == 0:
            res.append(int(string[:no_of_digits//2]))
            res.append(int(string[no_of_digits//2:]))
        else:
            res.append(number * 2024)
    
    return res

def parse(puzzle_input):
    """Parse input."""
    return [int(numbers) for numbers in puzzle_input.split()]

def part1(data):
    """Solve part 1."""
    numbers = data

    for _ in range(25):
        numbers = blink(numbers)

    return len(numbers)

def part2(data):
    """Solve part 2."""

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