my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

for foods in my_foods[:]:
    my_foods.append('cannoli')
    print("My favorite foods are: ")
    print(my_foods)

for foods in friend_foods[:]:
    friend_foods.append('ice cream')
    print("\nMy friends favorite foods are: ")
    print(friend_foods)
