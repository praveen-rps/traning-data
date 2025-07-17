courses = [
    ("C101", "Python Programming", 9000),
    ("C102", "Java Programming", 4000),
    ("C103", "DevOps Programming", 12000),
    ("C104", "Dotnet Programming", 5000),
    ("C105", "Machine Learning Programming", 19000)
]
def isRegistered(course):
    #code to check whether it is registered or not
    # if registered return true else false
    pass

def display(student):
    print("Student Id : ", student['id'])
    print("Name of Student: ", student['name'])
    print("Registered Courses: ")
    for course in student['courses']:
        print(course[0], " -- ", course[1], "--", course[2])
    print("Total Fee to pay: ", s['total_fees'])

# list to store the student details
students = []

#  Read the number of students for application
n = int(input("Enter number of students"))

for i in range(n):
    # print("Enter the student name: ")
    name = input("Enter the student name")
    sid = input("Enter the student id")
    registered_courses = set()
    course_list = []
    while True:
        print("THe list of courses available")
        for code, title, fee in courses:
            print(f"{code} -- {title} -- {fee}")
        choice = input("Enter the course number - DONE to exit")

        if choice == 'DONE':
            break
        if choice in registered_courses:
            print("Course already registered")
            continue

        found = False

        for course in courses:
            if course[0] == choice:
                course_list.append(course)
                registered_courses.add(choice)
                print("Course Added Successfully...!")
                found = True
                break
        if not found:
            print("Invalid Course Code")

    # Calculate the total fee for registered courses
    fees = 0
    for course in course_list:
        fees += course[2]

        student = {
            "id": sid,
            "name": name,
            "courses": course_list,
            "total_fees": fees
        }

    students.append(student)

    # Display the student details
for s in students:
    display(s)


