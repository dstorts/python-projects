import tkinter as t
from tkinter import PhotoImage
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FOREIGN = "French"
LANGUAGE_DOMESTIC = "English"
TITLE_FONT = ('Arial', 40, 'italic')
WORD_FONT = ('Arial', 60, 'bold')

to_learn = {}
current_card = {}
try:
    data = pandas.read_csv("data/french_words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records") #use orient=records because this makes every item in the generated list a keyed dictionary, i.e. every item in the list can be indexed with 'French' or 'English' respectively
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    current_card = random.choice(to_learn)
    #print(type(to_learn))
    #print(current_card['English'])
    flashcard.itemconfig(card_title, text=LANGUAGE_FOREIGN, fill='black')
    flashcard.itemconfig(card_word, text=current_card['French'], fill='black')
    flashcard.itemconfig(card_img, image=img_card_front)
    screen.after_cancel(flip_timer)
    flip_timer = screen.after(3000, func=flip_card)

def flip_card():
    flashcard.itemconfig(card_title, text="English", fill='white')
    flashcard.itemconfig(card_word, text=current_card['English'], fill='white')
    flashcard.itemconfig(card_img, image=img_card_back)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/french_words_to_learn.csv", index=False)
    next_card()

screen = t.Tk()
screen.title("Japanese Frequency Words Flash Cards")
screen.config(bg=BACKGROUND_COLOR, padx=20, pady=20, width=860, height=700)

flip_timer = screen.after(3000, func=flip_card)

img_card_front = PhotoImage(file='images/card_front.png')
img_card_back = PhotoImage(file='images/card_back.png')
img_right = PhotoImage(file='images/right.png')
img_wrong = PhotoImage(file='images/wrong.png')

flashcard = t.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_img = flashcard.create_image(400, 263, image=img_card_front)
card_title = flashcard.create_text(400, 150, text=LANGUAGE_FOREIGN, font=TITLE_FONT)
card_word = flashcard.create_text(400, 250, text='word', font=WORD_FONT)
flashcard.grid(row=0, column=0, columnspan=2)

dont_know_btn = t.Button(image=img_wrong, command=next_card,  highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0)
dont_know_btn.grid(row=1, column=0)

know_btn = t.Button(image=img_right, command=is_known,  highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0)
know_btn.grid(row=1, column=1)

next_card()

screen.mainloop()