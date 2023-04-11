#Python program to read last n lines of a file.
"""
def LastNLines(f,n):
    with open(f) as file:
        print('Last',n,'lines from file :',file1)
        for line in (file.readlines()[-n:]):
            print(line,end='')

f=input("Enter a file name: ")
n=int(input("No. of last lines to read: "))
"""

file1=open("program 4.txt","w")         # Open a new text file named program 4.txt in write mode

# Write a data in file
L=["1. I love deadlines.I love the whooshing noise they make as they go by.\n",
   "2. There is no greater agony than bearing an untold story inside you.\n",
   "3. If there's a book that you want to read, but it hasn't been written yet, then you must write it.\n",
   "4. We write to taste life twice, in the moment and in retrospect.\n",
   "5. One day I will find the right words, and they will be simple.\n",
   "6. Fantasy is hardly an escape from reality. It's a way of understanding it.\n",
   "7. You must stay drunk on writing so reality cannot destroy you.\n",
   "8. Fiction is the truth inside the lie.\n",
   "9. The road to hell is paved with adverbs.\n"]

file1.writelines(L) # To print lines in L.
file1.close()

n = int(input("\nEnter Lines To Read(1-9): ")) # Take a input from user to how many lines they want to read
file1=open("program 3.txt","r")    # Open a program 3.txt file in read mode
for i in range(n):
	print(file1.readline())


