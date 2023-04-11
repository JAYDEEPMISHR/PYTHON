# Python program to copy the contents of a file to another file.

with open("program 1.txt",'r') as file:
    with open("program 2.txt",'w') as file1:
        for line in file:
            file1.write(line)


