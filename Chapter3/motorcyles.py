motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ninja'
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

cars = ['toyota' , 'bmw', 'mercedes-benz']
shoes = []

print(cars)
shoes = []
shoes.insert(0,'nike')
print(shoes)

del cars[0]
print(cars)

popped_motorcycles = motorcycles.pop()
print(popped_motorcycles)
print(motorcycles)

