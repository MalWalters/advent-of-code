# Advent of Code
# Day 02
# Part 1

import os, csv, math

#open file
data_directory = os.path.dirname(os.path.abspath(__file__))
data_file = 'day-02-input.txt'
source_file = os.path.join(data_directory,data_file)

opp_list = []

with open(source_file) as f:
    data = f.read().splitlines() #data is a 1 element list
    for item in data[0].split(','):
        opp_list.append(int(item))
    #print(opp_list)
    #print('=============================================================')
    address_pointer = 0
    operand = opp_list[address_pointer]    
    while operand != 99:          
        if opp_list[address_pointer] == 1:
            # Adding
            opp_list[opp_list[address_pointer + 3]] = opp_list[opp_list[address_pointer + 1]] + opp_list[opp_list[address_pointer + 2]]
        elif opp_list[address_pointer] == 2:
            #Multiplication
            opp_list[opp_list[address_pointer + 3]] = opp_list[opp_list[address_pointer + 1]] * opp_list[opp_list[address_pointer + 2]]
        address_pointer += 4
        operand = opp_list[address_pointer]

    print(opp_list[0])
