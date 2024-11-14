# Algorithm Document



- Purpose: User inputs file selection.
- Name: file_name
- Parameters: None
- Return: selection

1. Selection variable = user input ("Please select a file:")
2. While file doesn't exist:
   1. Output error message
   2. Selection = user input
3. Return selection variable



- Purpose: Reads selected file.
- Name: read_file
- Parameters: selection
- Return: table

1. Set table equal to empty list. 
2. Try:
   1. Open file selection for reading
