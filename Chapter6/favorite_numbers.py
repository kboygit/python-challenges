favorite_numbers = {
    'janeene': 1,
    'aneene': 2,
    'aning': 3,
    'ning': 4,
    'ing': 5,
}

# print("Janeene's favorite number is:" +
#       str(favorite_numbers['janeene']).title())
# print("Aneene's favorite number is:" +
#       str(favorite_numbers['aneene']).title())
# print("Aning's favorite number is:" +
#       str(favorite_numbers['aning']).title())
# print("Ning's favorite number is:" +
#       str(favorite_numbers['ning']).title())
# print("Ing's favorite number is:" +
#       str(favorite_numbers['ing']).title())

for name, num in favorite_numbers.items():
    print("Name:" + name.title())
    print("\tFavorite Number:" + str(num).title())