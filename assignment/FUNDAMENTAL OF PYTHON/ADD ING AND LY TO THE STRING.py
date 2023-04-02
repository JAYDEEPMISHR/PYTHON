# Python program to add 'ing' at the end of a given string(length should be at least 3). If the given string already ends with 'ing'then add 'ly' instead. If the string length of the given string is lessthan 3, leave it unchanged.

my_string = input("enter a string: ")


if len(my_string) < 3:
    new_string = my_string
    
elif my_string[-3:] == 'ing':
    new_string = my_string + 'ly'
    
else:
    new_string = my_string + 'ing'
    
print (new_string)
