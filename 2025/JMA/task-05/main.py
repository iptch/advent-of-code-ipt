def get_highest_joltage(batteries_row):
    max_1 = max_2 = pos = 0

    ## Get first number, ignoring last number and newline character
    for i in range(0, len(batteries_row) - 2):
        n = int(batteries_row[i])
        if n > max_1:
            max_1 = n
            pos = i
    batteries_row_updated = batteries_row[pos + 1:]

    ## Get second number, ignoring newline character
    for i in range(0, len(batteries_row_updated) - 1):
        n = int(batteries_row_updated[i])
        if n > max_2:
            max_2 = n

    print("Number: {} \n\tRight Segment: {} \n\tMax1: {} \n\tMax2: {} \n\tNumber: {} \n".format(batteries_row, batteries_row_updated, max_1, max_2, int(str(max_1) + str(max_2))))

    return int(str(max_1) + str(max_2))



def solve(input):
    solution = 0
    with open(input, 'r') as file:
        for line in file:
            solution += get_highest_joltage(line)
    return solution


if __name__ == '__main__':
    print(solve("input.txt"))
