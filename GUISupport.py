import tkinter as tk
from constant import members, keys
from PIL import ImageTk
from PIL.Image import Image

HEIGHT = 700
WIDTH = 800


def select_check(i):
    if i.get() == 1:
        print("Pressed! ")
    pass


def callback(checkbox):
    for i in checkbox:
        print(i.get())


def load(root):
    checkVar = []
    for _ in range(len(members)):
        checkVar.append(tk.IntVar())
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()
    frame = tk.Frame(root, bg="cyan")
    frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
    label = tk.Label(frame, text="List of Members:")
    label.grid(row=0, column=1)
    C = []
    j = 1
    for i in range(len(members)):
        C.append(tk.Checkbutton(frame, text=members[i], var=checkVar[i], onvalue=1,
                                offvalue=0, height=1, width=25))
        if i % 3 == 0:
            j += 1
            C[i].grid(row=j, column=i % 3)
    """for j in range(len(C)):
        if j % 3 == 0:
            i += 1
        C[j].grid(row=i, column=j % 3)"""
    button = tk.Button(frame, text="Test Button", command=callback(checkVar))
    button.grid(row=25, column=1)
    return canvas, frame, label, C, button, checkVar


def app_page():
    root = tk.Tk()
    Number_of_Members = len(members)
    checkVar = []
    # canvas, frame, label, C, button, checkVar = load(root)
    for _ in range(len(members)):
        checkVar.append(tk.IntVar())
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()
    frame = tk.Frame(root, bg="cyan")
    frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
    label = tk.Label(frame, text="List of Members:")
    label.grid(row=0, column=1)
    C = []
    for i in range(len(members)):
        tempC = tk.Checkbutton(frame, text=members[i], var=checkVar[i],  onvalue=1,
                               offvalue=0, height=1, width=25)
        C.append(tempC)
    i = 1
    for j in range(len(C)):
        if j % 3 == 0:
            i += 1
        C[j].grid(row=i, column=j % 3)
    button = tk.Button(frame, text="Test Button", command=callback(checkVar))
    button.grid(row=25, column=1)

    root.mainloop()


app_page()
