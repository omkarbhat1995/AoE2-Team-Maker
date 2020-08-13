import tkinter as tk
from tkinter import simpledialog
from equal_dis import do_sorting
import pandas as pd
from PIL import ImageTk, Image

HEIGHT = 600
WIDTH = 800
checkVar = []
list_of_current_members = []
keys_of_current_members = []
button_pressed = False


def callback():
    global checkVar, members, keys
    global list_of_current_members
    global keys_of_current_members
    list_of_current_members = []
    keys_of_current_members = []
    for i in range(len(checkVar)):
        if checkVar[i].get() == 1:
            if members[i] not in list_of_current_members:
                list_of_current_members.append(members[i])
                keys_of_current_members.append(int(keys[i]))
    button_pressed = True
    print(f"New:{list_of_current_members}")
    print(keys_of_current_members)
    form_team()


def load(root):
    global members, keys, checkVar
    checkVar = []
    for _ in range(len(members)):
        checkVar.append(tk.IntVar())
    canvas = tk.Canvas(root, bg="black", height=HEIGHT, width=WIDTH)
    # background_image = tk.PhotoImage(file='aoe2.png')
    # background_label = tk.Label(root, image=background_image)
    # background_label.place(relwidth=1, relheight=1)
    # image = ImageTk.PhotoImage(Image.open('aoe2.png'))
    # canvas.create_image(0, 0, anchor='nw', image=image)
    canvas.pack()

    frame = tk.Frame(root, bg="cyan")
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.3)
    label = tk.Label(frame, text="List of Members:")
    label.grid(row=0, column=1)
    C = []
    for i in range(len(members)):
        tempC = tk.Checkbutton(frame, text=members[i], var=checkVar[i], onvalue=1, offvalue=0, height=1, width=25)
        C.append(tempC)
    i = 1
    for j in range(len(C)):
        if j % 3 == 0:
            i += 1
        C[j].grid(row=i, column=j % 3)
    sort_to_teams = tk.Button(frame, text="Create teams", command=callback)
    sort_to_teams.grid(row=i + 1, column=0)
    add_member = tk.Button(frame, text="Add new Players", command=newplayer)
    add_member.grid(row=i + 1, column=2)
    return canvas, frame, label, C, sort_to_teams, add_member, checkVar


def newplayer():
    global members, keys
    s = simpledialog.askstring("Name of the new player", "Please enter the name of the new player")
    s1 = simpledialog.askstring("Rating", "Please enter rating out of 10")
    members.append(s)
    keys.append(int(s1))
    print(members)
    print(keys)
    name = "Players.csv"
    list1 = []
    for i in range(len(members)):
        list1.append([members[i], keys[i]])
    player = pd.DataFrame(list1, columns=['member', 'keys'])
    player.to_csv(name)
    load(root)


def form_team():
    display_frame = tk.Frame(root, bg="blue")
    display_frame.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.3)
    label1 = tk.Label(display_frame, text="Teams are displayed below.")
    label1.pack(side='top')
    leftframe = tk.Frame(display_frame)
    leftframe.pack(side="left")
    rightframe = tk.Frame(display_frame)
    rightframe.pack(side="right")
    team1_box = tk.Listbox(leftframe)
    team2_box = tk.Listbox(rightframe)
    if len(list_of_current_members) <= 8:
        print(list_of_current_members)
        team1, team2 = do_sorting(list_of_current_members, keys_of_current_members)
        for i in range(len(team1)):
            team1_box.insert(i, team1[i])
        for j in range(len(team2)):
            team2_box.insert(j, team2[j])
    team1_box.pack()
    team2_box.pack()


def app_page():
    global members, keys, root, checkVar

    df = pd.read_csv("Players.csv", usecols=["member", "keys"])
    members = df["member"].values.tolist()
    keys = df["keys"].values.tolist()
    df = pd.read_csv("Civs.csv", usecols=["arch_civ", "cav_civ", "seige_civ", "inf_civ", "navy_civ", "gun_civ"])
    arch_civ = df["arch_civ"].values.tolist()
    cav_civ = df["cav_civ"].values.tolist()
    seige_civ = df["seige_civ"].values.tolist()
    inf_civ = df["inf_civ"].values.tolist()
    navy_civ = df["navy_civ"].values.tolist()
    gun_civs = df["gun_civ"].values.tolist()
    print(arch_civ, cav_civ, seige_civ, inf_civ, navy_civ, gun_civs)

    root = tk.Tk()

    canvas, frame, label, C, button, button1, checkVar = load(root)
    root.mainloop()


app_page()
