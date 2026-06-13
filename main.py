
import json
from helpers import display_employees
# print("Greetings!")

# Function #1 Creates a function & returns employee list
def load_employees():
    with open("employees.json", "r") as file:
        return json.load(file)

# Function #2 Accepts data & writes it in JSON file
def save_employees(employees):
    with open("employees.json", "w") as file:
        json.dump(employees, file, indent=4)

employees = load_employees()

print("Current Employees:")
display_employees(employees)

name = input("Enter Employee Name: ")
shift = input("Enter Shift (morning/night): ")
working_input = input("Is the Employee Working? (yes/no): ")
# Convert yes/no into True/False 
if working_input.lower() == "yes":
    working = True
else:
    working = False

new_employee = {
    "name": name, "shift": shift, "working": working
}

employees.append(new_employee)
save_employees(employees)
print("\nNew Employee Added!")
