# This code will calculate the area of a circle from the user-supplied radius

# Call the math function
import math

print('This code will calculate and print the area of a circle based on the radius provided.')

# Request radius of circle from user
radius = input('Please enter the radius of the circle: ')

# Calculate area of the circle
area = math.pi * int(radius)**2

# Print calculated area of circle to screen
print(f'The area of the circle is {area}.')
