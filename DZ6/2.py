lst = [2, 5, 3, 4, 1, 4, 3]
print([lst[i]+lst[-1-i] for i in range(len(lst)//2+1)])