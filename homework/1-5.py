#5) Пользователь вводит число N. Создать массив размера N, который одинаково читается как слева направо, так и справа налево.

N = int(input())

l1 = [x for x in range(0, N+1)]
l1 = l1[0:int(N/2)]

if N%2:
    l1 += reversed(l1)
    l1.insert(int(N/2), int(N/2))
else:
    l1 += reversed(l1)

print(l1)