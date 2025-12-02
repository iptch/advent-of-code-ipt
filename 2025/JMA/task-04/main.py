def verify_id(the_id):
    string_id = str(the_id)
    section = 1
    while section <= len(string_id) / 2:
        sub = string_id[:section]
        if string_id.count(sub) == len(string_id) / len(sub):
            return the_id
        section += 1
    return 0


def verify(ids_to_verify):
    id_solution = 0
    for id in ids_to_verify: id_solution += verify_id(id)
    return id_solution


def solve(input):
    solution = 0
    with open(input, 'r') as file:
        ids = file.read().split(",")
        for product_range in ids:
            splits = product_range.split("-")
            solution += verify(range(int(splits[0]), int(splits[1]) + 1))
    return solution


if __name__ == '__main__':
    print(solve("input.txt"))
