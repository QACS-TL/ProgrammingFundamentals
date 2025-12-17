import math

def convert_length(value, units):
    if units == "metres":
        return  value / 100.0
    return value


def print_area(shape, details, area, units, decimals):
    print(
        f"The area of a {shape} {details} is {round(area, decimals)} square {units}"
    )


def rectangle_area_calculator(height, width, units="cms"):
    height = convert_length(height, units)
    width = convert_length(width, units)

    area = height * width
    return area
    #print_area("rectangle",  f"of height {height} and width {width}", area, units, 2)

def triangle_area_calculator(height, width, units):
    height = convert_length(height, units)
    width = convert_length(width, units)

    area = 0.5 * height * width

    print_area("triangle",  f"of height {height} and width {width}", area, units, 2)

def circle_area_calculator(radius, units):
    height = convert_length(radius, units)

    area = math.pi  * math.pow(radius, 2)

    print_area("circle", f"of radius {radius}", area, units, 2)


print("*** Rectangle Area Calculator ***")
h = int(input("Enter the height (in cm): "))
w = int(input("Enter the width (in cm): "))
a = rectangle_area_calculator( width=w, height=h)
rectangle_area_calculator(h, w, "metres")

print("*** Triangle Area Calculator ***")
triangle_area_calculator(h, w, "cm")
triangle_area_calculator(h, w, "metres")

print("*** Circle Area Calculator ***")
radius = int(input("Enter the radius of a circle (in cm): "))
circle_area_calculator(radius, "cm")
circle_area_calculator(radius, "metres")


