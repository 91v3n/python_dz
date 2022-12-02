def fract(num):
    num += [num.pop(0)%1 for i in range(len(num))]
    return round(max(num) - min(num), 10)

print(fract([1.1, 1.2, 3.1, 5.17, 10.02]))
print(fract([4.07, 5.1, 8.2444, 6.9814]))