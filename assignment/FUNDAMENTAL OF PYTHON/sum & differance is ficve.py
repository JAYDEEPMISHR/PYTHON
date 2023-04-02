# Take input from user 

x=int(input("Give value of X:"))
y=int(input("Give value of Y:"))

if x==y or x+y==5 or abs(x-y)==5:   # IF value of X and Y is equal or their sum or subtraction is 5 the output will return zero
    print("True")

else:
    print("False")
