# User defined function with no arguments and no return value

def printline():
    print("*"*60)
printline()
print("\t\tWelcome to Python")
printline()

# User defined function with arguments and no return value.

def sub(j,k):
    print("Subtraction: ",j-k)
printline()
x=int(input("Enter value: "))         # Get values from user
y=int(input("Enter value: "))
sub(x,y)
#sub(100,50)        #Give direct value 
printline()

# User defined function with arguments and return value.

def add(a,b):
    return a+b

printline()
x=int(input("Enter value: "))         # Get values from user
y=int(input("Enter value: "))
ans=add(x,y)                          # Store a value at other place, which is used whenever it is needed
print("Addition: ",ans)
print("Addition: ",add(x,y))          # Direct store a value, which is not used anywhere saperately. 
printline()
