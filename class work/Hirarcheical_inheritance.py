# Hirarcheical inheritance

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

class D(A):                                    # Derived class from Class A

    def getD(self,d):
        self.d=d
    def putD(self):
        print("D: ",self.d)

# Object creation

b1=B()
c1=C()
d1=D()
b1.getA(10)
b1.getB(100)
c1.getC(200)
d1.getD(20)
b1.putA()
b1.putB()
c1.putC()
d1.putD()
