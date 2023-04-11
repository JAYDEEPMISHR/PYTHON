#Sigle Inheritance


class A:                                       # Base/Parent class

    def getA(self,a):
        self.a=a
    def putA(self):
        print("A: ",self.a)


class B(A):                                    # Derived class

    def getB(self,b):
        self.b=b
    def putB(self):
        print("B: ",self.b)
        
b1=B()
b1.getA(10)
b1.getB(100)
b1.putA()
b1.putB()
