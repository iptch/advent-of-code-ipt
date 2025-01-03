# aoc_template.py

import pathlib
import sys
from functools import lru_cache

NUM = {
    "7": {'7': 'A', '8': '>A', '9': '>>A', '4': 'vA', '5': 'v>A', '6': 'v>>A', '1': 'vvA', '2': 'vv>A', '3': 'vv>>A', '0': '>vvvA', 'A': '>>vvvA'},
    "8": {'7': '<A', '8': 'A', '9': '>A', '4': '<vA', '5': 'vA', '6': 'v>A', '1': '<vvA', '2': 'vvA', '3': 'vv>A', '0': 'vvvA', 'A': 'vvv>A'},
    "9": {'7': '<<A', '8': '<A', '9': 'A', '4': '<<vA', '5': '<vA', '6': 'vA', '1': '<<vvA', '2': '<vvA', '3': 'vvA', '0': '<vvvA', 'A': 'vvvA'},
    "4": {'7': '^A', '8': '^>A', '9': '^>>A', '4': 'A', '5': '>A', '6': '>>A', '1': 'vA', '2': 'v>A', '3': 'v>>A', '0': '>vvA', 'A': '>>vvA'},
    "5": {'7': '<^A', '8': '^A', '9': '^>A', '4': '<A', '5': 'A', '6': '>A', '1': '<vA', '2': 'vA', '3': 'v>A', '0': 'vvA', 'A': 'vv>A'},
    "6": {'7': '<<^A', '8': '<^A', '9': '^A', '4': '<<A', '5': '<A', '6': 'A', '1': '<<vA', '2': '<vA', '3': 'vA', '0': '<vvA', 'A': 'vvA'},
    "1": {'7': '^^A', '8': '^^>A', '9': '^^>>A', '4': '^A', '5': '^>A', '6': '^>>A', '1': 'A', '2': '>A', '3': '>>A', '0': '>vA', 'A': '>>vA'},
    "2": {'7': '<^^A', '8': '^^A', '9': '^^>A', '4': '<^A', '5': '^A', '6': '^>A', '1': '<A', '2': 'A', '3': '>A', '0': 'vA', 'A': 'v>A'},
    "3": {'7': '<<^^A', '8': '<^^A', '9': '^^A', '4': '<<^A', '5': '<^A', '6': '^A', '1': '<<A', '2': '<A', '3': 'A', '0': '<vA', 'A': 'vA'},
    "0": {'7': '^^^<A', '8': '^^^A', '9': '^^^>A', '4': '^^<A', '5': '^^A', '6': '^^>A', '1': '^<A', '2': '^A', '3': '^>A', '0': 'A', 'A': '>A'},
    "A": {'7': '^^^<<A', '8': '<^^^A', '9': '^^^A', '4': '^^<<A', '5': '<^^A', '6': '^^A', '1': '^<<A', '2': '<^A', '3': '^A', '0': '<A', 'A': 'A'}
}

DIR = {
    "^": {"^": "A", "A": ">A", "<": "v<A", "v": "vA", ">": "v>A"},
    "A": {"^": "<A", "A": "A", "<": "v<<A", "v": "<vA", ">": "vA"},
    "<": {"^": ">^A", "A": ">>^A", "<": "A", "v": ">A", ">": ">>A"},
    "v": {"^": "^A", "A": "^>A", "<": "<A", "v": "A", ">": ">A"},
    ">": {"^": "<^A", "A": "^A", "<": "<<A", "v": "<A", ">": "A"}
}

@lru_cache(None)
def length(seq, n):
    if n > 0:
        min_len = 0
        
        for i, dir in enumerate(seq):
            if i == 0:
                min_len += length(DIR["A"][dir], n-1)
            else:
                min_len += length(DIR[seq[i-1]][dir], n-1)

        return min_len

    return len(seq)

def parse(puzzle_input):
    """Parse input."""

    return puzzle_input.splitlines()

def part1(data):
    """Solve part 1."""
    complexity = 0

    for code in data:
        sequences = [NUM["A"][num] if i == 0 else NUM[code[i-1]][num] for i, num in enumerate(code)]
        complexity += length("".join(sequences), 2) * int(code[:-1])

    return complexity

def part2(data):
    """Solve part 2."""
    complexity = 0

    for code in data:
        sequences = [NUM["A"][num] if i == 0 else NUM[code[i-1]][num] for i, num in enumerate(code)]
        print(length("".join(sequences), 25))
        complexity += length("".join(sequences), 25) * int(code[:-1])

    return complexity

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