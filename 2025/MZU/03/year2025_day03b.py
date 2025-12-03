from timeit import default_timer as timer

from aocd import data

DAY = '03'
PART = 'b'

N = 12


def solve(lines):
    result = 0
    for line in lines:
        numbers = [int(n) for n in  line]
        joltage = ""
        last_index = -1
        for i in range(N-1):
            highest_number = max(numbers[last_index+1:-(N-(i+1))])
            last_index = numbers[last_index+1:-(N-(i+1))].index(highest_number) + last_index + 1
            joltage += str(highest_number)
        joltage += str(max(numbers[last_index+1:]))
        result += int(joltage)
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
