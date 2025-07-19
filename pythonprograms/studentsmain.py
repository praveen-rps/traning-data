#import studentutils as sutils
from studentutils import addstudent, displaystudents

studentslist = []

n = int(input("Enter the number of students"))
for i in range(n):
    name = input("Enter name of the student")
    marks = []
    for j in range(3):
        x = int(input("Enter subject marks"))
        marks.append(x)
    addstudent(studentslist, name, marks)


displaystudents(studentslist)


