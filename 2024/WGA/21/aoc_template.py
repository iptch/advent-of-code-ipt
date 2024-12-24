# aoc_template.py

import pathlib
import sys
import heapq
from collections import defaultdict

NUMPAD = ["789", "456", "123", " 0A"]
DIRPAD = [" ^A", "<v>"]
DIRECTIONS = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

def get_buttons(keypad):
    graph = {}

    for x, row in enumerate(keypad):
        for y, cell in enumerate(row):
            graph[cell] = (x, y)

    return graph

def get_moves_dict(keypad):
    moves_dict = defaultdict(dict)
    buttons = get_buttons(keypad)

    for i in buttons:
        for j in buttons:
            if i != " " and j != " ":
                moves_dict[i][j] = dijkstra(buttons[i], buttons[j], keypad)

    return moves_dict

def dijkstra(start, end, map):
    pq = [(0, start[0], start[1], "")]
    visited = set()

    while pq:
        cost, x, y, seq = heapq.heappop(pq)

        if (x, y) == end:
            return seq + "A"

        if (x, y, seq) in visited:
            continue
        
        visited.add((x, y, seq))

        for new_dir in DIRECTIONS:
            dx, dy = DIRECTIONS[new_dir]
            nx, ny = x + dx, y + dy

            if nx >= 0 and nx < len(map) and ny >= 0 and ny < len(map[nx]) and map[nx][ny] != ' ':
                new_cost = cost + 1
                dir = "" if seq == "" else seq[-1]

                # Get sequences with the least direction changes
                if dir != new_dir:
                    new_cost += 1
                    
                    # Get sequences with button furthest away from A in front when moving diagonally
                    if new_dir == "<" and dir in ["v", "^"] or new_dir == "v" and dir == ">":
                        new_cost += 1

                heapq.heappush(pq, (new_cost, nx, ny, seq+new_dir))
    return

def get_sequence(code, n):
    numpad_moves_dict = get_moves_dict(NUMPAD)
    dirpad_moves_dict = get_moves_dict(DIRPAD)

    sequence = ""

    for i, num in enumerate(code):
        if i == 0:
            sequence += numpad_moves_dict["A"][num]
        else:
            sequence += numpad_moves_dict[code[i-1]][num]

    for _ in range(n):
        tmp = ""

        for i, dir in enumerate(sequence):
            if i == 0:
                tmp += dirpad_moves_dict["A"][dir]
            else:
                tmp += dirpad_moves_dict[sequence[i-1]][dir]

        sequence = tmp

    return sequence

def parse(puzzle_input):
    """Parse input."""

    return puzzle_input.splitlines()

def part1(data):
    """Solve part 1."""
    complexity = 0

    for code in data:
        sequence = get_sequence(code, 2)
        complexity += len(sequence) * int(code[:-1])

    return complexity

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