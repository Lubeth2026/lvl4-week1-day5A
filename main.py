
import json

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


new_employee = {
    "name": "John Smith", "shift": "morning", "working": True
}

employees.append(new_employee)
save_employees(employees)
print("\nNew Employee Added!")
