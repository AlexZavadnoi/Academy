"""
Переменной var_int - 10, var_float - значение 8.4, var_str - "No".
Значение, хранимое в переменной var_int,
увеличьте в 3.5 раза. Полученный результат свяжите с переменной var_big.
Измените значение, хранимое в переменной var_float,
уменьшив его на единицу, результат свяжите с той же переменной.
Разделите var_int на var_float, а затем var_big на var_float.
Результат данных выражений не привязывайте ни к каким переменным.
Измените значение переменной var_str на "NoNoYesYesYes".
Выведите значения всех переменных.
"""

var_int = 10
var_float = 8.4
var_str = "No"

var_big = var_int * 3.5
var_float = var_float - 1

print(var_int / var_float)
print(var_big / var_float)
print(var_str*2 + "Yes"*3)