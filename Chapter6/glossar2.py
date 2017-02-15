learned = {
    'del': 'delete',
    'insert': 'insert an element',
    'dictionary': 'a set of key:value pairs',
    'list': 'an array',
    'operators': 'a set of mathematical operators',
}

for key,value in learned.items():
    print(key, ':' , value)

learned['set'] = 'a unique set of key:value pairs'
learned['.values'] = 'iterates through values'
learned['.keys'] = 'iterates through keys'

print("\nNew set:")
for key,value in sorted(learned.items()):
    print(key, ':' , value)