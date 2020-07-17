from constant import keys,members
curr_keys=[]
curr_members=[]
for i in range(len(members)):
     print("Say Y or N")
     #print(f"{members[i]}")
     a=input(members[i])
     if a=='y' or a=='Y':
          curr_members.append(members[i])
          curr_keys.append(keys[i])

print(curr_members)
print(curr_keys)
summation=0
for i in curr_keys:
     summation+=i
#n=2
#n=input("number of teams")
print(f"Creating 2 teams")
Team_1=[]
Team1_key=0
Team_2=[]
Team2_key=0
Team_1.append(curr_members[0])
Team1_key = +curr_keys[0]
if len(curr_keys)<=8:
     for i in range(len(curr_keys)):
          #print(f"Iterator:{i}")
          if i==0:
               print("asd")
          else:
               if Team2_key<=summation/2 and Team1_key<=summation/2:
                    if Team1_key>Team2_key:
                         Team_2.append(curr_members[i])
                         Team2_key+=curr_keys[i]
                         #print(f"Team{1}:{Team_1}:{Team1_key}")
                         #print(f"Team{2}:{Team_2}:{Team2_key}")
                    elif Team2_key>Team1_key:
                         Team_1.append(curr_members[i])
                         Team1_key += curr_keys[i]
                         #print(f"Team{1}:{Team_1}:{Team1_key}")
                         #print(f"Team{2}:{Team_2}:{Team2_key}")
                    elif Team1_key==Team2_key:
                         Team_1.append(curr_members[i])
                         Team1_key+=curr_keys[i]
                         #print(f"Team{1}:{Team_1}:{Team1_key}")
                         #print(f"Team{2}:{Team_2}:{Team2_key}")
               elif Team2_key>=summation/2 and Team1_key>=summation/2:
                    print("Asd")
                    #print(f"Team{1}:{Team_1}:{Team1_key}")
                    #print(f"Team{2}:{Team_2}:{Team2_key}")
else:
     print("too many players! Discard a few!")
print(Team_1)
print(Team_2)
