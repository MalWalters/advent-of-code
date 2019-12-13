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
    for x in range(0,len(opp_list),4):
        #print(type(opp_list[x]))
        operand = opp_list[x]
        if operand == 99:
            break
        first_number = opp_list[opp_list[x + 1]]
        second_number = opp_list[opp_list[x + 2]]
        where_to_change = opp_list[x + 3]
        if opp_list[x+3] == 0:
            print("here" + str(opp_list[x + 1]) + ':' + str(opp_list[x]) +':' + str(opp_list[x + 2]))
        if opp_list[x] == 1:
            # Adding
            opp_list[where_to_change] = first_number + second_number
        elif opp_list[x] == 2:
            #Multiplication
            opp_list[where_to_change] = first_number * second_number
        print(opp_list[0])
