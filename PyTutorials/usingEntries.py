import tkinter
from tkinter import *
from tkinter import ttk

root=Tk()
entry=ttk.Entry(root, width='30')
entry2=ttk.Entry(root, width='30')

entry.insert(0,'Please enter your name')
entry2.config(show='*')
entry2.insert(0,'Enter your pass please')

def callback():
    val1=entry.get()
    val2=entry2.get()
    print('Your name is ' + val1)
    print('Your password is ' + val2)

button=tkinter.Button(root, width='20', text='Submit',command=callback)

entry.pack()
entry2.pack()
button.pack()

entry.state(['disabled'])
entry.state(['!disabled'])
entry2.state(['readonly'])

root.geometry('300x300')


root.mainloop()