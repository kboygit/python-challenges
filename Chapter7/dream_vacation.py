dream_vacation = {}

poll = True

while poll:
    dream_vacay = input("If you could visit one place in the world,where would you go?: ")
    name = input("What is your name?: ")

    dream_vacation[name] = dream_vacay

    again = input("\nIs there another place you wanted to go? (yes/no): ")
    if again == 'no':
        poll = False
    elif again != str('yes') or again != str('no'):
        print("\nPlease type 'yes' or 'no': ")
        poll = False

print("\n---- POLL RESULT ----")
for name, dream_vacay in dream_vacation.items():
    print("\n" + name.title() + " likes to go to " + dream_vacay.title())

