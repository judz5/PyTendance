from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding= 10)
frm.grid()
ttk.Label(frm, text = "Welcome to Attendance with PyTendance! |").grid(column=0, row=0)
ttk.Label(frm, text = "| This is how you will be logging into our PiCamera!").grid(column = 1, row = 0)
ttk.Button(frm, text = "     Click me if you aren't registered!     ", command = root.destroy).grid(column=0,row=1)
ttk.Button(frm, text = "Click me if you are registered and want to Sign in!", command = root.update_idletasks()).grid(column=1, row = 1)
root.mainloop()
