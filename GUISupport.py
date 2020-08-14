import tkinter as tk
import random
from tkinter import simpledialog
from equal_dis import do_sorting
import pandas as pd
import numpy
from PIL import ImageTk, Image

HEIGHT = 1000
WIDTH = 1250
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
    # print(f"New:{list_of_current_members}")
    # print(keys_of_current_members)
    # civ_selection()
    form_team()


def load(root):
    global members, keys, checkVar
    checkVar = []
    for _ in range(len(members)):
        checkVar.append(tk.IntVar())
    canvas = tk.Canvas(root, bg="black", height=HEIGHT, width=WIDTH)
    canvas.pack()
    frame = tk.Frame(root, bg="cyan")
    frame.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.2)
    label = tk.Label(frame, text="List of Members:")
    label.grid(row=0, column=2)
    C = []
    for i in range(len(members)):
        tempC = tk.Checkbutton(frame, text=members[i], var=checkVar[i], onvalue=1, offvalue=0, height=1, width=25)
        C.append(tempC)
    i = 1
    for j in range(len(C)):
        if j % 5 == 0:
            i += 1
        C[j].grid(row=i, column=j % 5)
    sort_to_teams = tk.Button(frame, text="Create teams", command=callback)
    sort_to_teams.grid(row=i + 1, column=0)
    add_member = tk.Button(frame, text="Add new Players", command=newplayer)
    add_member.grid(row=i + 1, column=4)
    return canvas, frame, label, C, sort_to_teams, add_member, checkVar


def remove_frames(root):
    for widget in root.winfo_children():
        widget.destroy()
        # canvas.pack_forget():


def newplayer():
    global members, keys
    s = simpledialog.askstring("Name of the new player", "Please enter the name of the new player")
    s1 = simpledialog.askstring("Rating", "Please enter rating out of 10")
    members.append(s)
    keys.append(int(s1))
    # print(members)
    # print(keys)
    name = "Players.csv"
    list1 = []
    for i in range(len(members)):
        list1.append([members[i], keys[i]])
    player = pd.DataFrame(list1, columns=['member', 'keys'])
    player.to_csv(name)
    remove_frames(root)
    load(root)


def generate_teams1():
    global civ1, civ2, civ3, civ4, civ5, civ6, team1_civ
    team1_civ = []
    if civ1.get() == 1:
        flag = True
        while flag:
            civ = random.choice(arch_civ)
            if civ not in team1_civ:
                team1_civ.append(civ)
                flag = False
    if civ2.get() == 1:
        flag = True
        while flag:
            civ = random.choice(cav_civ)
            if civ not in team1_civ:
                team1_civ.append(civ)
                flag = False
    if civ3.get() == 1:
        flag = True
        while flag:
            civ = random.choice(seige_civ)
            if civ not in team1_civ:
                team1_civ.append(civ)
                flag = False
    if civ4.get() == 1:
        flag = True
        while flag:
            civ = random.choice(inf_civ)
            if civ not in team1_civ:
                team1_civ.append(civ)
                flag = False
    if civ5.get() == 1:
        flag = True
        while flag:
            civ = random.choice(navy_civ)
            if civ not in team1_civ:
                team1_civ.append(civ)
                flag = False
    if civ6.get() == 1:
        flag = True
        while flag:
            civ = random.choice(gun_civs)
            if civ not in team1_civ:
                team1_civ.append(civ)
                flag = False
    print(team1_civ)
    global civ11, civ21, civ31, civ41, civ51, civ61
    global team2_civ
    team2_civ = []
    if civ11.get() == 1:
        flag = True
        while flag:
            civ = random.choice(arch_civ)
            if civ not in team2_civ:
                team2_civ.append(civ)
                flag = False
    if civ21.get() == 1:
        flag = True
        while flag:
            civ = random.choice(cav_civ)
            if civ not in team2_civ:
                team2_civ.append(civ)
                flag = False
    if civ31.get() == 1:
        flag = True
        while flag:
            civ = random.choice(seige_civ)
            if civ not in team2_civ:
                team2_civ.append(civ)
                flag = False
    if civ41.get() == 1:
        flag = True
        while flag:
            civ = random.choice(inf_civ)
            if civ not in team2_civ:
                team2_civ.append(civ)
                flag = False
    if civ51.get() == 1:
        flag = True
        while flag:
            civ = random.choice(navy_civ)
            if civ not in team2_civ:
                team2_civ.append(civ)
                flag = False
    if civ61.get() == 1:
        flag = True
        while flag:
            civ = random.choice(gun_civs)
            if civ not in team2_civ:
                team2_civ.append(civ)
                flag = False
    print(team2_civ)
    show_team_civs()


def generate_teams2():
    global civ11, civ21, civ31, civ41, civ51, civ61
    global team2_civ
    team2_civ = []
    if civ11.get() == 1:
        flag = True
        while flag:
            civ = random.choice(arch_civ)
            if civ not in team2_civ:
                team2_civ.append(civ)
                flag = False
    if civ21.get() == 1:
        flag = True
        while flag:
            civ = random.choice(cav_civ)
            if civ not in team2_civ:
                team2_civ.append(civ)
                flag = False
    if civ31.get() == 1:
        flag = True
        while flag:
            civ = random.choice(seige_civ)
            if civ not in team2_civ:
                team2_civ.append(civ)
                flag = False
    if civ41.get() == 1:
        flag = True
        while flag:
            civ = random.choice(inf_civ)
            if civ not in team2_civ:
                team2_civ.append(civ)
                flag = False
    if civ51.get() == 1:
        flag = True
        while flag:
            civ = random.choice(navy_civ)
            if civ not in team2_civ:
                team2_civ.append(civ)
                flag = False
    if civ61.get() == 1:
        flag = True
        while flag:
            civ = random.choice(gun_civs)
            if civ not in team2_civ:
                team2_civ.append(civ)
                flag = False
    print(team2_civ)
    show_team_civs()


def show_team_civs():
    global team1_civ, team2_civ
    frame1 = tk.Frame(root)
    frame1.place(relx=0.3, rely=0.65, relwidth=0.4, relheight=0.25)
    label2 = tk.Listbox(frame1, height=5)
    label3 = tk.Listbox(frame1, height=5)
    for i in range(len(team1_civ)):
        label2.insert(i, team1_civ[i])
    for j in range(len(team2_civ)):
        label3.insert(j, team2_civ[j])
    label4 = tk.Label(frame1,text="Team1 Civs")
    label5 = tk.Label(frame1,text="Team2 Civs")
    label4.pack(side="left")
    label2.pack(side='left')
    label5.pack(side='right')
    label3.pack(side='right')


def civ_selection():
    global civ1, civ2, civ3, civ4, civ5, civ6, civ11, civ21, civ31, civ41, civ51, civ61
    global team1_civ, team2_civ
    display_frame = tk.Frame(root, bg="magenta")
    display_frame.place(x=525, y=0, relx=0.05, rely=0.35, relwidth=0.55, relheight=0.25)
    label1 = tk.Label(display_frame, text="Civs are displayed below.")
    label1.grid(row=0, column=1)
    civ1 = tk.IntVar()
    civ2 = tk.IntVar()
    civ3 = tk.IntVar()
    civ4 = tk.IntVar()
    civ5 = tk.IntVar()
    civ6 = tk.IntVar()
    arch = tk.Checkbutton(display_frame, text="Archer Civ", var=civ1, onvalue=1, offvalue=0, height=1,
                          width=25)
    arch.grid(row=1, column=0)
    cav = tk.Checkbutton(display_frame, text="Cavalry Civ", var=civ2, onvalue=1, offvalue=0, height=1, width=25)
    cav.grid(row=1, column=1)
    seige = tk.Checkbutton(display_frame, text="Seige Civ", var=civ3, onvalue=1, offvalue=0, height=1, width=25)
    seige.grid(row=1, column=2)
    inf = tk.Checkbutton(display_frame, text="Infantry Civ", var=civ4, onvalue=1, offvalue=0, height=1, width=25)
    inf.grid(row=2, column=0)
    navy = tk.Checkbutton(display_frame, text="Navy Civ", var=civ5, onvalue=1, offvalue=0, height=1, width=25)
    navy.grid(row=2, column=1)
    gun = tk.Checkbutton(display_frame, text="Gunpowder Civ", var=civ6, onvalue=1, offvalue=0, height=1, width=25)
    gun.grid(row=2, column=2)
    button1 = tk.Button(display_frame, text="Select Civs for Team1", command=generate_teams1)
    # button1.grid(row=3, column=1)
    label2 = tk.Label(display_frame, text="Civs are displayed below.")
    label2.grid(row=4, column=1)
    civ11 = tk.IntVar()
    civ21 = tk.IntVar()
    civ31 = tk.IntVar()
    civ41 = tk.IntVar()
    civ51 = tk.IntVar()
    civ61 = tk.IntVar()
    arch = tk.Checkbutton(display_frame, padx=0.5, text="Archer Civ", var=civ11, onvalue=1, offvalue=0, height=1,
                          width=25)
    arch.grid(row=5, column=0)
    cav = tk.Checkbutton(display_frame, text="Cavalry Civ", var=civ21, onvalue=1, offvalue=0, height=1, width=25)
    cav.grid(row=5, column=1)
    seige = tk.Checkbutton(display_frame, text="Seige Civ", var=civ31, onvalue=1, offvalue=0, height=1, width=25)
    seige.grid(row=5, column=2)
    inf = tk.Checkbutton(display_frame, text="Infantry Civ", var=civ41, onvalue=1, offvalue=0, height=1, width=25)
    inf.grid(row=6, column=0)
    navy = tk.Checkbutton(display_frame, text="Navy Civ", var=civ51, onvalue=1, offvalue=0, height=1, width=25)
    navy.grid(row=6, column=1)
    gun = tk.Checkbutton(display_frame, text="Gunpowder Civ", var=civ61, onvalue=1, offvalue=0, height=1, width=25)
    gun.grid(row=6, column=2)
    button2 = tk.Button(display_frame, text="Select Civ combo for Teams", command=generate_teams1)
    button2.grid(row=7, column=1)


def form_team():
    display_frame = tk.Frame(root, bg="blue")
    display_frame.place(relx=0.05, rely=0.35, relwidth=0.4, relheight=0.25)
    label1 = tk.Label(display_frame, text="Teams are displayed below.")
    label1.pack(side='top')
    leftframe = tk.Frame(display_frame)
    leftframe.pack(side="left")
    rightframe = tk.Frame(display_frame)
    rightframe.pack(side="right")
    team1_box = tk.Listbox(leftframe, height=5)
    team2_box = tk.Listbox(rightframe, height=5)
    if len(list_of_current_members) <= 8:
        # print(list_of_current_members)
        team1, team2 = do_sorting(list_of_current_members, keys_of_current_members)
        for i in range(len(team1)):
            team1_box.insert(i, team1[i])
        for j in range(len(team2)):
            team2_box.insert(j, team2[j])
    team1_box.pack()
    team2_box.pack()
    civ_selection()


def remove_nan(array):
    array = [x for x in array if str(x) != 'nan']
    return array


def app_page():
    global members, keys, root, checkVar
    global arch_civ, cav_civ, seige_civ, inf_civ, gun_civs, navy_civ
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
    arch_civ = remove_nan(arch_civ)
    cav_civ = remove_nan(cav_civ)
    seige_civ = remove_nan(seige_civ)
    inf_civ = remove_nan(inf_civ)
    navy_civ = remove_nan(navy_civ)
    gun_civs = remove_nan(gun_civs)
    print(arch_civ, cav_civ, seige_civ, inf_civ, navy_civ, gun_civs)

    root = tk.Tk()

    canvas, frame, label, C, button, button1, checkVar = load(root)
    # form_team()
    root.mainloop()


app_page()
