magician_names = ['jik', 'jok', 'jak', 'juk']
def show_magicians(magician_names):
    """ print out names """
    for name in magician_names:
        print(name.title())

def make_great(magician_names):
    for name in magician_names:
        print("the Great " + name.title() + ".")

show_magicians(magician_names)
print("--- | ---")
make_great(magician_names)
