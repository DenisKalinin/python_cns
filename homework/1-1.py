#1) Дан список [1, 2, 3, 4, 5]. Вывести квадраты всех чисел из списка
li1 = [1, 2, 3, 4, 5]
i = 0

for x in li1:
    print(li1[i] * li1[i])
    i += 1

'''while i < len(li1):
    print(li1[i]*li1[i])
    i = i + 1'''