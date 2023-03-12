sname=input("ENTER STUDENT NAME : ")
rno=int(input("Enter Roll Number : "))
s1=int(input("Enter Marks of Subject 1: "))
s2=int(input("Enter Marks of Subject 2: "))
s3=int(input("Enter Marks of Subject 3: "))

total=s1+s2+s3
per=total/3

print("Student Name : ",sname)
print("Roll Number : ",rno)
print("Total : ",total)
print("Percentage : ",per)

if per>=70 :
    print("Distinction")
elif per>=60 :
    print("First Class")
elif per>=50 :
    print("Second Class")
elif per>=40 :
    print("Pass Class")
else:
    print("Fail")
    
        
