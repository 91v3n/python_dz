# Решил сделать по своему. Проверок ни каких не делал. Надеюсь такого варианта ни у кого нет =)

def prnt (game):
    print(game[0], game[1], game[2])
    print(game[3], game[4], game[5])
    print(game[6], game[7], game[8])

def start(game, player):
    if player%2:
        pos = int(input('Куда поставить X '))-1
        game[pos] = 'X'
    else:
        pos = int(input('Куда поставить O '))-1
        game[pos] = 'O'
    return game
    
def winner (game, win):
    for i in range(8):
        if game[win[i][0]] == 'O' and game[win[i][1]] == 'O' and game[win[i][2]] == 'O':
            print('ПОБЕДА НОЛИКОВ')
            return True
        elif game[win[i][0]] == 'X' and game[win[i][1]] == 'X' and game[win[i][2]] == 'X':
            print('ПОБЕДА КРЕСТИКОВ')
            return True
    return False

game = [x for x in range(1,10)]
win = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
player = 1
prnt(game)
game = ['*' for x in range(1,10)]

while winner(game, win) != True and player < 10:
    game = start(game, player)
    prnt(game)
    player += 1
else:
    print('ГЕЙМ ОВЕР')

    