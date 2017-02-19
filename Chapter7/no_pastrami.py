sandwich_orders = ['peanut butter', 'pastrami', 'turkey ham', 'pastrami', 'tuna', 'chicken', 'pastrami']
finished_sandwiches = []

print("Sorry we ran out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    order = sandwich_orders.pop()

    print("\nVerifying order: " + order.title())
    finished_sandwiches.append(order)

print("\n---- ALL ORDERS ARE ----")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

