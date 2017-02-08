invite_people = ['lola tinang' , 'yabin' , 'papa ondo' , 'lolo pedong']
invite = "You are invited "
unable = "I am so sorry you can't make it "

print(unable + invite_people[0].title())

print(unable + invite_people[2].title())



invite_people[0] = 'mama'
invite_people[2] = 'papa'

print( invite + invite_people[0].title())
print( invite + invite_people[2].title() )

print("There are " + str(len(invite_people)) + ".That will be going on dinner tonight")
