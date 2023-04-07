# Python program to read an entire text file

file1=open("program 1.txt","w")         # Open a new text file named program 1.txt in write mode

L=["This is my first file\n","Opening a new file\n","Delete an old file"] # Write a data in file

file1.writelines(L) # To print lines in L.
file1.close() 
