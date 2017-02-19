prompt = "Enter a series of pizza toppings;Cheese,Pepperoni,Bell Pepper,Tomato:"
prompt += "\n(Type 'stop' to stop)"

topping = ""
while topping != 'stop':
    topping = input(prompt)

    if topping != 'stop':
        print("\n" + topping.title() + " has been added to the pizza.\n")
    else:
        print("\nAll toppings has been added to the pizza!")