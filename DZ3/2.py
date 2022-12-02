def pair(num):
    half = len(num)//2+1 if len(num)%2 !=0 else len(num)//2
    print([num[i]*num[-i-1] for i in range(half)])

pair([2,3,5,6])
pair([2,3,4,5,6])