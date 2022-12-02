def bn(num):
    return bn(num//2) * 10 + num%2 if num > 0 else 0

print(bn(45))