#4) Пользователь вводит три числа. Написать "yes", если можно взять какие-то два из них и в сумме получить третье.
a = int(input())
b = int(input())
c = int(input())

if (a+b == c) or (a+c == b) or (b+c == a):
    print("yes")
else:
    print("no")