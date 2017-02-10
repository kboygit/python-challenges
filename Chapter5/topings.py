requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_toppings in requested_toppings:
    if requested_toppings == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_toppings + ".")


print("\nFinished making your pizza!")


requested_orders = []
if requested_orders:
    for requested_orders in requested_orders:
        print("Adding " + requested_orders + ".")
    print("\nFinished making your piza!")
else:
    print("\nAre you sure you want a plain pizza")
