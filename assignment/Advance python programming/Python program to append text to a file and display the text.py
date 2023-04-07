#Python program to append text to a file and display the text.

file1=open("program 2.txt","w")         # Open a new text file named program 2.txt in write mode

L=["This is my first file\n","Opening a new file\n","Delete an old file"] # Write a data in file

file1.writelines(L) # To print lines in L.
file1.close()

file1=open("program 2.txt","a")     # Open a program 2 file in append mode to add some new text
file1.write("\n")
file1.write("This is good")
file1.close()
