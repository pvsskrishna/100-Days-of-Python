import tkinter

from bokeh.models import Label
from spyder.plugins.completion.providers.kite.utils.status import check_if_kite_installed

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1 #25
SHORT_BREAK_MIN = 1#5
LONG_BREAK_MIN = 1#20
reps = 0
# Global variable used to store the reference to the `after()` timer event.
# This allows us to access or cancel the timer from multiple functions.
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    window.after_cancel(timer)
    check_mark_label.config(text="")
    timer_label.config(text="Timer")
    canvas.itemconfig(count_label,text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # if reps is 8th:
    if reps % 8 == 0:
        timer_label.config(text='Long Break', fg=RED)
        count_down(long_break_sec)

    # if reps is 1st/3rd/5th/7th:
    elif reps % 2 == 1:
        timer_label.config(text='Work Time', fg=GREEN)
        count_down(work_sec)

    # if reps is 2nd/4th/6th:
    elif reps % 2 == 0:
        timer_label.config(text='Short Break', fg=PINK)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = count // 60  # we can also write this as math.floor(count/60) by importing math module.
    count_sec = count % 60

    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(count_label, text=f"{count_min}:{count_sec}")
    #itemconfig method is used to config the items on the canvas,
    #we don't use config method because it is used to config the components

    if count > 0:
        global timer
        timer = canvas.after(1000,count_down,count-1)
        print(count)
        #"after" a function from tkinter module canvas class.
        # It is used to execute the function after certain ms(milli seconds) of time is completed.

    else:
        start_timer()
        # for every 2 reps we are completing one work session(i.e work + short break)
        # So, we will create one check ✔ mark after 2 reps
        work_sessions = reps//2
        marks = ""
        for _ in range(work_sessions):
            marks += "✔"
        check_mark_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
#Creating window
window = tkinter.Tk()
window.title("Pomodoro")  # which means Tomato in Italian 🍅
window.config(padx=100,pady=50,bg=YELLOW)

#creating canvas
canvas = tkinter.Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
    #use highlightthickness=0 parameter to make the image boarders to blend with bg or to hide the borders

tomato_img = tkinter.PhotoImage(file=r"./tomato.png")
    #use relative path of image if it is in another folder

canvas.create_image(100,112,image=tomato_img)
count_label = canvas.create_text(102,132,text="00:00",font=(FONT_NAME,25,"bold"),fill="white")
canvas.grid(column=2,row=2)

start_button = tkinter.Button(text="Start",width=6,font=(FONT_NAME,12,"bold"),command=start_timer)
start_button.grid(column=1,row=3)

reset_button = tkinter.Button(text="Reset",width=6,font=(FONT_NAME,12,"bold"),command=timer_reset)
reset_button.grid(column=3,row=3)

timer_label = tkinter.Label(text='Timer',font=(FONT_NAME,30,"bold"),fg=GREEN,bg=YELLOW) #fg=foreground
timer_label.grid(column=2,row=1)

check_mark_label = tkinter.Label(font=(FONT_NAME,12,"bold"),bg=YELLOW,fg=GREEN) #removed text='✔' for validation
check_mark_label.grid(column=2,row=3)

window.mainloop()