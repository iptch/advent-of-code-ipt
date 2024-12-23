# aoc_template.py

import pathlib
import sys
import heapq
from collections import defaultdict

NUMPAD = ["789", "456", "123", " 0A"]
DIRPAD = [" ^A", "<v>"]
DIRECTIONS = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

def get_buttons(keypad):
    graph = defaultdict(tuple)

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
    pq = [(0, "", start[0], start[1])]
    visited = set()

    while pq:
        cost, seq, x, y = heapq.heappop(pq)

        if (x, y) == end:
            return seq + "A"

        if (x, y) in visited:
            continue
        
        visited.add((x, y))

        for dir in DIRECTIONS:
            dx, dy = DIRECTIONS[dir]
            nx, ny = x + dx, y + dy

            if nx >= 0 and nx < len(map) and ny >= 0 and ny < len(map[nx]) and map[nx][ny] != ' ':
                heapq.heappush(pq, (cost+1, seq+dir, nx, ny))
    return

def parse(puzzle_input):
    """Parse input."""

    return puzzle_input.splitlines()

def part1(data):
    """Solve part 1."""
    numpad_moves_dict = get_moves_dict(NUMPAD)
    dirpad_moves_dict = get_moves_dict(DIRPAD)
    complexity = 0

    for code in data:
        dir_seq_1 = ""
        dir_seq_2 = ""
        dir_seq_3 = ""

        for i in range(len(code)):
            if i == 0:
                dir_seq_1 += numpad_moves_dict["A"][code[i]]
            else:
                dir_seq_1 += numpad_moves_dict[code[i-1]][code[i]]

        for i in range(len(dir_seq_1)):
            if i == 0:
                dir_seq_2 += dirpad_moves_dict["A"][dir_seq_1[i]]
            else:
                dir_seq_2 += dirpad_moves_dict[dir_seq_1[i-1]][dir_seq_1[i]]

        for i in range(len(dir_seq_2)):
            if i == 0:
                dir_seq_3 += dirpad_moves_dict["A"][dir_seq_2[i]]
            else:
                dir_seq_3 += dirpad_moves_dict[dir_seq_2[i-1]][dir_seq_2[i]]

        complexity += len(dir_seq_3) * int(code[:-1])

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