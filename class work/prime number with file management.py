import random

data=open("myfile.txt","w")
for i in range(10):
    num=random.randint(1,300)
    data.write(str(num)+",")
data.close()

data=open("myfile.txt","r")
primeno=open("prime_number.txt","w")

l=data.read().split(",")[:-1]

for i in int([l]):
    
    if int[(l)]%2!=0:
        for i in range(3,int(l/2)+1,2):
            if l%i==0:
                print(i,"Number is not prime")
                break
            else:
                prime_number.write(i+",")
        else:
            print(i,"Number is not prime")
primeno.close()
        
    
        
