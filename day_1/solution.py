#!/usr/bin/env python3
import argparse

def parse_input_data():
    with open("input.txt", "r") as input_file:
        data = input_file.read()
        parsed_data = data.splitlines()
        return parsed_data

def solution_1():
    parsed_data = parse_input_data()
    frequency_result = 0
    for frequency_reading in parsed_data:
        frequency_result += int(frequency_reading)
    print("Final frequency result = {}".format(frequency_result))

def solution_2():
    parsed_data = parse_input_data()
    current_frequency = 0
    previously_seen_frequencies = {current_frequency}
    while True: # We may have to traverse the input data multiple times before seeing a repeat
        for frequency_reading in parsed_data:
            current_frequency += int(frequency_reading)
            if current_frequency in previously_seen_frequencies:
                print("The current frequency {} has been seen before!".format(current_frequency))
                return
            previously_seen_frequencies.add(current_frequency)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--solution_2", help="Find the answer to solution 2", action="store_true")
    args = parser.parse_args()
    if args.solution_2:
        solution_2()
    else:
        solution_1()