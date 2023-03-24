# Swap two numbers with temp vriable

a=int(input("Give value for A: "))            # Get input from user
b=int(input("Give value for B: "))

temp=a                                        # Logic for Swapping using temp. variable
a=b                                           
b=temp                                         

print("After swap value of A is :",a)
print("After swap value of B is :",b)

# Swap two numbers without temp vriable

a=int(input("Give value for A: "))            # Get input from user
b=int(input("Give value for B: "))

a,b=b,a                                       # Logic for Swapping without using temp. variable

print("After swap value of A is :",a)
print("After swap value of B is :",b)


