#6) Пользователь вводит строку. Напечатать словарь, ключами которого являются четные символы строки, а значениями нечетные. Если последнему ключу не хватает значения, не добавлять его в словарь.

a = input()
b = {}
c = 1
d = 0

a = a.replace(' ', '')
a = list(a)

if (len(a)%2 != 0):
    del a[-1]

for i in range(int(len(a)/2)):
    b[a[c]] = a[d]
    c += 2
    d += 2

print(b)