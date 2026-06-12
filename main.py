
import json
# print("Greetings!")

employees = [
    { "name": "Jess Noelle", "shift": "morning", "working": True },
    { "name": "Joe Hadden", "shift": "night", "working": True },
    { "name": "Kari Millan", "shift": "night", "working": False }
]

# with open("employees.json", "w") as file:
#   json.dump(employees, file)

with open("employees.json", "r") as file:
    employees = json.load(file)
print(employees)
