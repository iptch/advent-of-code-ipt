import pandas as pd

def read_input():
    """ reads the input (csv) file into a list"""
    # use pandas df as it fills null values automatically with NaN
    data = pd.read_csv('input02.csv', header=None, delimiter=';')
    return data


# Function to check if a report is valid
def is_valid_report(report):
    ascending = None
    for i in range(1, len(report)):
        difference = report[i] - report[i - 1]

        # Determine if the trend is valid (increasing or decreasing)
        if difference > 0:
            if ascending is None:
                ascending = True  # Set trend to ascending
            elif ascending is False:
                return False  # Trend changed, invalid
        elif difference < 0:
            if ascending is None:
                ascending = False  # Set trend to descending
            elif ascending is True:
                return False  # Trend changed, invalid

        # Check if the difference is valid (between 1 and 3)
        if not (1 <= abs(difference) <= 3):
            return False  # Invalid difference

    return True  # If no violations, the report is valid

if __name__ == "__main__":
    data = read_input()

    # get a single report
    reports = data.apply(lambda row: row.dropna().tolist(), axis=1)

    valid_report = 0

    # Iterate over each report
    for report in reports:
        # First check if the current report is valid
        if is_valid_report(report):
            valid_report += 1
            print(f"Report: {report} - Valid: True")
        else:
            # Check if valid with an element removed
            valid_with_one_removal = False

            for i in range(len(report)):
                # Create a new report without the i-th element
                new_report = report[:i] + report[i + 1:]

                # Check if the new report is valid
                # Break out of the loop as soon as we find one
                if is_valid_report(new_report):
                    valid_with_one_removal = True
                    break

            if valid_with_one_removal:
                valid_report += 1
                print(f"Report: {report} - Valid: True (with one removal)")
            else:
                print(f"Report: {report} - Valid: False")

    print("Total valid: " + str(valid_report))