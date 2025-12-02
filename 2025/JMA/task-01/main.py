if __name__ == '__main__':
    pos = 50
    password = 0

    with open('task-01/input.txt', 'r') as file:
        for line in file.readlines():
            sign = -1 if line.startswith("L") else 1
            num = int(line[1:-1])

            pos += sign * num

            while pos < 0:
                pos += 100

            while pos >= 100:
                pos -= 100

            if pos == 0:
                password += 1

    print(password)