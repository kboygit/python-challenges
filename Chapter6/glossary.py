learned = {
    'del': 'delete',
    'insert': 'insert an element',
    'dictionary': 'a set of key:value pairs',
    'list': 'an array',
    'operators': 'a set of mathematical operators',
}

for learn in learned:
    print("The meaning of ", learn, 'is', learned[learn])

for learn, value in learned.items():
    print(learn, ':',  value )

for learn in learned:
    print("The meaning of " + learn + " is " + str(learned[learn]))