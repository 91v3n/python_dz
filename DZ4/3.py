def check(path):
    file = open(path, 'r')
    temp = file.read().split()
    i=2
    while i <= len(temp):
        if temp[i] == '5':
            temp[i-2] = temp[i-2].upper()
            temp[i-1] = temp[i-1].upper()
        i+=3
        print(temp)
    file.close
    file = open(path, 'w')
    i=0
    while i <= len(temp)-3:
        file.write(f'{temp[i]} {temp[i+1]} {temp[i+2]}\n')
        i+=3
    file.close
    
check('file.txt')