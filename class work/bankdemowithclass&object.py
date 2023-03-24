class Bank:

    def openAccount(self,acno,cname,balance):
        self.acno=acno
        self.cname=cname
        self.balance=balance
        print("Hello ",self.cname," Your account number ",self.acno," is open with balance Rs.",self.balance)

    def deposite(self,amount):
        self.balance=self.balance+amount

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount

        else:
            self.needs=amount-self.blalance
            print("Soory, You need ",self.needs," Rs.to withdraw from your account")

    def checkBalance(self):
        print("Your current balance is",self.balance)

b1=Bank()

acno=int(input("Enter Your Account number: "))
cname=input("Enter Customer name: ")
balance=int(input("Enter Ammount: "))

b1.openAccount(acno,cname,balance)

while True:

    print("*"*30)
    print("1. Deposite")
    print("2. Withdraw")
    print("3. Check Your Balance")
    print("4. Exit")
    print("*"*30)

    choice=int(input("Enter Your Choice: ")
    
