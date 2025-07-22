from time import process_time_ns


class Employee:
    org = "Wipro"

    @staticmethod
    def getOrgDetails():
        dept="Finance"
        print("Org details :", Employee.org)

    @staticmethod
    def test():
        print("Hello")

    def __init__(self, name, dept,salary):
        self.name = name
        self.dept = dept
        self.salary = salary
    def __str__(self):
        return f"Name={self.name}, dept={self.dept}, salary={self.salary}"

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.name == other.name and self.dept == other.dept and self.salary == other.salary
        return False

    def __hash__(self):
       return 1001

    def __gt__(self, other):
        return self.salary < other.salary


if __name__ == "__main__":
    emp1 = Employee("Kishore","Finance",20000)
    emp2 = Employee("Anil","Development",10000)
    emp3 = Employee("Mahesh","Development",70000)
    emp4 = Employee("Balu","Quality",40000)
    emp5 = Employee("Naren","HR",60000)
    emp6 = Employee("Kishore","Finance",20000)
    employee_data = {}
    employee_data[emp1] = "Manager"
    employee_data[emp2] = "Lead"
    employee_data[emp3] = "Developer"
    employee_data[emp4] = "Executive"
    employee_data[emp5] = "Manager"
    Employee.org="Wipro Technologies"
    print("emp1 = The org class value is :",emp1.org)
    print("emp2 - The org class value is :",emp2.org)
    Employee.getOrgDetails()
    Employee.test()

    print("The hashc ode of emp1",hash(emp1))

    for emp,item in employee_data.items():
        print(emp,item)
    employee_list = [emp1,emp2,emp3,emp4,emp5,emp6]
    sorteddata = sorted(employee_list)
    print("Employees in Sorted order of their salaries")
    for emp in sorteddata:
        print(emp)






