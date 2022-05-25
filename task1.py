# Найти сумму чисел списка стоящих на нечетной позиции 

numbers_list = [9, 8, 6, 3, -4, 7] 

sum = 0
for i in range(len(numbers_list)):
    if (i % 2 == 0):
        sum += numbers_list[i]

print(f'Ответ : \nСумма чисел списка {numbers_list}, стоящих на нечетной позиции = {sum}')


