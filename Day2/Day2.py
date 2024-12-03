File = 'ChallengeDataDay2.txt'
testFile = 'testDataDay2.txt'

def extractData(filename):
    data = []
    testData = open(filename)
    for line in testData:
        data.append(line.split())
    #returns a list of all the data
    return data

def check_if_valid_sequence(num_list):
    #sort the list into ascending or descending
    numbers_ascending = sorted(num_list)
    numbers_descending = sorted(num_list, reverse = True)
    if (num_list == numbers_ascending or num_list == numbers_descending):
        return True
    else: return

def check_if_valid_sequence_part2(num_list):
    #check the sequence to see if the numbers are all ascending or decending
    last_number = int(num_list[0])
    current_number = int(num_list[1])
    ascending = (current_number > last_number)
    print (ascending, type(ascending))
    for i in range(len(num_list) -1):
        current_number = int(num_list[i+1])
        print(current_number, type(current_number))
        next_step_ascending = current_number > last_number
        if ascending == next_step_ascending:
            last_number = current_number
        else:
            new_numlist = num_list.copy()
            new_numlist.pop(i+1)
            return new_numlist, False
    return num_list, True



def check_sequence_difference(num_list):
    initial_number = num_list[0]
    for i in range(len(num_list) - 1):
        if (1<=  (abs(num_list[i+1] - initial_number))  <= 3) :
            initial_number = num_list[i+1]
        else:
            return False
    return True

def check_sequence_difference_part2(num_list):
    initial_number = num_list[0]
    for i in range(len(num_list) - 1):
        if (1<=  (abs(int(num_list[i+1]) - int(initial_number)))  <= 3) :
            initial_number = num_list[i+1]
        else:
            new_numlist = num_list.copy()
            new_numlist.pop(i + 1)
            return new_numlist, False
    return num_list, True



def main(filename):
    #get the list of the data
    raw_data = extractData(filename)
    #set the initial sum as 0
    sum_of_safe_reports = 0
    successful_entries = []
    unsuccessful_entries = []
    #test for initial success, remove errors and append to uncessessful if unsuccessful on first round
    for i in range(len(raw_data)):
        line = raw_data[i]
        check_sequence_result = check_if_valid_sequence_part2(line)
        if check_sequence_result[1] == True:
            check_within_three = check_sequence_difference_part2(line)
            if check_within_three[1] == True:
                successful_entries.append(check_within_three[0])
            else:
                unsuccessful_entries.append(check_within_three[0])
        else:
            unsuccessful_entries.append(check_sequence_result[0])
    #try again with unsuccessfuls
    for u in range(len(unsuccessful_entries)):
        second_pass_line = unsuccessful_entries[u]
        check_sequence_result_second_pass = check_if_valid_sequence_part2(second_pass_line)
        if check_sequence_result_second_pass[1] == True:
            check_within_three_second_pass = check_sequence_difference_part2(second_pass_line)
            if check_within_three_second_pass[1] == True:
                successful_entries.append(second_pass_line)

    print(successful_entries)
    print(len(successful_entries))


#main(testFile)
main(File)