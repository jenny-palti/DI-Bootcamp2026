# Exercise 2: Working with JSON - Week 2, Day 4

import json
import os

sampleJson = """{
   "company":{
      "employee":{
         "name":"emma",
         "payable":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Step 1: Load the JSON string into a Python dictionary
data = json.loads(sampleJson)

# Step 2: Access the nested "salary" key
salary = data["company"]["employee"]["payable"]["salary"]
print("Salary:", salary)

# Step 3: Add the "birth_date" key to the employee
data["company"]["employee"]["birth_date"] = "1995-03-21"

# Step 4: Save the modified JSON to a file (next to this script)
output_path = os.path.join(os.path.dirname(__file__), "modified_employee.json")
with open(output_path, "w") as file:
    json.dump(data, file, indent=4)

print("Saved to", output_path)
