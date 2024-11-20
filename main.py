# Programmers:  Caitlin Burns John Elehwany
# Course:  CS151, professor Zee
# Due Date: 11/21
# Lab Assignment:  10
# Problem Statement:  creates a new row of movie profit
# Data In: file names
# Data Out: new file with profit row
# Credits: read me file and class notes
# Input Files: movies.csv
import os


# Purpose: gets file name inout from user
# Parameters: none
# Return: selection
def file_name():
    selection = input('Enter file name: ')
    while not os.path.isfile(selection):
        print('Error. Please try again')
        selection = input('Enter file name: ')
    return selection


# Purpose: reads file and converts strings to ints to make a table
# Parameters: selection
# Return: table
def read_file(selection):
    table = []
    try:
        file = open(selection, 'r')
        for line in file:
            row = line.split(',')
            row[2] = int(row[2])
            row[3] = int(row[3])
            row[4] = int(row[4])
            table.append(row)
        file.close()
    except FileNotFoundError:
        print('File does not exist')
    return table


# Purpose: calculates profit and appends to list
# Parameters: table
# Return: none
def calculate_profit(table):
    for row in table:
        budget = row[2]
        gross = row[3] + row[4]
        profit = gross - budget
        row.append(profit)


# Purpose: converts table to file
# Parameters: table
# Return: none
def table_to_file(table):
    out_file = input('what would you like to name the output file?: ')
    fd = open(out_file, 'w')
    for row in table:
        line = ','.join(map(str, row))
        line += '\n'
        for item in row:
            line += str(item) + ' '
        fd.write(line)


# Purpose: runs main program
# Parameters: none
# Return: none
def main():
    print('This program stores the information from a selected file as a list and outputs a new \nfile with an added profit row.')
    selection = file_name()
    table = read_file(selection)
    calculate_profit(table)
    table_to_file(table)
    print('File created. Thank you for using this program!')



main()