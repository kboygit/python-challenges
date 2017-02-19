prompt = "How young are you?"

current_age = 3
while current_age < 12:
    ticket = input(prompt)
    print(ticket)

    if current_age <= 3:
        print("The ticket is free\n")
        break
    elif current_age >= 3 and current_age <= 12:
        print("The ticket is $10\n")
        break
    else:
        print("The ticket is $15\n")
        break



