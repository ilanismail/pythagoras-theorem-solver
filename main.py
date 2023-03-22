#equations
#c^2 - b^2 = a^2
#c^2 - a^2 = b^2
#a^2 + b^2 = c^2 

#importing the math lib
import math

#selecting any side you want of the triangle
side = input("Give the side you want to solve for (a, b, or c): ")

#solving side a of the triangle
if side == "a":
    b = float(input("Give Side b: "))
    c = float(input("Give Side c: "))   
    a = math.sqrt(c ** 2 - b ** 2)
    print(f"The length of the side a is {a}")

#solving side b of the triangle
if side == "b":
    a = float(input("Give Side a: "))    
    c = float (input("Give Side c:"))
    b = math.sqrt(c ** 2 - a ** 2)
    print(f"The length of the side b is {b}")

#solving hypotenuse of the triangle
if side == "c":
    a = float(input("Give Side a: "))    
    b = float(input("Give Side b: "))
    c = math.sqrt(a ** 2 + b ** 2)
    print(f"The length of the hypotenuse is {c}")

#if any invalid input is there
else:
    print("Invalid input")    