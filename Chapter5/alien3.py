alien_color = ['green', 'yellow', 'red']
# Snippet Bellow wont work #
# if alien_color is 'green':
#     print("you earned 5 points")
# elif alien_color is 'yellow':
#     print("you earned 10 points")
# elif alien_color is 'red':
#     print("you earned 15 points.")

if 'green' in alien_color:
    print("you earned 5 points")
elif 'yellow' in alien_color:
    print("you earned 10 points")
elif 'red' in alien_color:
    print("you earned 15 points")

if 'green' in alien_color:
    print("you earned 5 points")
if 'yellow' in alien_color:
    print("you earned 10 points")
if 'red' in alien_color:
    print("you earned 15 points")


if alien_color == 'green' in alien_color:
    print("points = 5")
elif alien_color == 'yellow' in alien_color:
    print("points = 10")
elif alien_color == 'red' in alien_color:
    print("points = 15")
