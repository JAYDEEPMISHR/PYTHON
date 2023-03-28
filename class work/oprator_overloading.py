# Operator_overloading & Magic method

#Class creation

class Point:
    def __init__(self,x,y):                   # Whenever object is created __init__ function is automatically called
        print("init called")
        self.x=x
        self.y=y

    def __str__(self):                  # Whenever object is print then __str__ function is called and return some string compulsory
        print("str called")
        return "({0},{1})".format(self.x,self.y)

    def __add__(self,obj):
        x=self.x+obj.x
        y=self.y+obj.y
        return Point(x,y)

p1=Point(11,33)
print(p1)
p2=Point(22,44)
print(p2)
print("Addiion of Objects: ",p1+p2)
