from tkinter import *

root=Tk()
label=Label(root,text='Hello Python')
#label['text']='Hello Tkinter'
label.config(text='Hello Tk Inter',fg='red')
label.config(bg='yellow',text='Hello Python I love you so much!')
label.config(wraplength='150')
label.config(font='Times 15')
label.pack()
root.geometry('300x250')



root.mainloop()
