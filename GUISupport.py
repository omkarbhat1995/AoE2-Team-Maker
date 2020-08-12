import tkinter as tk
from constant import members, keys

HEIGHT = 700
WIDTH = 800

root = tk.Tk()
checkVar = []
NumberofMembers = len(members)
for _ in range(len(members)):
    checkVar.append(tk.IntVar())

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
frame = tk.Frame(root, bg="cyan")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
label = tk.Label(frame, text="List of Members:")
label.grid(row=0, column=2)
C = []
for i in range(len(members)):
    tempC = tk.Checkbutton(frame, text=members[i], variable=checkVar[i], onvalue=1, offvalue=0, height=1, width=25)
    C.append(tempC)
i = 1
for j in range(len(C)):
    if j % 6 == 0:
        i += 1
    C[j].grid(row=i, column=j % 6)
button = tk.Button(frame, text="Test Button")

button.grid(row=25,column=10)

root.mainloop()
