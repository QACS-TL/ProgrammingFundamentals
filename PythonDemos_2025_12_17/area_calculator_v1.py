import math

def rectangle_area_calculator(height, width, units):
    if units == "metres":
        height = height /100
        width = width / 100
    area = height * width
    print(f"The area of a rectangle of height {height} and width {width} is {round(area, 2)} square {units}")

def triangle_area_calculator(height, width, units):
    if units == "metres":
        height = height /100
        width = width / 100
    area = 0.5 * height * width
    print(f"The area of a triangle of height {height} and width {width} is {round(area, 2)} square {units}")

def circle_area_calculator(radius, units):
    if units == "metres":
        radius = radius /100
    area = math.pi  * math.pow(radius, 2)
    print(f"The area of a circle of radius {radius} is {round(area, 4)} square {units}")


print("*** Rectangle Area Calculator ***")
height = int(input("Enter the height (in cm): "))
width = int(input("Enter the width (in cm): "))
rectangle_area_calculator(height, width, "cm")
rectangle_area_calculator(height, width, "metres")

print("*** Triangle Area Calculator ***")
triangle_area_calculator(height, width, "cm")
triangle_area_calculator(height, width, "metres")

print("*** Circle Area Calculator ***")
radius = int(input("Enter the radius of a circle (in cm): "))
circle_area_calculator(radius, "cm")
circle_area_calculator(radius, "metres")


