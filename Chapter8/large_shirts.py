def make_shirt(text, size='large'):
    print("The size of your shirt is " + size.title()+ ".")
    print("The print you wanted is " + "'" + text + "'.\n")

make_shirt('I love it!')
make_shirt(text='I love Python')

def make_shirt(text, size='medium'):
    print("The size of your shirt is " + size.title()+ ".")
    print("The print you wanted is " + "'" + text + "'.\n")

make_shirt('I love it!')
make_shirt(text='I love Python')

def make_shirt(text, size):
    print("The size of your shirt is " + size.title()+ ".")
    print("The print you wanted is " + "'" + text + "'.\n")

make_shirt('I love it!', 'small')
make_shirt(text='I love Python', size='extra large')