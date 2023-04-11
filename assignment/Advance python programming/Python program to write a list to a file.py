# Write a Python program to write a list to a file.

# list of names
names = ['JAYDEEP', 'HIMANSHU', 'GABBAR']

# open file in write mode
with open('program 1.txt','w') as fp:
    for item in names:
        # write each item on a new line
        fp.write("%s\n" % item)
    print('Done')
