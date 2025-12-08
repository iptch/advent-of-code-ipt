from itertools import batched

def update_row(row, separators):
    res = []
    for idx, c in enumerate(row):
        if idx in separators:
            res.append(";")
        else:
            res.append(c.strip())
    return res


def concat_nbrs(c, grid, pos):
    res = c
    for row in grid[1:-1]:
        res += row[pos]
    return res


def solve(filename):
    with open(filename, "r") as file:
        grid = [line.rstrip("\n") for line in file]
        ops = [op for op in list(grid[-1:][0]) if op != " "]

        # Get Grid Parameters
        height = len(grid)
        width = len(grid[0])

        ## Convert to List of lists
        grid = [list(row) for row in grid]

        ## Detect separators
        separators = [x for x in range(width) if all(grid[y][x] == " " for y in range(height))]

        ## Update grid
        grid = [update_row(row, separators) for row in grid]

        ## Concat numbers
        nbrs = [concat_nbrs(c, grid, idx) for idx, c in enumerate(grid[0]) if c != ";"]

        ## Package numbers
        res = op = 0
        for nbr_batch in batched(nbrs, height-1):
            if ops[op] == "+":
                intermediate_sum = 0
                for nbr in nbr_batch:
                    intermediate_sum += int(nbr)
                res += intermediate_sum

            else:
                intermediate_sum = 1
                for nbr in nbr_batch:
                    intermediate_sum *= int(nbr)

                res += intermediate_sum

            print("op: {}, nbrs: {}, intermediate_sum: {}".format(ops[op], nbr_batch, intermediate_sum))
            op += 1

        return res

if __name__ == "__main__":
    print(solve("input.txt"))
