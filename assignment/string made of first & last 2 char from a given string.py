"""
Python program to get a string made of the first 2 and the last 2 chars from a given a string.
If the string length is less than 2, return instead of the empty string.
"""


def string(str1):                                   # Define string function

    if len(str1)<2:
        return ""


    else:
        return str1[:2]+ str1[-2:]

my_string=input("Enter a String: ")
print("New Modified string is: ",string(my_string))
