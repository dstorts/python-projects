from tkinter import *
from tkinter import ttk

root = Tk()

entry=ttk.Entry(root, width=30)
entry2=ttk.Entry(root, width=30, show='*')
entry.insert(0, 'Please enter name')
entry2.insert(0, 'pass')
button=ttk.Button(root, text='Enter')
lbltitle = ttk.Label(text='Our Title Here', font=(('Arial'),22))
lblname = ttk.Label(text='Your Name : ')
lblpass = ttk.Label(text='Your Pass : ')
lbltitle.grid(row=0, column=0, columnspan=2)#columnspan forces the widget to be sized to fit its cell in the grid
lblname.grid(row=1, column=0, sticky=W)#sticky allows you to bias the position in the specified cell of the grid
lblpass.grid(row=2, column=0, sticky=W)
entry.grid(row=1, column=1)
entry2.grid(row=2, column=1)
#button.grid(row=3, column=1, sticky=E+W) #can add compass directions to stretch a widget to touch each position
button.grid(row=3, column=1, sticky=E, pady=5) #adding padding along the y direction (alse exists padx)

cboxvar = IntVar()
cboxvar.set(0)
cbox = ttk.Checkbutton(root, text='Rememeber Me',variable=cboxvar).grid(row=4,column=0)

def callback():
    print("Your Name: " + entry.get())
    print("Your Pass: " + entry2.get())
    if cboxvar.get() == 1:
        print("Remember Me is selected")
    else:
        print("Remember Me is NOT selected")

button.config(command=callback)

root.geometry('500x450')
root.mainloop()