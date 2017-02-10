available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_toppings in requested_toppings:
    if requested_toppings in available_toppings:
        print("Adding " + "requested_topping" + ".")
    else:
        print("Sorry, we don't have " + requested_toppings + ".")

print("\nFinished making your pizza!")  
