import random

data=open("data.txt","w")
for i in range(10):
    num=random.randint(1,100)
    data.write(str(num)+",")
data.close()

data=open("data.txt","r")
even=open("even.txt","w")
odd=open("odd.txt","w")
prime=open("prime number.txt","w")

l=data.read().split(",")[:-1]

for i in l:
    
    if int(l)%2!=0:
        for i in range(3,int(l/2)+1,2):
            if l%i==0:
                print(i,"Number is not prime")
                break
            else:
                prime.write(i+",")
        else:
            print(i,"Number is not prime")
        
    if int(i)%2==0:
        even.write(i+",")
    else:
        odd.write(i+",")
        
data.close()
even.close()
odd.close()
prime.close()
