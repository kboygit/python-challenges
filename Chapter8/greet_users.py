def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

def call_brands(brands):
    """Print a simple call to brands"""
    for brand in brands:
        call = "Wassup, " + brand.title() + "!"
        print(call)

userbrands = ['nike', 'adidads', 'puma']
call_brands(userbrands)