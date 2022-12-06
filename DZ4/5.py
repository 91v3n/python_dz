def rle(word):
    rle_word = ''
    pre_i = ''
    count = 0
    for i in word:
        if i != pre_i:
            if count > 1:
                rle_word += str(count) + pre_i
            else:
                rle_word += pre_i            
            count = 0
        count += 1
        pre_i = i
    else:
        if count > 1:
            rle_word += str(count) + pre_i
        else:
            rle_word += pre_i 
    print(rle_word)
    with open('rle.txt', 'w') as file:
        file.write(rle_word)

def unrle():
    unrle_word = ''
    count = ''
    with open('rle.txt', 'r') as file:
        rle_word = file.read()
    for i in rle_word:
        if i.isdigit():
            count += i
        elif not count == '':
            unrle_word += i * int(count)
            count = ''
        else:
            unrle_word += i
            count = ''
    print (unrle_word)

rle('AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool')
unrle()