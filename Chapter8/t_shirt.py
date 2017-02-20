def make_shirt(size, text):
    print("The size of your shirt is " + size.title()+ ".")
    print("The print you wanted is " + "'" + text + "'.\n")

make_shirt('medium', 'I love it!')
make_shirt(size='large', text='I love it')