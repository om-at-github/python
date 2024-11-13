# python class_employee_inhertance.py

#  Define a class Employee having members id, name, department, salary. Create a 
#  subclass called manager with member bonus. Define methods accept and display in 
#  both the classes. Create n objects of the manager class and display the details of the 
#  manager having the maximum total salary (salary+bonus).

class Employee:
    def __init__(self, id, name, department, salary):
        self.id = id
        self.name = name
        self.department = department
        self.salary = salary
        
    def accept(self):
        self.id = int(input("Enter id: "))
        self.name = input("Enter name: ")
        self.department = input("Enter department: ")
        self.salary = int(input("Enter salary: "))
            
    def display(self):
        print("Id: ", self.id)
        print("Name: ", self.name)
        print("Department: ", self.department)
        print("Salary: ", self.salary)

class manager(Employee):
    def __init__(self, id, name, department, salary, bonus):
        self.id = id
        self.name = name
        self.department = department
        self.salary = salary
        self.bonus = bonus

    def acceptM(self):
        self.id = int(input("Enter id: "))
        self.name = input("Enter name: ")
        self.department = input("Enter department: ")
        self.salary = int(input("Enter salary: "))
            
    def displayM(self):
        print("Id: ", self.id)
        print("Name: ", self.name)
        print("Department: ", self.department)
        print("Salary: ", self.salary)


emp1 = Employee(1, "Rahul1", "ITa", 100009)
emp2 = Employee(2, "Rahul2", "ITb", 100008)
emp3 = Employee(3, "Rahul3", "ITc", 100007)
emp4 = Employee(4, "Rahul4", "ITd", 100006)
emp5 = Employee(5, "Rahul5", "ITe", 100005)
emp6 = Employee(6, "Rahul6", "ITf", 100004)
emp7 = Employee(7, "Rahul7", "ITg", 100003)
emp8 = Employee(8, "Rahul8", "ITh", 100002)
emp9 = Employee(9, "Rahul9", "ITi", 100001)
emp10 = Employee(10, "Rahul10", "ITjj", 1000011)


emp1.display()
emp2.accept()
emp3.display()
