import math

# Function to calculate circumference
def calculate_circumference(radius):
    return 2 * math.pi * radius

# Input from user
radius = float(input("Enter the radius of the circle: "))

# Calculate and display the result
circumference = calculate_circumference(radius)
print(f"The circumference of the circle is: {circumference:.2f}")
