def parse_input(part):
    lines = []
    with open("input.txt") as f:
        for line in f:
            line = line.rstrip("\n")
            lines.append(line)

    width = max(len(line) for line in lines)
    grid = [line.ljust(width) for line in lines]

    nrows = len(grid)
    op_row_idx = nrows - 1

    sep = []
    for col in range(width):
        is_sep = all(grid[r][col] == " " for r in range(nrows))
        sep.append(is_sep)

    problems = []
    c = 0
    while c < width:
        if sep[c]:
            c += 1
            continue

        start = c
        while c < width and not sep[c]:
            c += 1
        end = c
    
        operator = None
        for ch in grid[op_row_idx][start:end]:
            if ch in "+*":
                operator = ch
                break

        nums = []

        if part == "one":
            for r in range(op_row_idx):
                segment = grid[r][start:end]
                digits = "".join(ch for ch in segment if ch.isdigit())
                if digits:
                    nums.append(int(digits))
        
        elif part == "two":
            for col in range(end - 1, start - 1, -1):
                column_digits = ""
                for r in range(op_row_idx):
                    ch = grid[r][col]
                    if ch.isdigit():
                        column_digits += ch
                if column_digits != "":
                    number = int(column_digits)
                    nums.append(number)

        if nums:
            problems.append((operator, nums))

    return problems


def calculate_total(problems):
    total = 0
    for op, nums in problems:
        if op == "+":
            value = sum(nums)
        elif op == "*":
            value = 1
            for num in nums:
                value *= num
        total += value

    return total


def main():
    problems = parse_input("one")
    total = calculate_total(problems)
    print("total_part_one", total)

    problems_part_two = parse_input("two")
    total = calculate_total(problems_part_two)
    print("total_part_two", total)


if __name__ == "__main__":
    main()