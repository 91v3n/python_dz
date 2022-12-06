def prime(num):
    prime_list = []
    first = 2
    while first <= num:
        if num%first == 0 and first not in prime_list:
            prime_list.append(first)
            num //= first
        else:
            first+=1
    return prime_list

print(prime(int(input('enter number '))))
