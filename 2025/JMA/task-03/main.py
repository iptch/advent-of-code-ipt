def verify(ids_to_verify):
    id_solution = 0
    for id in ids_to_verify:
        string_id = str(id)
        length = len(string_id)
        first_half = string_id[:length//2]
        second_half = string_id[length//2:]

        if length % 2 == 0:
            print("ID: {}, first-half: {}, second-half: {}".format(id, first_half, second_half))
            if first_half == second_half:
                id_solution += id
    return id_solution


def solve(input):
    solution = 0
    with open(input, 'r') as file:
        ids = file.read().split(",")
        for product_range in ids:
            splits = product_range.split("-")
            solution += verify(range(int(splits[0]), int(splits[1])+1))
    return solution


if __name__ == '__main__':
    print(solve("input.txt"))
