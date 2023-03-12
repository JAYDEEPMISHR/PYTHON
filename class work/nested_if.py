a=int(input("ENTER A: "))
b=int(input("ENTER B: "))
c=int(input("ENTER C: "))

if a>b:
    if a>c:
        print("A is Greater Number")
    else:
        print("C is Greater Number")
elif b>c:
    print("B is Greater Number")
else:
    print("C is Greater Number")
