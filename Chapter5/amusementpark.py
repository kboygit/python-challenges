age = 69
# if age < 4:
#     print("Your admission is free")
# elif age < 18:
#     print("The admission is $5")
# else:
#     print("Admission for anyone age 18 or older is $10")
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 3
elif age >= 65:
    price = 10
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")
