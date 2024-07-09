import math

def area_of_circle(radius):
    return math.pi * radius * radius

# Example usage
radius = float(input("Enter the radius of the circle : "))
area = area_of_circle(radius)
print(f"The area of the circle with radius {radius} is {area:.2f}")
