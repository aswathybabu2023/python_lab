def Circle(r):
    print("Area = ", 3.14 * r ** 2)
    print("Perimeter = ", 2 * 3.14 * r)


def Rectangle(l, b):
    print("Area = ", l * b)
    print("Perimeter = ", (2 * l) + (2 * b))


def Cuboid(l, w, h):
    print("Perimeter of cuboid= ", 4 * (l + w + h))
    print("Area of cuboid= ", 2 * l * w + 2 * l * h + 2 * h * w)


def Sphere(r):
    print("Perimeter of sphere = ", 2 * 3.14 * r)
    print("Area of sphere= ", 4 * 3.14 * r ** 2)


import Graphics.Circle

print("CIRCLE")
r = int(input("Enter radius "))
Graphics.Circle.Circle(r)

import Graphics.Rectangle

print("RECTANGLE")
l = int(input("Enter length "))
b = int(input("Enter breadth "))
Graphics.Rectangle.Rectangle(l, b)

from Graphics.ThreeDgraphics import Cuboid

print("CUBOID")
l = int(input("Enter length "))
w = int(input("Enter width "))
h = int(input("Enter height "))
Graphics.ThreeDgraphics.Cuboid.Cuboid(l, w, h)

from Graphics.ThreeDgraphics import Sphere

print("SPHERE")
r = int(input("Enter radius "))
Graphics.ThreeDgraphics.Sphere.Sphere(r)
