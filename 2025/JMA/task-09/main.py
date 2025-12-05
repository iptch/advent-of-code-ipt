def is_spoiled(item, inventory):
    for boundary in inventory:
        if not (item < boundary[0] or item > boundary[1]):
            return False
    return True


def solve(input_file):
    not_spoiled = []
    items = []
    solution = 0
    is_inventory = True
    with open(input_file) as f:
        for line in f.readlines():
            if line == "\n":
                is_inventory = False
                continue
            if is_inventory:
                new_range = [int(n.replace("\n", "")) for n in line.split("-")]
                not_spoiled.append(new_range)
            if not is_inventory and not line == "\n":
                items.append(int(line.replace("\n", "")))

    for item in items:
        if not is_spoiled(item, not_spoiled):
            solution += 1



    print(not_spoiled)
    print(items)
    return solution

if __name__ == '__main__':
    print(solve("input.txt"))
