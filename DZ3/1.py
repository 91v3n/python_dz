from random import randint

def odd(num):
    sum = 0
    for i in num[1::2]:
        sum += i
    return sum

num = [randint(1,9) for i in range(int(input('введите размер массива ')))]
print (num)
print (num[1::2])
print (odd(num))