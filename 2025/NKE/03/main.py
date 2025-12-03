def parse_input():
    banks = []
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            banks.append(str(line))                            
    return banks


def calc_max_joltage(banks):

    total = 0
    for line in banks:
        best = 0
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                val = int(line[i]) * 10 + int(line[j])
                if val > best:
                    best = val

        total += best
    return total


def max_12_subsequence(line):
    k = 12
    num_drops = len(line) - k
    stack = []

    for d in line:
        while num_drops > 0 and stack and stack[-1] < d:
            stack.pop()
            num_drops -=1
        stack.append(d)

    while num_drops > 0:
        stack.pop()
        num_drops -= 1

    return ''.join(stack[:k])


def calc_max_joltage_large(banks):
    total = 0
    for line in banks:
        chosen = max_12_subsequence(line)
        total += int(chosen)
    return total


def main():
    banks = parse_input()
    max_joltage = calc_max_joltage(banks)
    max_joltage_large = calc_max_joltage_large(banks)
    print("max_joltage: ", max_joltage)
    print("max_joltage: ", max_joltage_large)


if __name__ == "__main__":
    main()