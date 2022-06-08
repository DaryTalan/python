import math
x = float(input("Введите число x1: "))
y = float(input("Введите число y1: "))
x2 = float(input("Введите число x2: "))
y2 = float(input("Введите число y2: "))
b = math.sqrt( ((x-x2)**2)+((y-y2)**2) )
b = round(b, 2)
print(f" Расстояние = {b}")
