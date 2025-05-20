import pandas as pd
from tkinter import *
import random

BACKGROUND_COLOR = '#B1DDC6'
current_card={}
to_learn={}
try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv("data/Telugu_English_Freq - Sheet1.csv")
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')
'''source: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html
#print(data.to_dict())    #‘dict’ (default) : dict like {column -> {index -> value}}
#print(data.to_dict(orient='records'))   #‘records’ : list like [{column -> value}, … , {column -> value}]'''


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text="Telugu",fill="black")
    canvas.itemconfig(card_word, text=current_card['Telugu'],fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(card_word, text=current_card["English"],fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv",index = False)
    next_card()


window = Tk()
window.title("Flash Cards")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(width=600, height=400,highlightthickness=0)
card_front_img = PhotoImage(file="images/new_images_resized/card_front_compact.png")
card_back_img = PhotoImage(file="images/new_images_resized/card_back_compact.png")
card_background = canvas.create_image(300, 200, image=card_front_img)

card_title = canvas.create_text(300, 100, text="Title", font=("Arial", 24, "italic"))
card_word = canvas.create_text(300, 200, text="Word", font=("Arial", 36, "bold"))

canvas.config(bg=BACKGROUND_COLOR)

canvas.grid(row=0, column=0,columnspan=3)


wrong_img = PhotoImage(file ="images/Original_Images/wrong.png")
wrong_button = Button(image=wrong_img,highlightthickness=0,bd=0,command=is_known) #bd=0: Removes the 1–2 pixel sunken border that normally surrounds a Button widget.
wrong_button.grid(row=1,column=0)

right_img = PhotoImage(file ="images/Original_Images/right.png")
right_button = Button(image=right_img,highlightthickness=0,bd=0,command=next_card)
right_button.grid(row=1,column=2)

next_card()
window.mainloop()
