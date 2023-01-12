import random
from tkinter import *
import pandas
data = pandas.read_csv("words_to_learn.csv")
to_learn = data.to_dict(orient="records")
current_card = {}
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
def is_known():
    to_learn.remove(current_card)
    data_1 = pandas.DataFrame(to_learn)
    data_1.to_csv("words_to_learn.csv")
    next_card()



window = Tk()
window.title("Flash card app")
window.config(bg="#B1DDC6", padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(height=526, width=800)
card_back_img = PhotoImage(file="card_back.png")
card_front_img = PhotoImage(file="card_front.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg="#B1DDC6", highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
cross_image = PhotoImage(file="wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0)
unknown_button.grid(row=1, column=0)
right_image = PhotoImage(file="right.png")
known_button = Button(image=right_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()
window.mainloop()
