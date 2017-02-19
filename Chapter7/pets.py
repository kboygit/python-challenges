pets  = ['dog' , 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
    while 'dog' in pets:
        pets.remove('dog')


print(pets)