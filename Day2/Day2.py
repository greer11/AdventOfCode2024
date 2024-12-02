File = 'ChallengeDataDay2.txt'
testFile = 'testDataDay2.txt'

def extractData(filename):
    data = []
    testData = open(filename)
    for line in testData:
        data.append(line.split())
    #returns a list of all the data
    return data

def check_if_valid_sequence(num_list, problem_dampener_value):
    #sort the list into ascending or descending
    numbers_ascending = sorted(num_list)
    numbers_descending = sorted(num_list, reverse = True)
    if (num_list == numbers_ascending or num_list == numbers_descending):
        return True
    else: return

def check_each_digit(digit, previous_digit, ascending):
    #check if it's ascending or descending from the last one
    #check if it's in a range of three
    is_ascending = False
    if (digit>previous_digit):
        is_ascending = True
    is_within_three = (1<=(abs(digit - previous_digit)) <=3)
    if (ascending == is_ascending and is_within_three):
        return True


def check_sequence_difference(num_list):
    initial_number = num_list[0]
    for i in range(len(num_list) - 1):
        if (1<=  (abs(num_list[i+1] - initial_number))  <= 3) :
            initial_number = num_list[i+1]
        else:
            return False
    return True

def check_data(list_of_numbers, dampener_value):
    #check_if_ascending
    print(f" the list of numbers is {list_of_numbers}")
    ascending = (list_of_numbers[0] < list_of_numbers[1])
    previous_number = int(list_of_numbers[0])
    for i in range(len(list_of_numbers)-1):
        #check ascending
        current_number = int(list_of_numbers[i+1])
        still_ascending = current_number > previous_number
        if still_ascending == ascending:
            # check within 3
            difference = abs(current_number - previous_number)
            within_three = (1 <= difference <= 3)
            if within_three:
                print(f"the number {current_number} is within 3 of {previous_number}")
                previous_number = current_number
                continue
            else:
                if dampener_value > 0:
                    print(f"whoops, {current_number} isn't within 3 of {previous_number}, but it's ok because we still have a dampener")
                    del list_of_numbers[i+1]
                    print(f"new data is {list_of_numbers}")
                    value = check_data(list_of_numbers, 0)
                    return value
                else:
                    return 0
        else:
            if dampener_value > 0:
                new_data = list_of_numbers.pop(i+1)
                value = check_data(new_data, 0)
                return value
            else:
                return 0
    return True

def main(filename):
    #get the list of the data
    raw_data = extractData(filename)
    #set the initial sum as 0
    sum_of_safe_reports = 0
    #split the data into manageable chunks
    for i in range(len(raw_data)):
        line_of_data = raw_data[i]
        value_of_data  = check_data(line_of_data, 1)
        sum_of_safe_reports += value_of_data
    print(sum_of_safe_reports)

main(testFile)