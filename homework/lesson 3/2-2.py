#2. Пользователь делает вклад в размере n рублей сроком на years лет под 10% годовых (каждый год размер его вклада
# увеличивается на 10%). Каждый год пользователь докладывает в банк сумму в  m рублей. (Эти деньги прибавляются к
# сумме вклада, и на них в следующем году тоже будут проценты) Написать функцию bank, принимающая аргументы n, m и
# years, и возвращающую сумму, которая будет на счету пользователя.

print("Введите размер вклада:")
n = int(input())
print("Введите срок вклада:")
y = int(input())
print("Введите сумму ежегодного пополнения вклада:")
m = int(input())

def bank(n, y, m=None):
    for i in range(y):
        p = int(n * 0.1)
        n += p
        if i <= y - 2:
            n += m
    return n
print(bank(n, y, m))