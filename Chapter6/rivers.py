rivers = {
    'nile': 'egypt',
    'mississippi': 'mississippi',
    'amazon': 'amazon',
}

for river in rivers:
    print("The " + river + " runs through " + str(rivers[river].title()))

print("\nRivers:",rivers.keys())
print("Country:",rivers.values())


print("\nRivers and its Countries:")
for keys in sorted(rivers.keys()):
    print("River:",keys.title())
for values in sorted(rivers.values()):
    print("Country:",values.title())