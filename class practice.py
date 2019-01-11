class Employee:
    empcount = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empcount =Employee.empcount+1

    def employeecount(self):
        print("Total employees %d" % Employee.empcount)

    def displayemployee(self):
        print("name:",self.name,", salary:",self.salary)

p1 = Employee("ram",35000)
p2 = Employee("rai",30000)

p1.displayemployee()
p2.displayemployee()
print("Total employees %d" % Employee.empcount)


