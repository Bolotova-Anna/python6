# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
a = int(input("введите первый лемент"))
n = int(input("введите количество элементов"))
d = int(input("введите разность"))
array = []
for i in range(n):
    prog = a+i*d
    array.append(prog)
print(array)
