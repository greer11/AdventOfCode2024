File = 'ChallengeDataDay2.txt'
testFile = 'testDataDay2.txt'

def extractData(filename):
    data = []
    testData = open(filename)
    for line in testData:
        data.append(line.split())
    #returns a list of all the data
    return data



def check_safety(check_report: list, remove_index=None):
    if remove_index is not None:
        if remove_index < 0:
            return False
        temp_list = [x for x in check_report]
        del temp_list[remove_index]
        check_report = [x for x in temp_list]
    safe = True

    if check_report[1]>check_report[0]:
        increasing = True
    else:
        increasing = False

    for n in range(0, len(check_report) - 1):
        difference = abs(check_report[n+1] - check_report[n])
        if not 1 <= difference <= 3:
            safe = False
        elif increasing and check_report[n+1] < check_report[n]:
            safe = False
        elif not  increasing and check_report[n+1] > check_report[n]:
            safe = False
        if not safe:
            if remove_index is None:
                return (check_safety(check_report, n) or check_safety(check_report, n+1) or check_safety(check_report, n-1))
            else:
                break
    return safe


def main(filename):
    safe_counter = 0
    data = extractData(filename)
    for line in data:
        int_line = []
        for s in line:
            int_line.append(int(s))
        report = [int(x) for x in int_line]
        if check_safety(report):
            safe_counter += 1
    print(safe_counter)


main(File)