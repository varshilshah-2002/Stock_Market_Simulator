from tkinter import *
from classes.database import *

def history_gui(user):

        root =Tk()
        lst = [('Email','Date','Symbol','Transaction Type','Unit Cost')]+display_history(user[0])

        total_rows = len(lst)
        total_columns  = 5
        for i in range(total_rows):
                for j in range(total_columns):
                        e=Entry(
                                root,
                                width = 20,
                                fg = "blue",
                                font = ("Arial",16,'bold')
                                )
                        e.grid(row=i, column = j)
                        e.insert(0,lst[i][j])
        root.mainloop()
