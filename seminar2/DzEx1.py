'''
1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

*Пример:*

- 6782 -> 23
- 0.56 -> 11
'''

number = float(input("Enter a  real number: "))

def Sum(nm):
        result = 0.0
        while nm / 10 != 0:
                nm = nm * 10
        while nm / 10 > 0:
                result = result + (nm / 10)
        print(result)


Sum(number)


#Не работает