## python Multiple_inheritance.py

# Program to create base class student and derived class test using multiple inhertance and
# display the marks of the student .

class Student:
# common base class for all students
    def getData(self,rollno,name,course):
        self.rollno=rollno
        self.name=name
        self.course=course
    def displayStudent(self):
        print("Roll Number :",self.rollno)
        print("name:",self.name)
        print("course name:",self.course)

# Inheritance
class Test(Student):
    def getMarks(self,marks):
        self.marks=marks
    def displaymarks(self):
        print("Total Marks:",self.marks)

class Sports:
    def getSportsMarks(self,spmarks):
        self.spmarks=spmarks
    def diplaySportMarks(self):
        print("Sports Marks:",self,self.spmarks)

# Multiple Inheritance
class Result(Test,Sports):
    def calculateGrade(self):
        m=self.marks+self.spmarks
        if m>480:self.grade="Distinction"
        elif m>360:self.grade="First Class"
        elif m>240:self.grade="Second Class"
        else:self.grade="Failed"
        print("Result:",self.grade)

# Main Program
r = int(input("enter the Roll number:"))
n = input("enter the name:")
c= input("enter the course name:")
m = int(input("Enter the Marks:"))
s = int(input("enter the Sports marks:"))
stud1=Result() #instance of child
stud1.getData(r,n,c)
stud1.getMarks(m)
stud1.getSportsMarks(s)
stud1.displayStudent()
stud1.displaymarks()
stud1.diplaySportMarks()
stud1.calculateGrade()
