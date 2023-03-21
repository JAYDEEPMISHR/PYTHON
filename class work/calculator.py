import calculatorUDF

while True:
    
    print("#"*30)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulo")
    print("#"*30)



    choice=int(input("Enter your choice:"))

    if choice==1:
        print("You choose Addition")
        x=int(input("Enter value 1 :"))
        y=int(input("Enter value 2 :"))
        calculatorUDF.addition(x,y)
    
    elif choice==2:
        print("You choose Subtraction")
        x=int(input("Enter value 1 :"))
        y=int(input("Enter value 2 :"))
        calculatorUDF.subtraction(x,y)

    elif choice==3:
        print("You choose Multiplication")
        x=int(input("Enter value 1 :"))
        y=int(input("Enter value 2 :"))
        calculatorUDF.multiplication(x,y)

    elif choice==4:
        print("You choose Division")
        x=int(input("Enter value 1 :"))
        y=int(input("Enter value 2 :"))
        calculatorUDF.division(x,y)

    elif choice==5:
        print("You choose Modulo")
        x=int(input("Enter value 1 :"))
        y=int(input("Enter value 2 :"))
        calculatorUDF.modulo(x,y)

    else:
        print("Thank You for using this program")

    ans=input("Do you want to continue? (y/n):")
    ans=ans.lower()
    if ans!='y':
        break
    

    
