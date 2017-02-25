def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""
    print(toppings)

def make_another_pizza(size, *toppings):
    """Summarize the pizza we are about to make"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'mozzarella')

make_another_pizza(16, 'hawaiian')
make_another_pizza(18, 'bell peppers', 'mushrooms', 'tomato')