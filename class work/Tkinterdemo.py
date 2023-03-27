from tkinter import *             # tkinter module
import mysql.connector            # mysql connector library(command in cmd= pip install mysql-connector-python)
import tkinter.messagebox as msg  # .messagebox.showinfo is a library of tkinter which shows data of written in box.

#Connect to server

def create_conn():                # Make a function to connect with server
    return mysql.connector.connect(      # mysql.connector.connect is a technique to connect your function with mysql database
            host="localhost",
            user="root",
            password="",
            database="python_5"
        )

# print(create_conn())              Check whether your object is created or not


# Insert data from registration form to database

def insert_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("Status","All fields are required")
    else:
        conn=create_conn()          # Call create_conn function and store into conn
        cursor=conn.cursor()
        query="insert into student(fname,lname,email,mobile) values(%s,%s,%s,%s)"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get())
        cursor.execute(query,args)  # To execute your query into mysql
        conn.commit()               # To save your data permanently to database table
        conn.close()
        e_fname.delete(0,'end')     # To delete data from text box only
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("Status","Your data saved successfully")
    



root=Tk()                         # Object creation
root.geometry("500x400")            # Set width & heigth of window 
root.title("My Registration form")
root.resizable(width=False,height=False)   # To hide maximize button from window

# Lable creation

l_id=Label(root,text="ID",font=("Arial",15))
l_id.place(x=50,y=50)

l_fname=Label(root,text="FIRST NAME",font=("Arial",15))
l_fname.place(x=50,y=100)

l_lname=Label(root,text="LAST NAME",font=("Arial",15))
l_lname.place(x=50,y=150)

l_email=Label(root,text="EMAIL",font=("Arial",15))
l_email.place(x=50,y=200)

l_mobile=Label(root,text="MOBILE",font=("Arial",15))
l_mobile.place(x=50,y=250)

# Text field entry

e_id=Entry(root)
e_id.place(x=200,y=50)

e_fname=Entry(root)
e_fname.place(x=200,y=100)

e_lname=Entry(root)
e_lname.place(x=200,y=150)

e_email=Entry(root)
e_email.place(x=200,y=200)

e_mobile=Entry(root)
e_mobile.place(x=200,y=250)

# Button creation

insert=Button(root,text="INSERT",font=("Arial",15),fg="White",bg="Blue",command=insert_data)
insert.place(x=50,y=285)

search=Button(root,text="SEARCH",font=("Arial",15),fg="White",bg="Blue")
search.place(x=140,y=285)

update=Button(root,text="UPDATE",font=("Arial",15),fg="White",bg="Blue")
update.place(x=240,y=285)

delete=Button(root,text="DELETE",font=("Arial",15),fg="White",bg="Blue")
delete.place(x=338,y=285)

