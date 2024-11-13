## python Cricle_area_and_volume.py

#  Define an abstract class shape and its subclass / circle). The subclass has an init function
#  which takes an argument (length/radius) Both classes have an area & volume function which can
#  print the area and volume of shape where the area of shape by default 0.   

from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        self.area = 0

    @abstractmethod
    def area(self):
        pass

    def volume(self):
        print("Volume of a 2D shape is 0.")

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        self.area = 3.14159 * self.radius * self.radius
        print("Area of the circle:", self.area)