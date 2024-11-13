# python single_inheritance.py

# Program to create base class student and derived class test using single inhertance and
# display the marks of the student .

class Student:#common base class for all students
    def getData(self,rollno,name,course):
        self.rollno=rollno
        self.name=name
        self.course=course
    def displayStudent(self):
        print("Roll Number:",self.rollno)
        print("Name:",self.name)
        print("Course:",self.course) 

# Inheritance
class Test(Student):
    def getMarks(self,marks):
        self.marks=marks
    def displayMarks(self):
            print("total marks:",self.marks)
r = int(input("enter the roll number:"))
n = input("enter the name:")
c = input("enter the course name:")
m = int(input("enter the marks:"))

#creating the object
print("Result")
stud1=Test()
stud1.getData(r,n,c)
stud1.getMarks(m)
stud1.displayStudent()
stud1.displayMarks()