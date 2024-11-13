# python class_animal_dog_inheritance.py

# Define a class Animal with methods sound() and move(). 
# Create a class Dog that inherits from Animal and overrides 
# the sound() method to print "Woof!". Instantiate a Dog object and call both
#  sound() and move() methods.

class Animal:
    def sound(self):
        print("Animal sound")
    def move(self):
        print("Animal move")            
class Dog(Animal):
        def sound(self): 
            print("Woof!")

my_dog = Dog()
my_dog.sound()
my_dog.move()
