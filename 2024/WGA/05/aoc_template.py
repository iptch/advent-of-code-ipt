# aoc_template.py

import pathlib
import sys

def violates_rule(rules, page_prev, page_next):
    for rule in rules:
        if rule[0] == page_next and rule[1] == page_prev:
            return True

    return False

def is_valid_update(rules, update):
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            if violates_rule(rules, update[i], update[j]):
                return False

    return True

def partition(rules, update, low, high):
    pivot = update[high]
    i = low - 1

    for j in range(low, high):
        if violates_rule(rules, update[j], pivot):
            i += 1
            update[i], update[j] = update[j], update[i]

    update[i + 1], update[high] = update[high], update[i + 1]

    return i + 1

def quick_sort(rules, update, low, high):
    if low < high:
        pivot = partition(rules, update, low, high)
        quick_sort(rules, update, low, pivot-1)
        quick_sort(rules, update, pivot+1, high)

def parse(puzzle_input):
    """Parse input."""
    input = puzzle_input.split("\n\n")
    rules = [[int(page) for page in rule.split("|")] for rule in input[0].split("\n")]
    updates = [[int(page) for page in update.split(",")] for update in input[1].split("\n")]

    return rules, updates

def part1(data):
    """Solve part 1."""
    rules, updates = data
    sum = 0

    for update in updates:
        if is_valid_update(rules, update):
            sum += update[(len(update)-1) // 2]

    return sum

def part2(data):
    """Solve part 2."""
    rules, updates = data
    sum = 0

    for update in updates:
        if not is_valid_update(rules, update):
            quick_sort(rules, update, 0, len(update)-1)
            sum += update[(len(update)-1) // 2]

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