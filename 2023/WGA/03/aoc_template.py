# aoc_template.py

import pathlib
import sys
import re

def extract(regex, data):
    result = []

    for i, row in enumerate(data):
        matches = re.finditer(regex, row)

        for match in matches:
            result.append((match.group(), i, match.start(), match.end()))

    return result

def is_adjacent_to_symbol(number, data):
    _, i, start, end = number
    search_str = ""

    for row in data[max(i-1, 0):min(i+2, len(data))]:
        search_str += row[max(start-1, 0):min(end+1, len(row))]

    if re.search(r"[^0-9.]", search_str) is not None:
        return True

    return False

def get_adjacent_numbers(gear, numbers):
    _, i_gear, j_gear, _ = gear
    adjacent_numbers = []

    for i in range(i_gear-1, i_gear+2):
        for val_num, _, start_num, end_num in [number for number in numbers if number[1] == i]:
            if start_num <= j_gear + 1 and end_num >= j_gear:
                adjacent_numbers.append(int(val_num))

    return adjacent_numbers

def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.splitlines()

def part1(data):
    """Solve part 1."""
    sum = 0
    numbers = extract(r"\d+", data)

    for number in numbers:
        if is_adjacent_to_symbol(number, data):
            sum += int(number[0])

    return sum

def part2(data):
    """Solve part 2."""
    sum = 0
    numbers = extract(r"\d+", data)
    gears = extract(r"\*", data)

    for gear in gears:
        adjacent_numbers = get_adjacent_numbers(gear, numbers)

        if len(adjacent_numbers) == 2:
            sum += adjacent_numbers[0] * adjacent_numbers[1]

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