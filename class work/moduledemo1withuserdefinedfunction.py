import UDF

while True:
    print("*"*30)
    print("1. Odd Even")
    print("2. Max OF Two")
    print("3. Max of Three")
    print("4. Fibonacci")
    print("5. Prime Number")
    print("*"*30)

    choice=int(input("Enter Your choice from menu: "))

    if choice==1:
        n1=int(input("Enter Value: "))
        UDF.oddeven(n1)
        print("*"*30)
        
    elif choice==2:
        n1=int(input("Enter Value: "))
        n2=int(input("Enter Value: "))
        UDF.maxoftwo(n1,n2)
        print("*"*30)
    elif choice==3:
        n1=int(input("Enter Value: "))
        n2=int(input("Enter Value: "))
        n3=int(input("Enter Value: "))
        UDF.maxofthree(n1,n2,n3)
        print("*"*30)
    elif choice==4:
        n1=int(input("Enter Value: "))
        UDF.fibonacci(n1)
        print("*"*30)
    elif choice==5:
        n1=int(input("Enter Value: "))
        UDF.prime(n1)
        print("*"*30)
    else:
        print("Thank You")
