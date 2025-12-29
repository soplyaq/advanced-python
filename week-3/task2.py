import math

a = float(input("Enter side: "))

triangle_area = (math.sqrt(3) / 4) * a * a
hex_area = 6 * triangle_area

print(hex_area)
4