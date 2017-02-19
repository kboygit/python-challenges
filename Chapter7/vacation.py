prompt = "If you could visit one place in the world, where would you go?"
prompt += "\nWhat is your name: "

while True:
    message = input(prompt)

    if message == 'stop':
        break
    else:
        print(message.title())