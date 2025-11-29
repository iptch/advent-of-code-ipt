# aoc_template.py

import pathlib
import sys
import re
from collections import defaultdict

def get_type_rank(hand):
    sorted_hand = "".join(sorted(hand))

    if re.search(r"(.)\1\1\1\1", sorted_hand) is not None:
        return 6
    if re.search(r"(.)\1\1\1", sorted_hand) is not None:
        return 5
    if (re.search(r"(.)\1\1(.)\2", sorted_hand) is not None or
        re.search(r"(.)\1(.)\2\2", sorted_hand) is not None):
        return 4
    if re.search(r"(.)\1\1", sorted_hand) is not None:
        return 3
    if (re.search(r".(.)\1(.)\2", sorted_hand) is not None or
        re.search(r"(.)\1.(.)\2", sorted_hand) is not None or
        re.search(r"(.)\1(.)\2.", sorted_hand) is not None):
        return 2
    if re.search(r"(.)\1", sorted_hand) is not None:
        return 1
    
    return 0

def get_card_rank(card, joker):
    if card == "T":
        return 10
    if card == "J":
        return 1 if joker else 11
    if card == "Q":
        return 12
    if card == "K":
        return 13
    if card == "A":
        return 14
    
    return int(card)
    
def get_most_frequent_card(hand):
    card_count = defaultdict(int)
    
    for card in hand:
        if card != "J":
            card_count[card] += 1
    
    return max(card_count, key=card_count.get)

def get_hand_strength(hand, joker):
    replaced_hand = hand

    if joker and hand != "JJJJJ":
        most_frequent_card = get_most_frequent_card(hand)
        replaced_hand = hand.replace("J", most_frequent_card)

    return (get_type_rank(replaced_hand),
            get_card_rank(hand[0], joker),
            get_card_rank(hand[1], joker),
            get_card_rank(hand[2], joker),
            get_card_rank(hand[3], joker),
            get_card_rank(hand[4], joker))

def parse(puzzle_input):
    """Parse input."""
    rows = [row.split() for row in puzzle_input.splitlines()]

    return [(hand, int(bid)) for hand, bid in rows]

def part1(data):
    """Solve part 1."""
    sorted_hands = sorted(data, key=lambda x: get_hand_strength(x[0], False))

    return sum([bid * (i+1) for i, (_, bid) in enumerate(sorted_hands)])

def part2(data):
    """Solve part 2."""
    sorted_hands = sorted(data, key=lambda x: get_hand_strength(x[0], True))

    return sum([bid * (i+1) for i, (_, bid) in enumerate(sorted_hands)])

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