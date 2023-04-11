# Hybrid inheritance

class A:                                       # Base/Parent class

    def getA(self,a):
        self.a=a
    def putA(self):
        print("A: ",self.a)


class B(A):                                    # Derived class from Class A

    def getB(self,b):
        self.b=b
    def putB(self):
        print("B: ",self.b)

class C(A):                                    # Derived class from Class A

    def getC(self,c):
        self.c=c
    def putC(self):
        print("C: ",self.c)

class D(B,C):                                   # Derived class from Class B&C

    def getD(self,d):
        self.d=d
    def putD(self):
        print("D: ",self.d)

# Object creation

d1=D()
d1.getA(10)
d1.getB(100)
d1.getC(200)
d1.getD(20)
d1.putA()
d1.putB()
d1.putC()
d1.putD()
