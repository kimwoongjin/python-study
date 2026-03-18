SCISSOR = '가위'
ROCK = '바위'
PAPER = '보'

WIN = 'WIN'
DRAW = 'DRAW'
LOSE = 'LOSE..'

mine = '가위'
yours = '바위'

if mine == yours:
    result = DRAW
else:
    if mine == SCISSOR:
        if yours == ROCK:
            result = LOSE
        else:
            result = WIN

    elif mine == ROCK:
        if yours == SCISSOR:
            result = WIN
        else:
            result = LOSE

    elif mine == PAPER:
        if yours == SCISSOR:
            result = LOSE
        else:
            result = WIN

print(result)