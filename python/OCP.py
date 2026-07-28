
#Solid Principles
#2.Open closed principle
#violation code

from math import pi

class Shape:
    def __init__(self, shape_type, **kwargs):
        if shape_type == "Rectangle":
            self.width = kwargs["width"]
            self.height = kwargs["height"]
        elif shape_type == "Circle":
            self.radius = kwargs["radius"]
        else:
            raise TypeError("Unsupported shape type")
    def calculateArea(self):
        if self.shape_type == "Rectangle":
            return self.width * self.height
        elif self.shape_type == "Circle":
            return pi* self.radius**2
        else:
            raise TypeError("Unsupported File Type")


#Fix Code

from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type
    @abstractmethod
    def calculate_area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height ):
        super().__init(self, "Rectangle")
        self.width= width
        self.height= height
    def calculate_area(self):
        return self.width * self.height
class Circle(Shape):
    def __init__(self,radius):
        super().__init__(self, "Circle")
        self.radius = radius
    def calculate_area(self):
        return pi*self.radius**2


    