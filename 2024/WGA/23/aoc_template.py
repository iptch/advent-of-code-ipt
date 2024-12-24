# aoc_template.py

import pathlib
import sys
import re
from collections import defaultdict

def get_sets(graph):
    sets = []

    for computer1 in graph:
        for computer2 in graph[computer1]:
            if computer2 > computer1:
                for computer3 in graph[computer2]:
                    if computer3 > computer2 and computer3 in graph[computer1]:
                        sets.append(",".join([computer1, computer2, computer3]))

    return sorted(sets)

def parse(puzzle_input):
    """Parse input."""
    
    return [row.split("-") for row in puzzle_input.splitlines()]

def part1(data):
    """Solve part 1."""
    graph = defaultdict(set)

    for computer1, computer2 in data:
        graph[computer1].add(computer2)
        graph[computer2].add(computer1)

    sets = get_sets(graph)
    sets_with_t = [set for set in sets if re.search("t[a-z]", set) != None]

    return len(sets_with_t)

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