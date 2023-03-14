s=input("Enter a String= ")

ch=0
wd=1
sp=0
dg=0
sc=0

for i in s:
    if i.isalpha():
        ch=ch+1
    elif i.isspace():
        sp=sp+1
        wd=wd+1
    elif i.isdigit():
        dg=dg+1
    else:
        sc=sc+1

print("Total words: ",wd)
print("Total characters: ",ch)
print("Total space: ",sp)
print("Total digit: ",dg)
print("Total special character: ",sc)
