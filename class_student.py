# python class_student.py

# Write a python script to define a class student having members roll no, name, age, 
# gender. Create a subclass called Test with member marks of 3 subjects. Create three 
# objects of the Test class and display all the details of the student with total marks.

class student :
    def StudentgetDAta(self,roll_no,name,age,gender)
    roll_no = int(input("enter the Roll no = "))
    name = str(input("Enter the Name = "))
    age = int(input("enter the Age = "))
    gender = str(input("Enter the Gender = "))
    
    displayStudent()

class Test :
    def Marks(self,Maths,English,Science):
        Maths = int(input("Maths marks = "))
        English = int(input("English Marks = "))  
        Science = int(input("Science Marks = "))

    # creating a object 
    print("Result")  
       