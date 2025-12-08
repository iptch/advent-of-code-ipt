def solve(filename):
    sums = 0
    with open(filename, "r") as file:
        sheet = []
        for line in file.readlines():
            numbers = line.replace("\n", "").split()
            sheet.append(numbers)

        nums = sheet[:-1]
        operators = sheet[-1]
        width = len(operators)
        height = len(nums)

        for i in range(0, width):
            op = operators[i]
            if op == "+":
                for j in range(0, height):
                    sums += int(nums[j][i])
            if op == "*":
                mult = 1
                for j in range(0, height):
                    mult = mult * int(nums[j][i])
                sums += mult

    return sums

if __name__ == "__main__":
    print(solve("input.txt"))