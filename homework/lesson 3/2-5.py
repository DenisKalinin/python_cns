#5. Написать функцию, которой можно передавать аргументы либо списком/кортежем, либо по одному.
# Функция производит суммирование всех аргументов

def amount(*args):
    n = 0
    for i in args:
        if type(i) == int:
            n = sum(args)
        else:
            n+=sum(i)
    return n

print(amount([1, 3, 5, 6]))
print(amount(1, 2, 4, 4, 5))
print(amount((1, 3, 4, 1)))
print(amount([3,]))
print(amount(2))
print(amount((1,)))