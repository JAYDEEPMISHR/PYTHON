# FIBONACCI SERIES

n=int(input("Enter a Range: "))    #get input range from user
a,b=0,1                            #first term=0, second term=1
print(a, end=" ")
while b<n:
    print(b,end=" ")
    a,b=b,a+b                      # swapping function
