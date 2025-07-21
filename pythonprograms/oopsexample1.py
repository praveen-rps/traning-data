class Employee:
    def __init__(self,name,dept):
        self.name=name
        self.dept=dept
        self.__salary=75000

    def __str__(self):
        return f"Name :{self.name} and Dept : {self.dept} and Salary : {self.__salary}"


    def printdata(self):
        name =  "Satish"
        dept = "Operations"
        print(name+" "+dept)


if __name__ == '__main__':
    employee1 = Employee("Kumar","Quality")
   # print(employee1.name+" "+employee1.dept+" "+employee1.__salary)
    print(employee1)
  #  employee2 = Employee(name="Anil", dept="finance")
  #  print(employee2)
  #  #employee2.printdata()