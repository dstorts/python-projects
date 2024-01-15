from tkinter import *

MILES_TO_KILOMETER_COEFFICIENT = 1.609

def convert_it():
    a = float(entry_input.get())
    b = '%.2f'%(a*MILES_TO_KILOMETER_COEFFICIENT)
    #print(b)
    #print(type(b))
    label_answer.config(text=b)

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=400, height=200)

entry_input = Entry(font=("Ubuntu",24), width=15)
entry_input.grid(row=0, column=1)

label_miles = Label(text="Miles",font=("Ubuntu",24))
label_miles.grid(row=0, column=2)

label_equal_to = Label(text="is equal to ",font=("Ubuntu",24))
label_equal_to.grid(row=1, column=0)

label_answer = Label(text="0",font=("Ubuntu",24))
label_answer.grid(row=1, column=1)

label_kilo = Label(text="Km",font=("Ubuntu",24))
label_kilo.grid(row=1, column=2)

btn_calc = Button(text="Calculate", command=convert_it,font=("Ubuntu",24))
btn_calc.grid(row=2, column=1)



window.mainloop()