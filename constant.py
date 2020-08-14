import pandas as pd

# members = ['Ajax', 'King_Arthur', 'Mhota', 'GVK', 'Black_Death', 'Noramay', 'Prof', 'Krakken', 'Shans', 'Lihkin',
# 'Starks', 'Peacekeeper']
# keys = [9.5, 6.5, 5, 6, 7, 8, 5, 9, 4, 3.5, 5.5, 3]
arch_civ = ['Britons', 'Chinese', "Mongols", "Mayans", "Italians"]
cav_civ = ["Franks", "Persians", "Sarracens", "Huns", "Indians", "Magyars"]
seige_civ = ["Celts", "Mongols", "Slavs"]
inf_civ = ["Celts", "Goths", "Japanese", "Teutons", "Vikings", "Aztecs", "Incas", "Slavs"]
navy_civ = ["Japanese", "Saracens", "Byzantines", "Vikings", "Korean", "Italians"]
gun_civs = ["Turks", "Spanish", "Indians"]

# Byzantines- Defense

def asdad():
    name = "Players.csv"
    list1 = []
    for i in range(len(members)):
        list1.append([members[i], keys[i]])
    player = pd.DataFrame(list1, columns=['member', 'keys'])
    player.to_csv(name)


# asdad()
# name = "Players.csv"
# player = pd.DataFrame([members, keys], columns=['members', 'keys'])
# player.to_csv(name)

df = pd.read_csv("Players.csv", usecols=["member", "keys"])
mem = df["member"].values.tolist()
print(mem)
