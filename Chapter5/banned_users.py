banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
user1 = 'andrew'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
    if user1 in banned_users:
        print("YOU ARE BANNED!")
