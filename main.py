
list_of_len=len([1, 2, 3, 4,5])

print(list_of_len)

list_of_sum=sum([1,2,5,7,9])

print(list_of_sum)

list_of_max=max([1, 2, 3, 10,5])

print(list_of_max)

import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
circle=Circle(5)

print("Area of shape",circle.area())

        