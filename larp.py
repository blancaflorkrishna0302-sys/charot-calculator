import tkinter as tk
import random

root = tk.Tk()
root.title("Calculator")
root.attributes("-fullscreen", True)

BG = "#0f0f0f"
PINK = "#ff4d8d"
WHITE = "#ffffff"

root.configure(bg=BG)
canvas = tk.Canvas(root, bg=BG, highlightthickness=0)
canvas.pack(fill="both", expand=True)

hearts = []

def create_heart():
    x = random.randint(100, root.winfo_width() - 100)
    y = root.winfo_height() - 100

    heart = canvas.create_text(
        x,
        y,
        text="❤",
        fill=PINK,
        font=("Arial", random.randint(20, 40))
    )

    hearts.append(heart)

def animate_hearts():
    for heart in hearts[:]:
        canvas.move(heart, random.randint(-2, 2), -3)

        x, y = canvas.coords(heart)

        if y < -50:
            canvas.delete(heart)
            hearts.remove(heart)

    root.after(30, animate_hearts)

def calculate(event=None):
    expression = entry.get()

    for _ in range(8):
        create_heart()

    output.config(state="normal")

    if expression == "":
        output.insert("end", "\nI miss you ❤️\n")
        output.see("end")
        root.after(2500, root.destroy)

    elif expression == "1+1":
        output.insert("end", "\n11, now try to calculate 6+7\n")

    elif expression == "6+7":
        output.insert("end", "\nSIX SEVENNNN, KIDDING ASIDE. PRESS ENTER\n")

    elif expression == "143":
        output.insert("end", "\nI love you ❤️\n")

    elif expression == "1122":
        output.insert("end", "\nYou're doing great!\n")

    else:
        output.insert("end", "\nMALII BASAHIN MO KASE YUNG INSTRUCTIONS.\n")

    output.see("end")
    output.config(state="disabled")

    entry.delete(0, tk.END)


frame = tk.Frame(canvas, bg=BG)
frame.place(relx=0.5, rely=0.5, anchor="center")

title = tk.Label(
    frame,
    text="♡ Charot Calculator ♡",
    fg=PINK,
    bg=BG,
    font=("Segoe UI", 28, "bold")
)
title.pack(pady=20)

subtitle = tk.Label(
    frame,
    text="Try to calculate 1+1...",
    fg="#bbbbbb",
    bg=BG,
    font=("Segoe UI", 12)
)
subtitle.pack(pady=(0,20))

entry = tk.Entry(
    frame,
    font=("Consolas", 18),
    bg="#1a1a1a",
    fg=WHITE,
    insertbackground=WHITE,
    justify="center",
    width=25,
    relief="flat"
)
entry.pack(ipady=12)

entry.bind("<Return>", calculate)

button = tk.Button(
    frame,
    text="Calculate ✨",
    command=calculate,
    bg=PINK,
    fg="white",
    font=("Segoe UI", 12, "bold"),
    relief="flat",
    padx=20,
    pady=10
)
button.pack(pady=20)

output = tk.Text(
    frame,
    width=50,
    height=10,
    bg="#1a1a1a",
    fg=WHITE,
    font=("Consolas", 12),
    relief="flat"
)
output.pack()

output.insert(
    "end",
    "Charot Calculator ♡\n\n"
)
root.bind("<Escape>", lambda e: root.destroy())

animate_hearts()
root.mainloop()