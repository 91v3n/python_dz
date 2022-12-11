def player(x):
    from random import randint
    if randint(0,1) == 0:
        while x > 0:
            step = int(input(f'Сколько конфет возьмёт первый игрок не более 28 из {x} - '))
            x -= step
            if x > 0:
                step = int(input(f'Сколько конфет возьмёт второй игрок не более 28 из {x} - '))
                x -= step
            else:
                print('Все конфеты забирает первый игрок')
                break
        else:
            print('Все конфеты забирает второй игрок')
    else:
        while x > 0:
            step = int(input(f'Сколько конфет возьмёт второй игрок не более 28 из {x} - '))
            x -= step
            if x > 0:
                step = int(input(f'Сколько конфет возьмёт первый игрок не более 28 из {x} - '))
                x -= step
            else:
                print('Все конфеты забирает второй игрок')
                break
        else:
            print('Все конфеты забирает первый игрок')

def bot(x):
    from random import randint
    step = 0
    if randint(0,1) == 0:
        while x > 0:
            step = int(input(f'Сколько конфет возьмёт игрок не более 28 из {x} - '))
            x -= step
            if x > 0:
                step = 29 - step
                x -= step
                print(f'бот взял {step} конфет осталось {x}')
            else:
                print('Все конфеты забирает игрок')
                break
        else:
            print('Все конфеты забирает Бот')
    else:
        while x > 0:
            if x < 29:
                print (f'бот взял {x} и выигрывает игру')
                x = 0
            elif step == 0:
                print(f'бот взял {step} конфет осталось {x}')
            else:
                step = 29 - step
                x -= step
                print(f'бот взял {step} конфет осталось {x}')
            if x > 0:
                step = int(input(f'Сколько конфет возьмёт игрок не более 28 из {x} - '))
                x -= step
            else:
                print('Все конфеты забирает бот')
                break
        else:
            print('Все конфеты забирает игрок')

candy = 145
if input('для игры с ботом введите 1, для игры с игроком 2 - ') == '1':
    bot(candy)
else:
    player(candy)
