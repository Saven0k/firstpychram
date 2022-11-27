#3 Задайте список из n чисел последовательности (1 + 1 / n)**n и выведите на экран их сумму.

#*Пример:*

#- Для n = 6: [2.0, 2.25, 2.37, 2.44, 2.488, 2.52]     ->       14.072    (Округлять не обязательно)

N = int(input("Enter  number:  "))

def Sum(n):
    lst = []
    for number in range(1, n+ 1):
        temp = (1 + 1 / number) ** number
        #lst.append((round((1 + 1 / number) ** number), 3))
        lst.append(round(temp, 3))
    print(lst)

Sum(N)