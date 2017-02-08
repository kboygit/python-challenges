invite_people = ['lola tinang' , 'yabin' , 'papa ondo' , 'lolo pedong']
invite = "You are invited "
unable = "I am so sorry you can't make it "
unable_sorry = "I am so sorry, I can't invite you to dinner "
congrats = "You are stil invited "

print(unable + invite_people[0].title())
print(unable + invite_people[2].title())

invite_people[0] = 'mama'
invite_people[2] = 'papa'

print( invite + invite_people[0].title())
print( invite + invite_people[2].title() )
print("I found a bigger table ")

invite_people.insert(0, 'hanna')
invite_people.insert(3, 'kboy')
invite_people.append('kwak')
print(invite_people)

print( invite + invite_people[0].title())
print( invite + invite_people[1].title())
print( invite + invite_people[2].title())
print( invite + invite_people[3].title())
print( invite + invite_people[4].title())
print( invite + invite_people[5].title())
print( invite + invite_people[6].title())

print("I am so sorry , I can only invite two people for dinner.")
a = invite_people.pop()
b = invite_people.pop(0)
c = invite_people.pop(1)
d = invite_people.pop(1)
f = invite_people.pop(2)
print(unable_sorry + a)
print(unable_sorry + b)
print(unable_sorry + c)
print(unable_sorry + d)
print(unable_sorry + f)
print(invite_people)
print(congrats + invite_people[0].title())
print(congrats + invite_people[1].title())
del invite_people[0]
del invite_people[0]
print(invite_people)
