# Employee Manager

## What the Program Does:
This program reads employee data from a JSON file, displays the current employees, allows the user to add a new employee, and saves the updated employee list back to the JSON file.

### How to Run the Program:
1. Open a terminal in the project folder
2. Run the command
python main.py
3. Follow the prompts to enter:
-Employee Name
-Shift (morning/night)
-Is the employee working (yes/no)

#### Files Used
employees.json
-Reads data from this file
-Writes updated data to file after new employee added
main.py
-Contains main program logic
-Loads data, collects user input, saves updates
helpers.py
-Contains helper functions used by main program
-Displays employee info