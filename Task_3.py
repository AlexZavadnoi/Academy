"""
Напишите программу, которая запрашивает с ввода восемь чисел, добавляет их в список.
На экран выводит их сумму, максимальное и минимальное из них.
"""

list_numbers = input("Введите 8 чисел через пробел: ").split()
#print("Список чисел : ", list_numbers)

num_list = list(map(float, list_numbers))
print("Список чисел", num_list)
print("Сумма списка = ", sum(num_list))
print("Максимальное число - ", max(num_list))
print("Миниальное число - ", min(num_list))