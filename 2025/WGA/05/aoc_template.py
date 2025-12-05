# aoc_template.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input."""
    ranges, ids = [[x for x in row.split()] for row in puzzle_input.split("\n\n")]
    ranges = [[int(x) for x in range.split("-")] for range in ranges]
    ranges = sorted(ranges, key=lambda x: x[0])
    ids = [int(id) for id in ids]

    return ranges, ids

def part1(data):
    """Solve part 1."""
    ranges, ids = data
    sum = 0

    for id in ids:
        for start, end in ranges:
            if id < start:
                break
            if start <= id <= end:
                sum += 1
                break

    return sum

def part2(data):
    """Solve part 2."""
    ranges, _ = data
    merged_ranges = [ranges[0]]

    for start, end in ranges[1:]:
        if start <= merged_ranges[-1][1]:
            if end > merged_ranges[-1][1]:
                merged_ranges[-1][1] = end
        else:
            merged_ranges.append([start, end])

    return sum([end - start + 1 for start, end in merged_ranges])

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