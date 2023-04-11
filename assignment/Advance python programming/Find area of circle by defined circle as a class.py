<<<<<<< HEAD
"""Write a Python class named Circle constructed by a radius and
two methods which will compute the area and the perimeter of a circle"""

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

NewCircle = Circle(8)
print(NewCircle.area())
print(NewCircle.perimeter())
=======
"""Write a Python class named Circle constructed by a radius and
two methods which will compute the area and the perimeter of a circle"""

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

NewCircle = Circle(8)
print(NewCircle.area())
print(NewCircle.perimeter())
>>>>>>> 763f7713ac1725ba7d2beafc214de1da0bafd124
