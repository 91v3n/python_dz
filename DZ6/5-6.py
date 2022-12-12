# задача 5
from random import randint
lst = [randint(1,100) for i in range(200)]
lst = [(i, lst[i]) for i in range(len(lst)) if lst[i]!=i]
print(lst)

# задача 6
lst = [i for i in lst if not sum(i)%5]
print(lst)