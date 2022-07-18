#dictionary - varName = {key:  value,,,,,,}

studentDetails = {
    "ID": "STD-0101",
    "Name": "John Doe",
    "Email": "jdoe@google.go",
    "Age": 26,
    "Alumni": False,
    "Courses": ["PMP", "CCNA", "OSD"],
    "Height":  5.4
}


stdName = studentDetails['Name']
# for item in studentDetails['Courses']:
stdCourses = studentDetails["Courses"][0:]
print("Student "+stdName+" has email "+studentDetails['Email'])

print(studentDetails.keys())
print(studentDetails.values())
print(studentDetails.items())

studentDetails["Gender"] = "Bob Risky"

if "Gender" in studentDetails:
    print("Gender record exists")
else:
    print("Gender record not found")

print(studentDetails)

studentDetails["Name"] = "Agapxx"

if "Name" in studentDetails:
    print("Name Record exists")
else:
    print("Gender record not found")

print(studentDetails)

studentDetails.update({"Gender": "Male"})

studentDetails.update({"Gender": "Male"})

studentDetails.pop("Alumni")
print(studentDetails)


studentDetails.popitem()
print(studentDetails)
studentDetails.popitem()
print(studentDetails)
studentDetails.popitem()
print(studentDetails)
studentDetails.popitem()
print(studentDetails)

del studentDetails['ID']
# del studentDetails

# studentDetails.clear()

for dataItem in studentDetails:
    print("The student details are shown below")
    print(studentDetails[dataItem])

y = student2["course"]
    print(y)

for key, val in studentDetails.items():
    print(key, val)


# Nesting Dictionaries

students = {
    'student1': {
        "Name": "John Doe",
        "Course": "Computer science",
        "Email": "jdoe@doe.doe"
    },
    "student2": {
        "Name": "Jane Doe",
        "Course": "Computer Engineering",
        "Email": "janedoe@doe.doe"
    }
}

student2 = students['student2']
print(student2["course"])