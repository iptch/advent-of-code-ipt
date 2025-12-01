from timeit import default_timer as timer

from aocd import data

DAY = '01'
PART = 'b'


def solve(lines):
    result = 0
    position = 50
    for line in lines:
        n = int(line[1:])
        if line[0] == 'L':
            for i in range(n):
                if position == 0:
                    position = 100
                position = position - 1
                if position == 0:
                    result += 1
                    position = 100
        else:
            for i in range(n):
                if position == 100:
                    position = 0
                position = position + 1
                if position == 100:
                    result += 1
                    position = 0
        print(f"processing {line} --> at position {position} - current password: {result}")

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
