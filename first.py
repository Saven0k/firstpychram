#a = int(input("Введите число - a: "))


#b = int(input("Введите число - b:  "))

#if a ** 2 == b:
#    print(f"Число {b} является квадратом числа {a} ")
#elif b ** 2 == a:
#    print(f"Число {a} является квадратом числа {b}")
#else:
#    print("Тут квадратов нет")


#print("Вводите числа массива: ")
#array = []
##for i in range(5):
#    number = int(input())
#    array.append(number)
#print(array)

#max = 0
#for i in array:
#    if i > max:
#       max = i
#
#print(max)



#N = int(input("Введите число N:  "))

#for i in range(-N, N+1):
#    print(i)


#N = float(input("Введите дробное число: "))



#4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

#def Cal(N):

#    if N % 1 == 0:
#        print("Число не дробное")
#        N = float(input("Введите дробное число: "))
#        Cal(N)

#    else:
#        N = int(N % 1 * 10)
#        print(N)

#Cal(N)

























#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

#Пример:

#- 6 -> да
#- 7 -> да
#- 1 -> нет

    #Day = int(input("Введите номер дня в недели: "))
#
#    def HollyDay(Day):
#        if Day == 6 or Day == 7:
#            print("Yes")
#        else:
#            print("no")

#    HollyDay(Day)









#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.





#Какаое значение мы бы не ввели будет True

#x = int(input("Введите значение числа x: "))
#y = int(input("Введите значение числа y: "))
#z = int(input("Введите значение числа z: "))
#def TrueorFalse(x , y , z):
#    if not(x or y or z) == ((not x) and (not y) and (not z)):
#        print(True)
#    else:
#        print(False)
#TrueorFalse(x , y , z)




# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт
# номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

#Пример:

#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

#x = int(input("Введите значение числа x: "))
#y = int(input("Введите значение числа y: "))
#
#def exercise3(x , y):
#    if x > 0 and y > 0:
#        print("1")
#    elif x > 0 and y < 0:
#        print('4')
#    elif x < 0 and y < 0:
#        print("3")
#    elif x < 0 and y > 0:
#        print("2")
#exercise3(x , y)

#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


#quarter = int(input("Введите номер четверти: "))


#def exercise4(quaeter):
#    if quaeter == 1:
#        print("x > 0 and y > 0")
#    elif quaeter == 2:
#        print("x < 0 and y > 0")
#    elif quaeter == 3:
#        print("x < 0 and y < 0")
#    elif quaeter == 4:
#        print("x > 0 and y < 0")

#exercise4(quarter)











#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.#

#Пример:
#
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21


x1 = int(input("Введите значение числа x первой точки: "))
y1 = int(input("Введите значение числа y первой точки: "))
x2 = int(input("Введите значение числа x второй точки: "))
y2 = int(input("Введите значение числа y второй точки: "))

def Distance2D(x1 , y1 , x2 , y2):
    result = round((((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5 , 3)
    print(result)
Distance2D(x1, y1, x2, y2)

















