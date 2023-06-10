# Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше 
# заданного максимума)
minimum = -3
maximum = 4
array = [1,7,4,9,11,-1]
array2 = []
for i in range(len(array)):
    if array[i] > minimum and array[i] <maximum:
        array2.append(array[i])
print(array2)