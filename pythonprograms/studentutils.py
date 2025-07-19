def addstudent(student_list, name, marks):
    student = {
        "name": name,
        "marks":marks,
        "total":sum(marks),
        "avg": sum(marks)/len(marks)
    }
    student_list.append(student)

def displaystudents(student_list):
    for student in student_list:
        print("-------The Student Details-------")
        print("Name of Student: ", student['name'])
        print("Marks of the Student: ", student['marks'])
        print("Total : ", student['total'])
        print("Average: ", student['avg'])

