#import modules
 
from tkinter import *
import os
from Top_Gainers_and_Losers import vp_start_gui

#import files
from classes.database import *
 
# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("1600x1600")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="#808080",width="300", height="2", font=("Comic Sans MS", 18)).pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Email * ",height="2", width="32",font=("Comic Sans MS", 16))
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username, width="30", font=("Comic Sans MS", 12))
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ",height="2", width="32",font=("Comic Sans MS", 16))
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*', width="30", font=("Comic Sans MS", 12))
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", height="2", width="16", font=("Comic Sans MS", 12), command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("1600x1600")
    Label(login_screen, text="Please enter details below to login",width="300", height="2", font=("Comic Sans MS", 18)).pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Email * ",height="2", width="32",font=("Comic Sans MS", 16)).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify, width="30", font=("Comic Sans MS", 12))
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ",height="2", width="32",font=("Comic Sans MS", 16)).pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*', width="30", font=("Comic Sans MS", 12))
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", command = login_verify, height="2", width="16", font=("Comic Sans MS", 12)).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
    result = registerdb(username_info,password_info)
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    if result:
        Label(register_screen, text="Registration Success,please proceed to login", fg="green", font=("calibri", 11)).pack()
    else:
        Label(register_screen, text="User exists", fg="red", font=("calibri", 11)).pack()
        

 
    # file = open(username_info, "w")
    # file.write(username_info + "\n")
    # file.write(password_info)
    # file.close()
 
    
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    
    result = authenticate(username1,password1)
    print(result)

    if result == '0':
        user_not_found()
    elif result == '-1':
        password_not_recognised()
    else:
        login_sucess(result)
        

    # list_of_files = os.listdir()
    # if username1 in list_of_files:
    #     file1 = open(username1, "r")
    #     verify = file1.read().splitlines()
    #     if password1 in verify:
    #         login_sucess()
 
    #     else:
    #         password_not_recognised()
 
    # else:
    #     user_not_found()
 
# Designing popup for login success
 
def login_sucess(user):
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("200x200")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=lambda:delete_login_success(user)).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("250x250")
    Label(password_not_recog_screen, text="Invalid Password ",height="2", width="15", font=("Comic Sans MS", 13)).pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised,height="1", width="12", font=("Comic Sans MS", 11)).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("250x250")
    Label(user_not_found_screen, text="User Not Found",height="2", width="15", font=("Comic Sans MS", 13)).pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen,height="1", width="15", font=("Comic Sans MS", 12)).pack()
 
# Deleting popups
 
def delete_login_success(user):
    login_success_screen.destroy()
    login_screen.destroy()
    vp_start_gui(user)
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    width= main_screen.winfo_screenwidth() 
    height= main_screen.winfo_screenheight()
    #setting tkinter window size
    main_screen.geometry("%dx%d" % (width, height))
    # main_screen.geometry("1280x1280")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="#808080", width="300", height="2", font=("Comic Sans MS", 18)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="32", command = login, font=("Comic Sans MS", 14)).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="32", command=register, font=("Comic Sans MS", 14)).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()
