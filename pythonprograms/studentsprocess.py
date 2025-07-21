class Student:
    def __init__(self,htno,name,branch):
        self.htno = htno
        self.name = name
        self.branch = branch


    def getData(self):
        self.m1 = int(input("Enter the first subject marks "))
        self.m2 = int(input("Enter the second subject marks "))
        self.m3 = int(input("Enter the third subject marks "))


    def processData(self):
       self.total = self.m1 + self.m2 + self.m3
       self.average = self.total / 3
       if self.average >= 80:
           self.result = "Distinction"
       elif self.average >= 70 and self.average <80:
           self.result = "First Class"
       elif self.average >= 60 and self.average <70:
           self.result = "Second Class"
       elif self.average >= 50 and self.average <60:
           self.result = "Third Class"
       else:
           self.result = "Fail"

    def printData(self):
        print("Hall Ticket No: ", self.htno)
        print("Name of the Student: ", self.name)
        print("Branch: ", self.branch)
        print("M1 = ",self.m1, "M2 = ",self.m2, "M3 = ",self.m3)
        print("Total = ", self.total)
        print("The average is: ",self.average)
        print("The result is: ",self.result)


if __name__ == '__main__':
    student1 = Student("1001","Satish","CSE")
    student1.getData()
    student1.processData()
    student1.printData()