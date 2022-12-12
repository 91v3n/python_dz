lst = [3**i for i in range(5)]
lst = list(map(lambda x: x*-1 if lst.index(x)%2 else x, lst))
print(lst)