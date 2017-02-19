message = input("Tell me something, and I will repeat it back to you: ")
print(message)

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

favorite_food = "\nWhat is your favorite food?"
favorite_food += "\nEnter 'x' to exit the program: "

food_input = " "
while food_input != 'x':
    food_input = input(favorite_food)

    if food_input != 'x':
        print(food_input)