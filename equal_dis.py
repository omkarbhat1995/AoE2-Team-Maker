def buildup():
    from constant import keys, members
    curr_keys = []
    curr_members = []
    for i in range(len(members)):
        print("Say Y or N")
        a = input(members[i])
        if a == 'y' or a == 'Y':
            curr_members.append(members[i])
            curr_keys.append(keys[i])

    print(curr_members)
    print(curr_keys)
    if len(curr_keys) <= 8:
        team1, team2 = do_sorting(curr_members, curr_keys)
    else:
        print("Too many players! Not gonna sort!")


def do_sorting(mem, keys):
    print("Sorting")
    n = len(mem) - 1
    for i in range(n, 0, -1):
        for j in range(n, n - i, -1):
            if keys[j] > keys[j - 1]:
                keys[j], keys[j - 1] = keys[j - 1], keys[j]
                mem[j], mem[j - 1] = mem[j - 1], mem[j]
    print(f'Players:{mem}')
    print(f'Values:{keys}')
    team1=[]
    team2=[]
    if len(mem) == 6:
        team1, team2 = form_teams(mem, keys, 3, 3)
    elif len(mem) == 7:
        team1, team2 = form_teams(mem, keys, 4, 3)
    elif len(mem) == 8:
        team1, team2 = form_teams(mem, keys, 4, 4)
    return team1, team2


def form_teams(mem, keys, a, b):
    Team_1 = []
    Team_2 = []
    team1keys = 0
    team2keys = 0
    # print(f"team1={team1keys}:team2={team2keys}:a={a}:b={b}")
    Team_1.append(mem[0])
    Team_2.append(mem[1])
    team1keys += keys[0]
    team2keys += keys[1]
    a = a - 1
    b = b - 1
    i = 2
    while i <= len(mem) - 1:  # a != 0 and b != 0:
        if team2keys >= team1keys and a > 0:
            Team_1.append(mem[i])
            team1keys += keys[i]
            i += 1
        elif team1keys >= team2keys and b > 0:
            Team_2.append(mem[i])
            team2keys += keys[i]
            i += 1
        # print(f"team1={team1keys}:team2={team2keys}:a={a}:b={b}")
    # print(f"team1={team1keys}:team2={team2keys}:a={a}:b={b}")
    print(f'Team1:{Team_1}')
    print(f'Team2:{Team_2}')
    return Team_1, Team_2


#buildup()
