# aoc_template.py

import pathlib
import sys

def mix(a, b):
    return a ^ b

def prune(a):
    return a & 16777215

def get_secret_numbers(init_number, n):
    secret_numbers = [init_number]

    for _ in range(n):
        result = secret_numbers[-1] << 6
        secret_number = mix(secret_numbers[-1], result)
        secret_number = prune(secret_number)

        result = secret_number >> 5
        secret_number = mix(secret_number, result)
        secret_number = prune(secret_number)

        result = secret_number << 11
        secret_number = mix(secret_number, result)
        secret_numbers.append(prune(secret_number))

    return secret_numbers

def parse(puzzle_input):
    """Parse input."""

    return list(map(int, puzzle_input.splitlines()))

def part1(data):
    """Solve part 1."""

    return sum([get_secret_numbers(init_number, 2000)[-1] for init_number in data])

def part2(data):
    """Solve part 2."""
    bananas = {}
    buyers = [None] * len(data)

    for i, init_number in enumerate(data):
        prices = [secret_number % 10 for secret_number in get_secret_numbers(init_number, 2000)]
        changes = [",".join([str(n - m) for m, n in zip(prices[j-4:j], prices[j-3:j+1])]) for j in range(len(prices)) if j > 3]
        buyers[i] = zip(prices[4:], changes)

    for buyer in buyers:
        max_prices = {}

        for price, seq in buyer:
            if seq not in max_prices or price > max_prices[seq]:
                max_prices[seq] = price

        for seq in max_prices:
            if seq in bananas:
                bananas[seq] += max_prices[seq]
            else:
                bananas[seq] = max_prices[seq]

    # Works on example input, but not on puzzle input
    max_seq = max(bananas, key=bananas.get)
    print(max_seq)

    return max(bananas.values())

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