#Python program to read a file line by line and store it into a list

with open("program 1.txt") as f:
    content_list=f.readlines()
print(content_list)

#remove new line characters
content_list = [x.strip() for x in content_list]
print(content_list)

