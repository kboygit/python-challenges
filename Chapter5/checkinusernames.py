current_users = ["admin" , "kboy", "qbz", "lol", "lolz"]
new_users = ["kboy" , "shoo", "lafang" , "admin", "pok"]

for new_users in new_users:
    if new_users in current_users:
        print(new_users.title() + " you need to enter a new username.")
    if new_users.upper() in current_users:
        print(new.users.upper() + " can't be used.")
    else:
        print("username available")
