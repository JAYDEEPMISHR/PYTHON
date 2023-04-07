# Python program to count the number of lines in a text file.

with open("program 1.txt") as f:
    lines=len(f.readlines())
    print("Total number of lines: ",lines)
