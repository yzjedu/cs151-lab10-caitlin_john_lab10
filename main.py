# comments
import os

def file_name():
    selection = input('Enter file name: ')
    while not os.path.isfile(selection)
        print('Error. Please try again')
        selection = input('Enter file name: ')
    return selection

def read_file(selection):
    table = []
    try:
        file = open(selection, 'r')
        for line in file:
            row = line.split(,)
            row[2] = int(row[2])
            row[3] = int(row[3])
            row[4] = int(row[4])
        table.append(row)
    except file
