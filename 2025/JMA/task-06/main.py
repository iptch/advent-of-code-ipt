def get_highest_joltage(batteries_row):
    batteries_row = batteries_row.strip()
    maximums = []
    pos = 0
    K = 12                     # must choose 12 digits

    for remaining in range(K, 0, -1):
        # Compute the window end so we don't run out of digits
        end = len(batteries_row) - remaining

        # Scan from current pos to allowed end
        window = batteries_row[pos:end + 1]

        # Choose max digit in the window
        max_digit = max(window)

        # Move pos to *after* the chosen digit
        idx = window.index(max_digit)
        pos += idx + 1

        # Append digit
        maximums.append(max_digit)

    # Convert selected digits into a number
    return int("".join(maximums))


def solve(input):
    solution = 0
    with open(input, 'r') as file:
        for line in file:
            solution += get_highest_joltage(line)
    return solution


if __name__ == '__main__':
    print(solve("input.txt"))