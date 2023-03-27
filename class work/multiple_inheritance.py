# Multiple inheritance

class A:                                       # Base/Parent class-1

    def getA(self,a):
        self.a=a
    def putA(self):
        print("A: ",self.a)


class B:                                       #Base/Parent class-2 

    def getB(self,b):
        self.b=b
    def putB(self):
        print("B: ",self.b)

class C(A,B):                                    # Derived class from Class A&B

    def getC(self,c):
        self.c=c
    def putC(self):
        print("C: ",self.c)

# Object creation

b1=C()
b1.getA(10)
b1.getB(100)
b1.getC(200)
b1.putA()
b1.putB()
b1.putC()
