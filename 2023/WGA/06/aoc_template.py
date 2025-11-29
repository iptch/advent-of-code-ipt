# aoc_template.py

import pathlib
import sys

def get_options_count(time, distance):
    discriminant = (time ** 2 - 4 * (distance + 1)) ** .5
    min_button_time = -((time - discriminant) // -2) # Upside-down floor division
    max_button_time = (time + discriminant) // 2

    return int(max_button_time - min_button_time + 1)

def parse(puzzle_input):
    """Parse input."""
    times, distances = puzzle_input.splitlines()

    return times.split()[1:], distances.split()[1:]

def part1(data):
    """Solve part 1."""
    times = [int(time) for time in data[0]]
    distances = [int(distance) for distance in data[1]]
    result = 1

    for i, time in enumerate(times):
        result *= get_options_count(time, distances[i])

    return result

def part2(data):
    """Solve part 2."""
    times, distances = data

    return get_options_count(int("".join(times)), int("".join(distances)))

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