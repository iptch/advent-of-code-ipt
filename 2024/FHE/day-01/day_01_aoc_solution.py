import numpy as np

def read_input():
    """ reads the input (csv) file into a list"""
    data = np.loadtxt('input.csv', delimiter=';')
    return data


if __name__ == "__main__":
    data = read_input()

    # split the data and sort according to size
    # switched left and right column, since I switched them in the input file by accident
    right_col = np.sort(data[:, 0])
    left_col = np.sort(data[:, 1])

    # calculate the distance between the elements and take the sum
    diff = abs(left_col - right_col)
    total_difference = np.sum(diff)

    # print the solution
    print("The total difference is: " + str(total_difference))

    # PART 2
    # create frequency dictionnary to avoid recalculations
    unique_values, counts = np.unique(right_col, return_counts=True)
    frequency_dict = dict(zip(unique_values, counts))

    # calculate the similarity score
    similarity_score = 0
    for num in left_col:
        # get the stored frequency or use default 0
        similarity_score += frequency_dict.get(num, 0) * num

    print("The similarity score is: " + str(similarity_score))



