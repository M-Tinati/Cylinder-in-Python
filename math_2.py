#A program calculates the volume and area of ​​the entire cylinder
from math import pi

x = int(input('Enter the radius: '))
z = int(input('Enter the height: '))
print(f'radius {x} height {z}')
volume = pi * x*x * z
all =((2* pi* x)*z ) +(( pi * x ** 2 ) * 2)
print(f"cylinder volume : {volume}") 
print(f"surface Area is : {all}") 
