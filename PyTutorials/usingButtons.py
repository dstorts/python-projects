from tkinter import *

root=Tk()

def callback():
    label.config(text='You clicked me',fg='yellow', bg='red') #change the label text when the button is clicked

label=Label(root,text='Hello Py') #assign this label to the root window
label.pack()#make the label visible

button=Button(root, text='Click Me', command=callback)#run the callback function when the button is clicked
button.pack()
button['state']='disabled' #disable the button
button['state']='normal' #enable the button

root.geometry("350x300")
root.mainloop()
