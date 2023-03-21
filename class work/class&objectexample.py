class Student:                              #class is created

    def getdata(self,fname,lname):           #1st function is created
        self.fname=fname
        self.lname=lname

    def putdata(self):                       # 2nd function is created
        print("First name: ",self.fname)
        print("Last name: ",self.lname)


A=Student()                                 #Object is created

A.getdata("Jaydeep","Mishra")
A.putdata()
