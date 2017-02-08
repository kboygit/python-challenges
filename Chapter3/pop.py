motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

last_moto  = motorcycles.pop()
print(motorcycles)
print(last_moto)
print("The last motorcycle I rode is a " + last_moto)

first_moto = motorcycles.pop(0)
print(first_moto)
print('The first motorcycled I owed was a ' + first_moto.title() + '.')
print(motorcycles)



