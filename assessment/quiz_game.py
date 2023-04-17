# Python has a built-in package called json, which can be used to work with JSON data.
import json
# Python Random module is an in-built module of Python which is used to generate random numbers. 
import random

user = []

				
print("\t\t\tWELCOME TO TOPS QUIZ GAMING CHALLENGE\n")
print("\t\t\tSelect Your Role\n")
print("\n")
print("\t\t\t-> Quiz Master (press 1)")
print("\t\t\t-> Quiz Cracker (press 2)")
print("\n")

Role=int(input("Select Your Role: ")) # Take input from user
print(Role)
if Role==1:
    print("\t\tWELCOME MASTER")
    print("SHAKE YOUR BRAIN AND ADD SOME CHALLENGING QUESTIONS..")
    print("\n")
    print("\t\t\tMENU")  
    print("press 1 for add questions")
    print("press 2 for view questions")
    print("press 3 for delete questions")
    print("press 4 for exit")
    operation=int(input("Which operation you want to perform? "))

    if operation==1:
        print('\n==========ADD QUESTIONS==========\n')
        ques = input("Enter the question that you want to add:\n")
        opt = []
        print("Enter the 4 options with character initials (A, B, C, D)")
        for _ in range(4):
                opt.append(input())
        ans = input("Enter the answer:\n")
        with open("assets/questions.json", 'r+') as f:
                questions = json.load(f)
                dic = {"question": ques, "options": opt, "answer": ans}
                questions.append(dic)
                f.seek(0)
                json.dump(questions, f)
                f.truncate()
                print("Question successfully added.")
