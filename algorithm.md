# Algorithm Document
Programmers:  Caitlin Burns John Elehwany
Course:  CS151, professor Zee
Due Date: 11/21
Lab Assignment:  10


- Purpose: Gets file name input from user.
- Name: file_name
- Parameters: None
- Return: selection

1. Selection variable = user input ("Enter file name:")
2. While file doesn't exist:
   1. Output error message
   2. Selection = user input
3. Return selection variable



- Purpose: Reads file and converts strings to ints and to make a table
- Name: read_file
- Parameters: selection
- Return: table

1. Create a table
2. Try:
   1. open file for reading
         1. For line in file:
            1. Split lines with commas
            2. Convert rows 2, 3, and 4 into integers
            3. Add row to table list via append()
         2. Close file
3. If file is not found output error
4. Return table



- Purpose: Calculates profit and appends to list.
- Name: calculate_profit
- Parameters: table
- Return: none
1. set new table to empty list
2. For each row in table:
   1. Budget is set to row 2
   2. Gross is set to row 3 + row 4
   3. Profit = gross - budget
   4. Add profit to row
   5. append new table to row
3. return new t

- purpose: finds most profitable movie in file
- name: max profit
- parameters: table
- return: most profit
1. set most profit equal to table index zero
2. for row in table
   1. if row index 5 is greater than most profit index 5
      1. set most profit equal to row
3. return most profit

   

- Purpose: Converts table to a file.
- Name: table_to_file
- Parameters: table
- Return: none

1. Get user input for name of output file
2. fd = open an out_file, 'w' for writing
3. For each row in table:
   1. set line equal to empty string
   2. For item in row:
      1. line += str item plus empty string
   3. write line plus a new line



- Purpose: Runs main program.
- Name: main
- Parameters: None
- Return: None

1. Output purpose of program to user
2. Selection = file_name()
3. Table is set to read file of selection
4. Run calculate_profit with table parameter
5. Run table_to_file with table profit parameter
6. Output file creation success
7. Ask user if they would like to see the movie with the most profit and set answer equal to choice variable
8. convert answer to lower
9. if choice is equal to 'y'
   1. call max profit function by setting it equal to most profit using table profit parameter
   2. output the name of the movie with the most profit using a f string printing most profit index 1
10. else
    1. output thank you message

-----

Run main() function