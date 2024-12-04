import re
import numpy as np

def read_input():
    """ reads the input (csv) file into a list"""
    with open('input03.txt', 'r') as file:
        data = file.read()

    return data

def closest_smaller_element(arr, index):
    closest = None
    closest_distance = float('inf')

    for i, num in enumerate(arr):
        if num < index and abs(num - index) < closest_distance:
            closest = num
            closest_distance = abs(num - index)

    return closest

def check_state(index, relevant_do_index, relevant_dont_index):
    distance_to_do = index - relevant_do_index
    distance_to_dont = index - relevant_dont_index

    if distance_to_do < distance_to_dont:
        return True
    else:
        return False


if __name__ == "__main__":
    data = read_input()

    # find mul pattern and corresponding indexes in data
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches_mul = re.findall(pattern, data)
    mul_start_indexes = [(m.start(0)) for m in re.finditer(pattern, data)]
    matches_int = [(int(x), int(y)) for x, y in matches_mul]

    # find "do()" pattern and corresponding indexes in data
    search_string = "do()"
    do_start_indexes = [0] + [i for i in range(len(data)) if data.startswith(search_string, i)]

    # find "don't()" pattern and corresponding indexes in data
    search_string = "don\'t()"
    dont_start_indexes = [-1] + [i for i in range(len(data)) if data.startswith(search_string, i)]

    results = 0

    for mul_start_index in mul_start_indexes:
        relevant_do_index = closest_smaller_element(do_start_indexes, mul_start_index)
        relevant_dont_index = closest_smaller_element(dont_start_indexes, mul_start_index)

        enabled = check_state(mul_start_index, relevant_do_index, relevant_dont_index)
        print("Mul_Index: " + str(mul_start_index) + ", Relevant Do: " + str(relevant_do_index) + ", Relevant Dont: " + str(relevant_dont_index) + ", enabled = " + str(enabled))

        if enabled:
            index = mul_start_indexes.index(mul_start_index)
            results += matches_int[index][0] * matches_int[index][1]

    print("Total mul sum: {}".format(results))







    # results = [x * y for x, y in matches_int]

    # total sum
    # total_mul_sum = np.sum(results)
    # print("Total mul sum: {}".format(total_mul_sum))
