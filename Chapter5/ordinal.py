ordinals = [1,2,3,4,5,6,7,8,9]

for ordinal in ordinals:
    if(ordinal == 1):
        print(str(ordinal) + "st")
    elif(ordinal == 2):
        print(str(ordinal) + "nd")
    elif(ordinal == 3):
        print(str(ordinal) + "rd")
    else:
        print(str(ordinal) + "th")
