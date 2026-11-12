students = [
    {
        "roll_no": "101",
        "name": "Rahul Das",
        "branch": "CSE",
        "semester": 7,
        "marks": 82
    },
    {
        "roll_no": "102",
        "name": "Riya Sharma",
        "branch": "AIML",
        "semester": 7,
        "marks": 91
    },
    {
        "roll_no": "103",
        "name": "Aman Kumar",
        "branch": "CSE",
        "semester": 6,
        "marks": 75
    }
]

print("================================")
print(" STUDENT INFORMATION SYSTEM")
print("================================")

search = input("Enter Student Name or Roll Number: ").strip().lower()

found = False

for student in students:

    if search in student["name"].lower() or search == student["roll_no"]:

        print("\nStudent Found!")
        print("----------------------------")
        print("Name     :", student["name"])
        print("Roll No  :", student["roll_no"])
        print("Branch   :", student["branch"])
        print("Semester :", student["semester"])
        print("Marks    :", student["marks"])
        print("----------------------------")

        found = True

if not found:
    print("\nStudent Not Found.")
