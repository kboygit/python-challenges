invite_people = ['lola tinang' , 'yabin' , 'papa ondo' , 'lolo pedong']
invite = "You are invited "
unable = "I am so sorry you can't make it "

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
