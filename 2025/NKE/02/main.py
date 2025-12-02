def parse_input():
    ranges = []
    with open("example.txt") as f:
        line = f.readline().strip()
        parts = line.split(",")
        for p in parts:
            start, end = p.split("-")
            ranges.append((int(start), int(end)))
                            
    return ranges


def is_invalid(n):
    s = str(n)
    if len(s) % 2 != 0:
        return False
    mid = len(s) // 2
    if s[:mid] == s[mid:]:
        return True
    else:
        return False


def is_invalid_part2(n):
    s = str(n)
    for chunk in range(1, len(s) // 2 + 1):
        if len(s) % chunk != 0:
            continue
        chunks = [s[i:i+chunk] for i in range(0, len(s), chunk)]

        if all(chunks[0] == chunks[i] for i in range(1, len(chunks))):
            return True
    
    return False


def count_invalid_ids(ranges, part):
    count = 0
    for start, end in ranges:
        for n in range(start, end+1):
            if part == 'one':
                if is_invalid(n):
                    count += n
            else:
                if is_invalid_part2(n):
                    count += n
    return count


def main():
    ranges = parse_input()
    count_one = count_invalid_ids(ranges, "one")
    count_two = count_invalid_ids(ranges, "two")
    print("part_one:", count_one)
    print("part_two:", count_two)


if __name__ == "__main__":
    main()