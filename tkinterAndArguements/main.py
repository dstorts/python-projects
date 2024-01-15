from tkinter import *
#using an astrisk allows us to initialize using classes from that module without writing the module name out
#e.g. now we can write 'window = Tk()' instead of 'window = tkinter.Tk()'

def btn_clicked():
    print("I got clicked")
    my_label.config(text="I got Clicked")

window = Tk()
window.title("My Second GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=30)

my_label = Label(text="I'm a label", font=("Courier New", 24, "bold"))
#my_label.place(x=0,y=0)
my_label.grid(column=0, row=0)

btn = Button(text="Click me", command=btn_clicked)
btn.grid(column=1,row=0,padx=40)

# for X in range(15):
#     for Y in range(15):
#         new_btn = Button(text="M")
#         new_btn.grid(column=X+2, row=Y)

#several ways to change attributes in a tkinter asset
#my_label["text"] = "New Text Yo"
#my_label.config(text="Hi there!")


window.mainloop()


