# 1. Найти сумму чисел списка стоящих на нечетной позиции 

 

numbers_list = [9, 8, 6, 3, -4, 7] 

sum = 0
for i in range(len(numbers_list)):
    if (i % 2 == 0):
        sum += numbers_list[i]

print(f'Ответ : \nСумма чисел списка {numbers_list}, стоящих на нечетной позиции = {sum}')


#________________________________________________________________________________________________________________
# 2. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

#numbers_list = []
numbers_list = [2, 3, 4, 5, 6]
#numbers_list = [2, 3, 5, 6]

last_i = len(numbers_list) // 2 if  len(numbers_list) % 2 == 0 else len(numbers_list) // 2 + 1
result_list = []

for i in range(last_i):
    result_list.append(numbers_list[i] * numbers_list[len(numbers_list) - 1 - i])


print(result_list)

#__________________________________________________________________________________________________________________________
# 3. В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math
from decimal import Decimal

numbers_list = ["1.1", "1.2", "3.1", "5", "10.01"]
decimal_numbers_list = list(map(Decimal, numbers_list))


min_fractional = decimal_numbers_list[0] - math.floor(decimal_numbers_list[0])
max_fractional = decimal_numbers_list[0] - math.floor(decimal_numbers_list[0])

for i in range(len(numbers_list)):
    if decimal_numbers_list[i] - math.floor(decimal_numbers_list[i]) > max_fractional:
        max_fractional = decimal_numbers_list[i] - math.floor(decimal_numbers_list[i])
    
    if decimal_numbers_list[i] - math.floor(decimal_numbers_list[i]) < min_fractional:
        min_fractional = decimal_numbers_list[i] - math.floor(decimal_numbers_list[i])

print(f'Разница между максимальной вещественной частью и минимальной = {max_fractional - min_fractional}')

#_______________________________________________________________________________________________________
# 4. Написать программу преобразования десятичного числа в двоичное

def decimal_to_binary(number_decimal):
    if number_decimal == 0:
         return "0"

    number_binary = ""
    while (number_decimal != 0):
        number_binary = str(number_decimal % 2) + number_binary
        number_decimal //= 2
    return number_binary


number_decimal = 10

print(f'Десятичное число {number_decimal} = двоичному числу {decimal_to_binary(number_decimal)}')
