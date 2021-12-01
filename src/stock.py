import sys
from tkinter import Label

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

import profile1_support
import classes.net_connect
import Stock_Price_Name

def stock(email,symbol,obj,top):
    # price = classes.net_connect.get_quote(symbol)

    # obj.Label1 = tk.Label(top)
    # obj.Label1.place(relx=0.133, rely=0.156, height=41, width=414)
    # obj.Label1.configure(background="#d9d9d9")
    # obj.Label1.configure(disabledforeground="#a3a3a3")
    # obj.Label1.configure(font="-family {Segoe UI} -size 14")
    # obj.Label1.configure(foreground="#000000")
    # obj.Label1.configure(text="Value of "+symbol+" stock is "+str(price))
    #Gets chart
    classes.net_connect.get_chart(symbol)
    Stock_Price_Name.vp_start_gui(email,symbol)
    

def vp_start_gui(mail):
    '''Starting point when module is the main routine.'''
    global val, w, root
    email = mail
    root = tk.Tk()
    top = Toplevel1 (email,root)
    profile1_support.init(root, top)
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
    profile1_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self,email, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+468+138")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.133, rely=0.156, height=41, width=414)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 14")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''BUY/SELL''')

        self.TButton1 = ttk.Button(top)
        self.TButton1.place(relx=0.35, rely=0.578, height=35, width=156)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''CHECK STATUS''',command=lambda:(stock(email,self.Text1.get("1.0",'end-1c'),self,top)))

        self.Text1 = tk.Text(top)
        self.Text1.place(relx=0.15, rely=0.422, relheight=0.076, relwidth=0.673)
        self.Text1.configure(background="white")
        self.Text1.configure(font="-family {Segoe UI} -size 14")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="blue")
        self.Text1.configure(selectforeground="white")
        self.Text1.configure(wrap="word")

if __name__ == '__main__':
    vp_start_gui()





