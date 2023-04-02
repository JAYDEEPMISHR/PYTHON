# Give reverse string when given string is Multiple of 4

def check_string(data):

    if len(data)%4==0:
        return data[::-1]
    return data

text=input("Enter string: ")            # Take a input from user
result= check_string(text)
print("Final String is: ",result)
