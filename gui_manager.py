from tkinter import *
from tkinter import messagebox
import func.py
#import func

win = Tk()
win.geometry('200x200')
win.title('PyTendance')

def hold():
    pass

def get_name():
    name = name_Tf.get()
    return name

# def takePhoto():
#     messagebox.showinfo('information', get_name())

Label(win, text="Enter Name").pack()
name_Tf = Entry(win)
name_Tf.pack()

Button(win, text='Check Attendance', command=hold).pack()

Button(win, text='New User', command=takePhoto).pack()


win.mainloop()