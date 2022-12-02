def fibo(num):
    lst = [0]
    for i in range(0,num+1):
        if i==1:
            lst.append(1)
            lst.insert(0, 1)
        elif i==2:
            lst.append(1)
            lst.insert(0, -1)
        elif i>2:
            lst.append(lst[-1]+lst[-2])
            lst.insert(0, -lst[-1] if i%2 == 0 else lst[-1])
    return lst
print(fibo(0))
print(fibo(1))
print(fibo(2))
print(fibo(8))