from random import randint

#4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# #Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.


N = int(input("Enter number: "))

fp = int(input("Enter first position: "))

sp = int(input("Enter second position: "))

def Find_Work(n , first_position , second_position):
    lst = []
    for number in range(-n , n + 1):
        lst.append(number)
    #print(lst)

    work = lst[first_position] * lst[second_position]
    #print(work)

    print(f"For {N} : {lst} -> work  =  {work}")

Find_Work(N , fp , sp)