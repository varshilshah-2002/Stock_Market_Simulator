#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Nov 23, 2021 11:10:30 AM IST  platform: Windows NT

import sys
from classes.database import person_operations

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import profile_support

def vp_start_gui(user):
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (user,root)
    profile_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    profile_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self,user, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+468+138")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.0, rely=0.0, height=71, width=594)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 14")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''PROFILE''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.0, rely=0.244, height=31, width=154)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 14")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''EMAIL''')

        # self.Text1 = tk.Text(top)
        # self.Text1.place(relx=0.267, rely=0.244, relheight=0.076, relwidth=0.69)
        # self.Text1.configure(background="white")
        # self.Text1.configure(font="-family {Segoe UI} -size 14")
        # self.Text1.configure(foreground="black")
        # self.Text1.configure(highlightbackground="#d9d9d9")
        # self.Text1.configure(highlightcolor="black")
        # self.Text1.configure(insertbackground="black")
        # self.Text1.configure(selectbackground="blue")
        # self.Text1.configure(selectforeground="white")
        # self.Text1.configure(wrap="word")

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.0, rely=0.4, height=31, width=154)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(cursor="fleur")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 14")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''BALANCE''')

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.0, rely=0.556, height=21, width=154)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Segoe UI} -size 14")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''GAIN''')

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.0, rely=0.689, height=21, width=154)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Segoe UI} -size 14")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''EXPENSE''')

        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.267, rely=0.222, height=41, width=344)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font="-family {Segoe UI} -size 13")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text=user[0])

        self.Label7 = tk.Label(top)
        self.Label7.place(relx=0.25, rely=0.356, height=41, width=364)
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font="-family {Segoe UI} -size 13")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text=round(person_operations(user[0],1),2))

        self.Label8 = tk.Label(top)
        self.Label8.place(relx=0.3, rely=0.505, height=41, width=304)
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font="-family {Segoe UI} -size 13")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text=round(person_operations(user[0],3),2))

        self.Label9 = tk.Label(top)
        self.Label9.place(relx=0.25, rely=0.606, height=51, width=344)
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(font="-family {Segoe UI} -size 13")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(text=round(person_operations(user[0],5),2))

if __name__ == '__main__':
    vp_start_gui()





