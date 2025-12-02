
def parse_input(file):
    input = []
    with open(file, "r") as f:
        for line in f:
            line = line.strip()
            direction = line[0]
            value = int(line[1:])
            input.append((direction, value))
    return input


def part_one(instructions):
    count = 0
    pos = 50

    for dir, val in instructions:

        if dir == 'R':
            pos += val
        if dir == 'L':
            pos += val * -1
        
        pos %= 100

        if pos == 0:
            count += 1

    return count


def part_two(instructions):
    count = 0
    pos = 50

    for dir, val in instructions:
        for _ in range(val):
            if dir == 'R':
                pos = (pos + 1) % 100
            elif dir == 'L':
                pos = (pos - 1) % 100
            if pos == 0:
                count += 1

    return count


def main():
    instructions = parse_input("example.txt")
    count_one = part_one(instructions)
    count_two = part_two(instructions)
    print("part 1: ", count_one)
    print("part 2: ", count_two)


if __name__ == "__main__":
    main()