import tkinter as tk

clickCount = 0

def leftClick(event):
    global clickCount
    clickCount += 1
    label.config(text="SOL (" + str(clickCount) + ")", fg="black")

def rightClick(event):
    global clickCount
    clickCount += 1
    label.config(text="SAĞ (" + str(clickCount) + ")", fg="black")

window = tk.Tk()
window.title("Mouse Click Test")

frame = tk.Frame(window, width=1920, height=1080, bg="white")
frame.pack()

label = tk.Label(frame, text="", font=("Arial", 24), bg="white", fg="white")
label.place(relx=0.5, rely=0.5, anchor="center")

frame.bind("<Button-1>", leftClick)
frame.bind("<Button-3>", rightClick)

window.mainloop()
