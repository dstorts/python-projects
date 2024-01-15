from tkinter import *
from tkinter import ttk

root=Tk()
root.geometry('500x450')#specify the dimensions of the root window

button1 = Button(root, text='Click Me')#right side adds the button to the gui window
button2 = ttk.Button(root, text='Click Me')
button1.pack()#allows the button to show up after being created
button2.pack()


root.mainloop()