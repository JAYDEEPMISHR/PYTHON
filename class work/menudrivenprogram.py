Amount=0
price=0
totalAmount=0
quantity=1

print("==========MENU===========")
print("1. Pizza  Price=180Rs/pcs")
print("2. Burger Price=100Rs/pcs")
print("3. Dosa   Price=80Rs/pcs")
print("4. Idli   Price=50Rs/pcs")
print("=========================")

choice=int(input("Enter Your Choice From Menu(1 to 4): "))

while choice>0:
    
    if choice==1:
        print("********You Choose Pizza********")
        quantity=int(input("How many Pieces? : "))
        price=180
        amount=price*quantity
        print(amount)
        
    
    elif choice==2:
        print("********You Choose Burger********")
        quantity=int(input("How many Pieces? : "))
        price=100
        amount=price*quantity
        print(amount)        
        

    elif choice==3:
        print("********You Choose Dosa********")
        quantity=int(input("How many Pieces? : "))
        price=80
        amount=price*quantity
        print(amount)        
        

    elif choice==4:
        print("********You Choose Idli********")
        quantity=int(input("How many Pieces? : "))
        price=50
        amount=price*quantity
        print(amount)        
        
    else:
        print("Thank You")
        
    totalAmount=totalAmount+amount
    print("Total Amount= ",totalAmount)
        
    ans=input("Do you want to continue? (y/n):")
    ans=ans.lower()
    if ans!='y':
        break
        

    
