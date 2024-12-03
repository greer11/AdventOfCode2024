import re

def extract_data(filename):
    data = open(filename).read()
    #returns a list of all the data
    return data

def find_matches(data):
    positive_matches = []
    k_sequence = r"mul\(\d+,\d+\)"
    matches = re.findall(k_sequence,data)
    for match in matches:
        print(match)
        positive_matches.append(match)
    return positive_matches


def main(filename):
    sum = 0
    data = extract_data(filename)
    matches = find_matches(data)
    print(len(matches))
    for i in range(len(matches)):
        string = matches[i]
        pattern = r"(\d+)"
        str_numbers = re.findall(pattern, string)
        factor = int(str_numbers[0])*int(str_numbers[1])
        print(f'factor is {factor}')
        sum += factor
    return sum

def strip_data(data, pattern_to_strip):
    pattern = pattern_to_strip
    positive_hits = []
    hits = re.findall(pattern, data)
    for hit in hits:
        positive_hits.append(hit)
    print("printing hits")
    print(hits)
    stripped_data = re.sub(pattern, '', data, flags=re.DOTALL)
    return stripped_data



def main_part_2(filename):
    sum = 0
    data = extract_data(filename)
    stripped_data = strip_data(data, r"don't\(\).*?do\(\)")
    further_stripped_data = strip_data(stripped_data, r"don't\(\).*")
    matches = find_matches(further_stripped_data)
    print(len(matches))
    for i in range(len(matches)):
        string = matches[i]
        pattern = r"(\d+)"
        str_numbers = re.findall(pattern, string)
        factor = int(str_numbers[0]) * int(str_numbers[1])
        print(f'factor is {factor}')
        sum += factor
    return sum





sum = main_part_2('challenge_data_day3.txt')
print(sum)