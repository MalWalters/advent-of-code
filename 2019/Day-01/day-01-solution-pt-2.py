# Advent of Code
# Day 01
# Part Advent

import os, csv, math

#open file
data_directory = os.path.dirname(os.path.abspath(__file__))
data_file = 'day-01-input.txt'
source_file = os.path.join(data_directory,data_file)

fuel_upper_counter = 0

def scales(mass):
    return math.floor(int(mass)/3)-2

with open(source_file) as f:
    data = f.read().splitlines()
 
    for mass in data:
        initial_fuel = 0
        total_fuel_weight = current_fuel_weight = initial_fuel_weight = scales(mass)
        while current_fuel_weight > 0:
            new_fuel_weight = scales(current_fuel_weight)
            if new_fuel_weight > 0:
                total_fuel_weight += new_fuel_weight
            current_fuel_weight = new_fuel_weight
            
        #total_fuel = initial_fuel + scales(initial_fuel, 'fuel')
        fuel_upper_counter += total_fuel_weight
print(fuel_upper_counter)