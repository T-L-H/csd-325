import json


with open("student.json", "r") as file:
    class_list = json.load(file)


def print_students(students):
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")



print_students(class_list)


new_student = {
    "F_Name": "Tevyah",
    "L_Name": "Hanley",
    "Student_ID": 81903,
    "Email": "tehanley@my365.bellevue.edu"
}
class_list.append(new_student)


print("Updated Student List:")
print_students(class_list)


with open("student.json", "w") as file:
    json.dump(class_list, file)

