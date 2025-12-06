from timeit import default_timer as timer

from aocd import data

import math

DAY = '06'
PART = 'b'


def solve(lines):
    result = 0
    numbers = []
    lines = [list(line) for line in lines]
    for i in range(len(lines[0])-1,-1,-1):
        col = [line[i] for line in lines]
        if all(c == ' 'for c in col):
            continue
        elif col[-1] == '+':
            numbers.append(int(''.join(col[:-1])))
            result += sum(numbers)
            numbers = []
        elif col[-1] == '*':
            numbers.append(int(''.join(col[:-1])))
            result += math.prod(numbers)
            numbers = []
        else:
            numbers.append(int(''.join(col)))

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
