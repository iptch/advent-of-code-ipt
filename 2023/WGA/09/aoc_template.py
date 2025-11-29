# aoc_template.py

import pathlib
import sys

def get_prediction(row, extrapolate_forwards):                      
    sequences = [row if extrapolate_forwards else list(reversed(row))]
    i = 0

    while any(number != 0 for number in sequences[i]):
        sequences.append([m-l for l, m in zip(sequences[i][:-1], sequences[i][1:])])
        i += 1

    prediction = sequences[-1][-1]

    for sequence in list(reversed(sequences))[1:]:
        prediction += sequence[-1]

    return prediction

def parse(puzzle_input):
    """Parse input."""
    return [[int(cell) for cell in row.split()] for row in puzzle_input.splitlines()]

def part1(data):
    """Solve part 1."""
    return sum([get_prediction(row, True) for row in data])

def part2(data):
    """Solve part 2."""
    return sum([get_prediction(row, False) for row in data])

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