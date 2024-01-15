import tkinter as t
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Ubuntu"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    #stop timer
    window.after_cancel(timer)
    #timer text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    #title label back to timer
    status_lbl.config(text="Timer", fg=GREEN)
    #check marks removed
    check_lbl0.config(text="")
    #reps reset
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 0 and reps < 7:
        #work
        status_lbl.config(text="WORK", fg=PINK)
        count_down(work_sec)
    elif reps % 2 != 0 and reps < 7:
        #short break
        status_lbl.config(text="Short Break", fg=GREEN)
        count_down(short_break_sec)
    elif reps == 7:
        #long break
        status_lbl.config(text="Long Break", fg=RED)
        count_down(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global reps
    min = int(count/60)
    if min == 0:
        min = "00"
    elif min < 10:
        min = f"0{min}"
    sec = int(count%60)
    if sec == 0:
        sec = "00"
    elif sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        reps += 1
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += CHECK_MARK
        check_lbl0.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = t.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = t.Canvas(width=200, height=226, bg=YELLOW, highlightthickness=0)
tomato = t.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(103, 112, text="00:00", fill="white", font=(FONT_NAME, 32))
canvas.grid(row=1, column=1)



start_btn = t.Button(text="START", bg=PINK, fg=YELLOW, command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = t.Button(text="RESET", bg=PINK, fg=YELLOW, command=reset_timer)
reset_btn.grid(row=2, column=2)

status_lbl = t.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 32))
status_lbl.grid(row=0, column=1)

check_lbl0 = t.Label(font=(FONT_NAME, 16), bg=YELLOW, fg=GREEN)
check_lbl0.grid(row=2, column=1)

window.mainloop()
