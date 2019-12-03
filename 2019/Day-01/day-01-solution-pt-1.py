# Advent of Code
# Day 01
# Part Advent

import os, csv, math

#open file
data_directory = os.path.dirname(os.path.abspath(__file__))
data_file = 'day-01-input.txt'
source_file = os.path.join(data_directory,data_file)

fuel_upper_counter = 0

with open(source_file) as f:
    data = f.read().splitlines()
    #print(data)
    for module in data:
        fuel_upper_counter += math.floor(int(module)/3)-2

print(fuel_upper_counter)