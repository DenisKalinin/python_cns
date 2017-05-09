'''6. Написать функцию-фабрику, которая будет возвращать функцию умножения на аргумент
Пример:
mult5 = multiple_inner(5)
print(mult5(7))
35'''

def multiple_inner(n):
    def mult(x):
        return x * n
    return mult

mult5 = multiple_inner(5)
print(mult5(7))