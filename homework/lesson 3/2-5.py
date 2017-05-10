#5. Написать функцию, которой можно передавать аргументы либо списком/кортежем, либо по одному.
# Функция производит суммирование всех аргументов
n=0
def amount(i):
    global n
    if type(i) == int:
        n += i
        return n
    else:
        return sum(i)

print(amount((7, 7, 7)))
print(amount([1, 3, 5, 6]))
print(amount(5))
print(amount([3, 5]))
print(amount(5))
print(amount((7, 4)))
print(amount(3))
