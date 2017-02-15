alien_O = {'x_position': 0,'y_position': 25,'speed': 'medium'}

print("Original x_position: " + str(alien_O['x_position']))

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

if alien_O['speed'] == 'slow':
    x_increment = 1
elif alien_O['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_O['x_position'] = alien_O['x_position'] + x_increment

print("New x_position: " + str(alien_O['x_position']))
