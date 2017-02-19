sandwich_orders = ['peanut butter', 'turkey ham', 'tuna' , 'chicken']
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()

    print("\nVerifying order: " + order.title())
    finished_sandwiches.append(order)

print("\n---- ALL ORDERS ARE ----")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

