# aoc_template.py

import pathlib
import sys
import re

def get_matches(card):
    winning_numbers, my_numbers = card
    matches = []

    for number in winning_numbers:
        if number in my_numbers:
            matches.append(number)

    return matches

def parse(puzzle_input):
    """Parse input."""
    cards = []

    for row in puzzle_input.splitlines():
        winning_numbers, my_numbers = re.sub(r"Card\s+\d+: ", "", row).split(" | ")

        winning_numbers = [int(number) for number in re.findall(r"\d+", winning_numbers)]
        my_numbers = [int(number) for number in re.findall(r"\d+", my_numbers)]

        cards.append((winning_numbers, my_numbers))

    return cards

def part1(data):
    """Solve part 1."""
    sum = 0
 
    for card in data:
        matches_count = len(get_matches(card))
        sum += 0 if matches_count == 0 else 2 ** (matches_count - 1)

    return sum

def part2(data):
    """Solve part 2."""
    cards_count = [1] * len(data)

    for i, card in enumerate(data):
        matches_count = len(get_matches(card))

        for j in range(i+1, i+matches_count+1):
            cards_count[j] += cards_count[i]

    return sum(cards_count)

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