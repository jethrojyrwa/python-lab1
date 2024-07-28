#Lab exercise 1: question 7
import math

def areaBH(base,height):
    return 0.5 * (base * height)

def areaSides():
    print("\nEnter sides of triangle:")
    
    a = float(input("Enter length of side a: "))
    b = float(input("Enter length of side b: "))
    c = float(input("Enter length of side c: "))

    s = (a+b+c)/2

    area = math.sqrt((s*(s-a))*(s*(s-b))*(s*(s-c)))
    return area

print("PART 1")
base = float(input("Enter base of the triangle: "))
height = float(input("Enter height of the triangle: "))

area = areaBH(base,height)

print("Area of the Triangle = ",area)

print("\n\nPART 2")

print("Triangle 1:")
area1 = areaSides()

print("\nTriangle 2:")
area2 = areaSides()

totalArea = area1 + area2
print("\nArea enclosed by both triangles = ", totalArea)

cont1 = (area1/totalArea) * 100
cont2 = (area2/totalArea) * 100

print("\nTriangle 1's contribution to the area = ",cont1,"%")
print("Triangle 2's contribution to the area = ",cont2,"%")
