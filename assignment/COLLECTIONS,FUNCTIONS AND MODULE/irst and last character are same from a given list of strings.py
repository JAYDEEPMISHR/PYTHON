"""
Python program to count the number of strings where the string length is 2 or more and
the first and last character are same from a given list of strings.
"""

s=0
list1=['aba','123','abc','aba']

for x in list1:
    
    if len(x)>1 and x[0]==x[-1]:
        print("The given words are:",x)
        s=s+1
    
    else:
        print("No. of words:",s)
