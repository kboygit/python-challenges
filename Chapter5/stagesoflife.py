persons = [ 10 , 20 , 30 , 40 , 50 , 60 , 70 , 80]
people = [ 10 , 20 , 30 , 40 , 50 , 60 , 70 , 80]

for person in persons:
    if person < 2:
        print("You are a baby")
    elif person >= 2 and person <= 4:
        print("You are a toddler")
    elif person >= 4 and person <= 13:
        print("You are a kid")
    elif person >= 13 and person <= 20:
        print("You are a teenager")
    elif person >= 20 and person <= 65:
        print("You are an adult")
    else:
        print("You are an elder")

# for p in people:
#     if p < 2:
#         print("You are a baby")
#     elif p 2 <= person < 4:
#         print("You are a toddler")
#     elif person 4 <= person < 13:
#         print("You are a kid")
#     elif person <= 13 person < 20:
#         print("You are a teenager")
#     elif person 20 <= person < 65:
#         print("You are an adult")
#     else:
#         print("You are an elder")
