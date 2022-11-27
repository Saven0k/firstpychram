from random import randint

#5 Реализуйте алгоритм перемешивания списка.
#Из библиотеки random использовать можно только randint
lst = []

for i in range(5):
    lst.append(int(input("Enter number: ")))
#print(lst)

def Change_elements_in_list(Some_list):
    lst2 = []
    for i in Some_list:
        x = randint(Some_list[0], Some_list[-1])
        if x  in lst2:
            y = randint(Some_list[0], Some_list[-1])
            lst2.append(y)
        else:
            lst2.append(x)
    print(lst2)

Change_elements_in_list(lst)

#Почему то не работает для ЦИФР больше 5 попробывал все поменять не получилось
