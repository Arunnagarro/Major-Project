from tkinter import *
from tkinter import messagebox
import mysql.connector
import os
import time
import Protect
import datetime as dt
import capture
import  log
#connecting to the database
db = mysql.connector.connect(host="localhost",user="root",passwd="18101997",database="login")
mycur = db.cursor()





def error_destroy():
    err.destroy()

def succ_destroy():
    succ.destroy()
    root1.destroy()

def error(err_info):
    global err
    err = Toplevel(root1)
    err.title("Error")
    err.geometry("200x100+550+300")
    Label(err,text=err_info,fg="red",font="bold").pack()
    Label(err,text="").pack()
    Button(err,text="Ok",bg="grey",width=8,height=1,command=error_destroy).pack()

def success():
    global succ
    succ = Toplevel(root1)
    succ.title("Success")
    succ.geometry("200x100+550+300")
    Label(succ, text="Registration successful...", fg="green", font="bold").pack()
    Label(succ, text="").pack()
    Button(succ, text="Ok", bg="grey", width=8, height=1, command=succ_destroy).pack()

def register_user():
    username_info = username.get()
    password_info = password.get()
    if username_info == "":
        error("please enter username")
    elif password_info == "":
        error("Please Enter Password")
    else:
        sql = "select * from login_info where username = %s and userpassword = %s"
        mycur.execute(sql,[(username_info),(password_info)])
        results = mycur.fetchall()
        if not results:
            sql = "insert into login_info (username,userpassword) values(%s,%s)"
            t = (username_info, password_info)
       
            
            root_encod=capture.capturephoto(username_info)
            if root_encod:
                mycur.execute(sql, t)
                db.commit()
                Label(root1, text="").pack()
                time.sleep(0.50)
                success()
        else:
            error("user exist.")



def registration():
    global root1
    root1 = Toplevel(root)
    root1.title("Registration Portal")
    root1.geometry("500x400+400+100")
    global username
    global password
    Label(root1,text="Register your account",bg="#3cdb0b",fg="black",font="bold",width=300).pack()
    username = StringVar()
    password = StringVar()
    Label(root1,text="").pack()
    Label(root1,text="Username :",font="bold").pack()
    Entry(root1,textvariable=username).pack()
    Label(root1, text="").pack()
    Label(root1, text="Password :").pack()
    Entry(root1, textvariable=password,show="*").pack()
    Label(root1, text="").pack()
    Button(root1,text="Register",bg="#0b92db",command=register_user).pack()

def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Log-In Portal")
    root2.geometry("500x400+400+100")
    global username_varify
    global password_varify
    Label(root2, text="Log-In Portal", bg="#3cdb0b", fg="black", font="bold",width=300).pack()
    username_varify = StringVar()
    password_varify = StringVar()
    Label(root2, text="").pack()
    Label(root2, text="Username :", font="bold").pack()
    Entry(root2, textvariable=username_varify).pack()
    Label(root2, text="").pack()
    Label(root2, text="Password :").pack()
    Entry(root2, textvariable=password_varify, show="*").pack()
    Label(root2, text="").pack()
    Button(root2, text="Log-In", bg="blue",fg="white",command=login_varify).pack()
    Label(root2, text="")

def logg_destroy():
    logg.destroy()
    root2.destroy()
    root.destroy()

def fail_destroy():
    fail.destroy()

def logged():
    global logg
    logg = Toplevel(root2)
    logg.title("Welcome")
    logg.geometry("720x560+300+50")
    Button(logg, text="Log-Out", bg="#9c9e9b", fg="white", width=8, height=1, command=logg_destroy).pack(side=TOP, anchor=NE)
    def update_clock():
        now = time.strftime("%H:%M:%S")
        label.config(text=str(now))
        logg.after(1000,update_clock)
    Label(logg, text="Welcome {} ".format(username_varify.get()), fg="green", font="bold,40").pack()
    Label(logg, text="").pack()
    Label(logg,text="you are logged in at "+f'{dt.datetime.now().time()}',fg="green" ,font="Times,24").pack()
    label =Label(logg,text="",fg="red",font="Times,20")
    label.pack()
    global user
    user=username_varify.get()
    update_clock()
    
    Button(logg, text="start camera", bg="green",fg="white",font=",35", width=15, height=3, command=start).place(relx=0.5, rely=0.5, anchor=CENTER)
    #Label(logg,text="press space to capture the photo " ,fg="red",font="bold,20").pack()
    Label(logg,text="press esc before logout to ensure camera is closed " ,fg="red",font="bold,20").pack()
    


def failed():
    global fail
    fail = Toplevel(root2)
    fail.title("Invalid")
    fail.geometry("200x100+550+300")
    Label(fail, text="Invalid credentials...", fg="red", font="bold").pack()
    Label(fail, text="").pack()
    Button(fail, text="Ok", bg="grey", width=8, height=1, command=fail_destroy).pack()
    

def start():    
    Protect.detect(user)
    



def login_varify():

    user_varify = username_varify.get()
    pas_varify = password_varify.get()
    #if user_varify=="":
    #    error("username is empty.")
    #if pas_varify=="":
    #    error("password is empty .")
    #if user_varify and pas_varify:
    sql = "select * from login_info where username = %s and userpassword = %s"
    mycur.execute(sql,[(user_varify),(pas_varify)])
    results = mycur.fetchall()
    
    if results:
        for i in results:
            global user
            logged()
            
           
            break
        
    else:
        failed()
    
    
      


def main_screen():
    global root
    root = Tk()
    root.title("WFH Detection Portal")
    root.geometry("720x560+300+50")
    Label(root,text="Welcome to Log-In Protal",font="bold",bg="#3cdb0b",fg="black",width=300).pack()
    Label(root,text="").pack()
    Button(root,text="Log-IN",width="8",height="1",bg="blue",fg="white",font="bold",command=login).place(x=325,y=200)
    Label(root,text="").pack()
    Button(root, text="Register",height="1",width="15",bg="#0b92db", fg="white",font="bold",command=registration).place(x=295,y=250)
    Label(root,text="").pack()
    Label(root,text="").pack()
    Label(root,text="Developed by Arun").pack(side=RIGHT, anchor=S)

main_screen()
root.mainloop()