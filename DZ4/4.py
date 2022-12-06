def cesar(word, key):
    abc = 'abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz'
    cesar_word = ''
    for i in word:
        lit = abc.find(i)
        cesar_word += abc[lit+key]
    print(cesar_word)
    with open('cesar.txt', 'w') as file:
        file.write(cesar_word)

def uncesar(key):
    abc = 'zyxwvutsrqponmlkjihgfedcba zyxwvutsrqponmlkjihgfedcba'
    uncesar_word = ''  
    with open('cesar.txt', 'r') as file:
        cesar_word = file.read()
    for i in cesar_word:
        lit = abc.find(i)
        uncesar_word += abc[lit+key]
    print (uncesar_word)      

cesar(input('enter word '), int(input('enter key ')))
uncesar(int(input('enter key ')))