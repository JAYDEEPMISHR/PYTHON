# Take input from user

x=int(input("Give value of X:"))
y=int(input("Give value of Y:"))
z=int(input("Give value of Z:"))

if x==y or y==z or z==x:
    print("sum=0")

else:
    print("sum=",x+y+z)
