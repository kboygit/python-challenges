car = 'honda'
shoes = ['nike', 'sperry', 'airmax']
shades = 'rayban'

print("Is car == 'honda'? I predict True.")
print(car == 'honda')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

shoe = 'nike'
shoe1 = 'adidas'
print("\nIs your shoes nike?")
print(shoe.lower() == 'nike')
print(shoe == 'nike' or shoe1 == 'nike')
print(shoe == 'nike' and shoe1 == 'nike')
print('nike' in shoes)
if shoe1 not in shoes:
    print("I do not want to collect " + shoe1.title())


my_num_pairs = 20
her_num_pairs = 21

print(my_num_pairs >= 21)
print(her_num_pairs >= 21)
