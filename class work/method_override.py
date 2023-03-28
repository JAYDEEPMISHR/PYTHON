# Method Override

#class formation

class A:                                                # Parent class

    def show(self):
        print("Show from A")

class B(A):                                             # Child class

    def show(self):
        super().show()                              # Super().function_name method is used to solve the problem in methodoveriding.
        print("Show from B")

class C(B):                                             # Child class

    def show(self):
        super().show()
        print("Show from C")

#Object creation
        
c1=C()
c1.show()
