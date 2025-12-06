from timeit import default_timer as timer

from aocd import data

import re
import math

DAY = '06'
PART = 'a'


def solve(lines):
    result = 0
    operators = re.findall(r'[+*]+', lines[-1])
    numbers_lines = [re.findall(r'\d+', line) for line in lines[:-1]]
    numbers = []
    for i in range(len(operators)):
        numbers.append([int(line[i]) for line in numbers_lines])
    for i in range(len(operators)):
        if operators[i] == '+':
            result += sum(numbers[i])
        else:
            result += math.prod(numbers[i])

    return result


def main():
    print(f'Advent of Code 2025 --- Day {DAY} --- Part {PART}')

    lines = data.splitlines()
    result = solve(lines)

    print(f'{str(result)}')


if __name__ == '__main__':
    start = timer()
    main()
    print(f"Completed in {timer() - start} sec")
