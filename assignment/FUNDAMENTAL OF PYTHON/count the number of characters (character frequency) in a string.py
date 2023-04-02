# Program to count the number of characters (character frequency) in a string

from collections import Counter

string=input("Write string:")
res= Counter(string)
print("Count of all characters in Given stirng is:\n"+ str(res))
