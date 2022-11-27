#2 семинар
#Задание на семинаре

'''
1. Напишите программу, которая принимает на вход число N и выдаёт
последовательность из N членов.

*Пример:*

- Для N = 5: 1, -3, 9, -27, 81




N = int(input("Введите число N: "))

lst = []

first = -3

i = 0

while i < N:
    for item in range(N):
        lst.append(first ** i)
        i += 1


print(lst)
'''




'''
2. Для натурального n создать список,
состоящий из элементов последовательности 3n + 1.

*Пример:*

- Для n = 4: [1, 4, 7, 10, 13]



lst = []

N = int(input("Введите число N: "))

for i in range(0, N+1):
    lst.append(3 * i + 1)

print(f' Для N = {N} :  {lst}')

'''


'''
3. Напишите программу, в которой пользователь будет задавать две строки,
а программа - определять количество вхождений одной строки в другой.

s1 = 'aaababaewfwef'
s2 = 'aba'

print(s1.count(s2))
'''


s1 = str(input("Введите первую строчку: "))
s2 = str(input("Введите вторую строчку: "))

def Check_in_or_no(string1 , string2):
    count = 0
    if string1 == string2:
        print("Строчки равны")
        s1 = str(input("Введите первую строчку: "))
        s2 = str(input("Введите вторую строчку: "))
        Check_in_or_no(s1 , s2)
    else:
        i = 0
        while i + len(string2) < len(string1):
            if string1[i:i + len(string2)] == string2:
                count += 1
            i += 1
    print(count)
Check_in_or_no(s1, s2)







