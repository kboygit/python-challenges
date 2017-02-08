dimensions = (200, 50)
sizes = ( 8,9,10 )
# dimensions[0] = 250
# Error
print("Original Dimensions:")
for dimension in dimensions:
    print(dimension)

# Writing Over A Tuple
dimensions = (400,100)
print("\nModified Dimensions:")
for dimension in dimensions:
    print(dimension)

print("\nTheses are the sizes: ")
for size in sizes:
    print(size)
# The same as:
# print(dimensions[0])
# print(dimensions[1])
# print(dimensions)
