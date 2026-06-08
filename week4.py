students = []

def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "marks": marks
    }

    students.append(student)

def view_students():

    if len(students) == 0:
        print("No records found")
        return

    for student in students:
        print(student["name"], "-", student["marks"])

def average_marks():

    if len(students) == 0:
        print("No records found")
        return

    total = 0

    for student in students:
        total += student["marks"]

    average = total / len(students)

    print("Average Marks:", average)

def highest_scorer():

    if len(students) == 0:
        print("No records found")
        return

    top_student = students[0]

    for student in students:
        if student["marks"] > top_student["marks"]:
            top_student = student

    print("Highest Scorer:")
    print(top_student["name"], "-", top_student["marks"])

while True:

    print("\nSTUDENT GRADE MANAGER")
    print("1. Add Student")
    print("2. View Students")
    print("3. Average Marks")
    print("4. Highest Scorer")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        average_marks()

    elif choice == "4":
        highest_scorer()

    elif choice == "5":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")