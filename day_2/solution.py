#!/usr/bin/env python3
from Levenshtein import distance, editops

def parse_input_data(file_name):
    with open(file_name, "r") as input_file:
        data = input_file.read()
        parsed_data = data.splitlines()
        return parsed_data

def solution_1():
    parsed_data = parse_input_data("input.txt")
    twos_count = 0
    threes_count = 0
    for line in parsed_data:
        seen_chars = {}
        for char in line:
             if char in seen_chars:
                 seen_chars[char] += 1
             else:
                seen_chars[char] = 1 
        sum = 0
        has_counted_2 = False
        has_counted_3 = False
        # Weak logic I shouldn't have to iterate back over the dict of seen_chars
        # I should keep track in the loop above
        for char in seen_chars:
            sum += seen_chars[char]
            if seen_chars[char] == 2 and not has_counted_2:
                has_counted_2 = True
                twos_count += 1
            if seen_chars[char] == 3 and not has_counted_3:
                has_counted_3 = True
                threes_count += 1

    print("twos_count = {}".format(twos_count))
    print("threes_count = {}".format(threes_count))
    print("checksum = {}".format(twos_count * threes_count))

def solution_2():
    # This can be measure using the Levenshtein distance
    # https://en.wikipedia.org/wiki/Levenshtein_distance
    parsed_data = parse_input_data("input.txt")
    for index, line_1 in enumerate(parsed_data):
        for line_2 in parsed_data[index:]: # TODO: Start from line_1 position +1 not the start of the list
            if distance(line_1, line_2) == 1:
                index_of_differing_char = editops(line_1, line_2)[0][1]
                print("Mathcing string = {}".format(line_1[:index_of_differing_char]+line_1[index_of_differing_char+1:]))
                return
        



if __name__ == "__main__":
    # solution_1()
    solution_2()