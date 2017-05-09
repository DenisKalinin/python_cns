#4. Написать функцию square, принимающую 2 аргумента — длину сторон прямогольника, и возвращающую 3 значения: периметр,
#  площадь и диагональ прямоугольника.

import math
print("Введите стороны треуголиника:")
a = int(input())
b = int(input())
def square(a, b):
    P = 2*(a+b)
    S = a*b
    D = math.sqrt(a**2 + b**2)
    return P, S, D

print(square(a, b))