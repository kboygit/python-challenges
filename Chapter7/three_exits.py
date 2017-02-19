prompt = "Enter a series of pizza toppings;Cheese,Pepperoni,Bell Pepper,Tomato:"
prompt += "\n(Type 'stop' to stop)"


# Using Condition Statement
topping = ""
while topping != 'stop':
    topping = input(prompt)

    if topping != 'stop':
        print("\n" + topping.title() + " has been added to the pizza.\n")
    else:
        print("\nAll toppings has been added to the pizza!")

# Using Active Variable
active = True
while active:
    topping = input(prompt)

    if topping != 'stop':
        print("\n" + topping.title() + " has been added to the pizza.\n")
    elif topping == 'stop':
        active = False
    else:
        print("\nAll toppings has been added to the pizza!\n")

# Using a break statement
while True:
    topping = input(prompt)

    if topping != 'stop':
        print("\n" + topping.title() + " has been added to the pizza.\n")
    elif topping == 'stop':
        break
    else:
        print("\nAll toppings has been added to the pizza!")

