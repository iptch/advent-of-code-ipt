from timeit import default_timer as timer

from aocd import data

DAY = '02'
PART = 'b'


def is_invalid(id):
    is_valid = True
    for pattern_size in range(1, len(id)//2 + 1):
        patterns = [id[j:j+pattern_size] for j in range(0, len(id), pattern_size)]
        if len(set(patterns)) == 1:
            is_valid = False
    return not is_valid


def solve(lines):
    result = 0
    for begin, end in [r.split('-') for r in lines[0].split(',')]:
        for id in range(int(begin), int(end) + 1):
            if is_invalid(str(id)):
                result += id
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
