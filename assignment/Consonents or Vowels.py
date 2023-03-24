# Check given character is vowel or consonent

n=input("Type one character(a-z,A-Z): ")                  # Get input from user
n=n.lower()                                               # Converts UPPERCASE to lowercase                             

if (n=="a" or n=="e" or n=="i" or n=="o" or n=="u"):
    print("The given letter is vowel")

else:
    print("The given letter is consonent")
