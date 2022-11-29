# 3 - Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.

from random import randint
array = [randint(-99,99) for i in range(int(input('введите размер массива ')))]
print(array)

i=0
while i < len(array):
    if array[i] < 0:
        array.insert(i+1, 0)
    i+=1
print(array)