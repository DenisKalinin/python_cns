#1. Написать функцию принимающую на вход число и возвращающую последовательность чисел Фибоначи до этого числа.

n = int(input())

def fibo(n):
        if n >= 1:
            f = [0, 1]
            for i in range(2, n + 1):
                f.append(f[i - 1] + f[i - 2])
            return f
        elif n == 0:
            f = [0]
            return f

print(fibo(n))